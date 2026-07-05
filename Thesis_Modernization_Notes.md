# Thesis Modernization Notes
## "A Queueing-Oriented Decision Process for Capacity Planning in a Job Shop Environment"
### Reference Document — All Clarifications, Corrections & Future Vision
### Mohamed M3 · June 2026

---

## PURPOSE OF THIS DOCUMENT

This document consolidates ALL clarifications, corrections, and design decisions
made during the modernization of the 1999 M.Sc. thesis into a Python platform.
It serves as:
- The single reference for all CL-1 to CL-13 clarifications
- A correction log for thesis ambiguities resolved during implementation
- A generalization guide for applying the framework to other fields
- The foundation for the Digital Twin extension (Sessions 31-33)

The dashboard (dashboard.py) references this document rather than cluttering
the UI with technical notes.

---

## SECTION A — ALL CLARIFICATIONS (CL-1 to CL-13)

### CL-1: Total Cost (F1) Source
```
F1 = Average Total Cost per unit — taken DIRECTLY from Table 4.3
No need to compute from DL, DM, IDL, IDM individually for case study.
Future work: compute from detailed cost equations (Table 4.2).
```

### CL-2: Table 4.9 Units
```
ALL values in Table 4.9 are PER UNIT per product:
  SP   = Gross Revenue (Selling Price) [$/unit]
  F1   = Average Total Cost [$/unit]
  NR   = Net Revenue [$/unit] = SP - F1
  Hours = Total machining time [hrs/unit] across ALL 3 stages
```

### CL-3: F1/SP Ratio
```
F1/SP ≈ 0.80 observed for ALL 6 products in this case study.
This is a case-study-specific observation, NOT a universal rule.
In general: F1/SP can vary (+/- 0.80).
Only constraint: F1 < SP (otherwise NR < 0 = loss).
```

### CL-4: NR(S) — Non-Linear with S
```
NR(S) is NOT constant and NOT linear as S increases.
Two competing effects:
  + More servers → higher server operating cost → F1 increases
  - More servers → shorter Ws → lower waiting cost → F1 decreases
Result: F1(S) is a NON-LINEAR mix function with a minimum at optimal S*.
Simplified model used: NR(S) = NR_base / S (approximation only)
```

### CL-5: Negative/Abnormal Rn Values
```
When S is too large: Rn turns negative (server cost > revenue).
Thesis convention: treat negative Rn as ZERO.
These are "abnormal" values — comment them, do not use for decisions.
Break-even S = last S where Rn > 0 → effective capacity limit.
```

### CL-6: μ in Table 4.9 = Service RATE
```
PROVEN: μ column in Table 4.9 = SERVICE RATE [u/hr]
Verification: ρ = λ/μ matches ALL 6 products exactly:
  8BD:      2/80  = 0.025 ✓
  8BK:      4/120 = 0.033 ✓
  8FJ500:   6/80  = 0.075 ✓
  8AS10:    4/16  = 0.250 ✓
  3CF12KVA: 2/8   = 0.250 ✓
  G.T3:     2/6   = 0.333 ✓ (BOTTLENECK)
```

### CL-7: Eq 3.8 Parameter μ
```
Eq 3.8: λ** = 2T(Sμ)² / (1 + 2TSμ)
  μ = service rate [u/hr] — SAME μ as queue formulas
  c = 8 hrs/shift — PHYSICAL meaning of shift capacity
  T = patient/reneging time in queue [0.1..1.0 hr]
Table 22 validation: T=0.2, μ=9.23 gives EXACT λ** values ✓
```

### CL-8: λ** Integer Rounding
```
λ** from Eq 3.8 is ROUNDED to nearest integer.
Reason: practical production — cannot produce fractional units.
Table 22 uses T=0.2 as reference → exact match after rounding ✓
```

### CL-9: Per-Unit Values (Table 4.3)
```
Direct per-unit values for all 6 products:
  Product    SP($)    F1($)    NR($)   Total_hrs
  8BD        45,000   36,000   9,000      80
  8BK        55,000   44,000  11,000     120
  8FJ500     25,000   20,000   5,000      80
  8AS10      15,000   12,000   3,000      16
  3CF12KVA    3,000    2,400     600       8
  G.T3        8,000    6,400   1,600       6

NOTE: SP_standard_parts = 25,000 in Table 4.2 represents variable
imported parts cost — EXCLUDED from Rn calculations.
It is NOT a cost per server — it is added to material cost only.
```

### CL-10: Two μ Concepts
```
CONCEPT A: μ in Table 4.9 = SERVICE RATE [u/hr]
  → Used in: ρ = λ/μ, M/M/S queue formulas (Eqs 3.1-3.7)
  → Proven: ρ matches ALL 6 products exactly ✓

CONCEPT B: "Hours" in Table 4.3 = SERVICE TIME [hrs/unit]
  → Total machining time across ALL 3 stages
  → Used for: stage-level μ allocation in simulation
  → Stage split ratios:
      Simplified: [1/3 : 1/3 : 1/3] × total_hours
      Actual:     [0.2 : 0.5 : 0.3] × total_hours

Conversion: μ_stage_j = 1 / (total_hours × ratio_j)  [u/hr]
```

### CL-11: Scheduling Process
```
POINT 1 — BOM Simplification:
  Each product = BOM list of 100+ small parts (Bill of Materials)
  Simplified to ONE aggregate part for modeling tractability
  μ = total machining time for ALL parts combined
  Applies to all 6 products

POINT 2 — Monthly Scheduling Logic:
  Period = MONTHLY production plan
  Process:
    → Select products (ALL 6 or SUBSET based on demand)
    → Load ONE BY ONE through serving system
    → ORDER = HIGH PRIORITY first (by ρ or NR)
    → This IS the Exhaustive/Gated polling discipline
  Priority order (by actual ρ, highest first):
    1. G.T3       (ρ=0.135, λ=0.807)
    2. 3CF12KVA   (ρ=0.125, λ=1.000)
    3. 8AS10      (ρ=0.017, λ=0.273)
    4. 8BD        (ρ=0.006, λ=0.467)
    5. 8FJ500     (ρ=0.003, λ=0.273)
    6. 8BK        (ρ=0.003, λ=0.302)

POINT 3 — Actual Factory Capacity:
  ACTUAL servers per stage (CL-12):
    Stage 1 (Cutting):  S = 5
    Stage 2 (Punching): S = 3  (recently +2 added)
    Stage 3 (Bending):  S = 5
  S = 156+ is NOT APPLICABLE (was computed error, not real)
  Capacity expansion = MORE SHIFTS (not more servers):
    1 shift  =  8 hrs/day  (baseline)
    2 shifts = 16 hrs/day  (expansion option A)
    3 shifts = 24 hrs/day  (expansion option B)

POINT 4 — Two λ Data Sources:
  λ_experimental (Table 4.9) = DESIGN TARGET values
    [2, 4, 6, 4, 2, 2] u/hr — used for capacity planning
  λ_actual (MPS Tables 4.5-4.8) = current real production rates
    [0.467, 0.302, 0.273, 0.273, 1.000, 0.807] u/hr — all ≤ 1
  Total ρ_actual = 0.288 (lightly loaded)
  Total ρ_experimental = 0.967 (near capacity, design target)
```

### CL-12: Server Types per Stage (Machine Groups)
```
WITHIN each stage: ALL servers are SAME TYPE → M/M/S valid
ACROSS stages: DIFFERENT machine types → different μ per stage

Stage 1 = Group 1 = Cutting machines (shears)   S=5 → M/M/5
Stage 2 = Group 2 = Punching machines            S=3 → M/M/3 ← BOTTLENECK
Stage 3 = Group 3 = Bending machines             S=5 → M/M/5

Single-queue engine (Stage 1 models): same-type servers ✓
Multi-queue engine (Stages 2-3): different types per stage ✓
Bottleneck: Stage 2 — fewest servers AND 50% of machining time
```

### CL-13: F1(S) Non-Linear Cost Behavior
```
F1(S) = f(server_cost ↑, waiting_cost ↓) — competing effects

As S increases:
  [+] Server operating cost INCREASES (more machines running)
  [-] Waiting time Ws(S) DECREASES (less congestion = less idle cost)
  Result: F1(S) is NON-LINEAR, NOT monotone

Real behavior:
  F1 high at S=1  → Ws cost dominates (long queues)
  F1 decreases    → toward optimal zone
  F1 minimum      → at optimal S*
  F1 increases    → server cost dominates (idle machines)
  Rn < 0          → beyond break-even → treat as 0 (CL-5)

This is the fundamental economic tradeoff of the thesis.
Rn(S) = λ** × (SP - F1(S)) has TRUE maximum at optimal S*.
Dashboard Tab 2 shows this non-linear curve.
```

---

## SECTION B — CORRECTIONS TO ORIGINAL THESIS

```
CORRECTION 1: μ Interpretation
  Original: μ column labelled ambiguously as "service rate"
  Resolved: μ = service RATE [u/hr], proven by ρ = λ/μ exact match
  Impact: All queue calculations use μ as rate, not time ✓

CORRECTION 2: λ Values in Table 4.9
  Original: λ = [2,4,6,4,2,2] presented without context
  Resolved: These are EXPERIMENTAL design targets, NOT actual MPS rates
  Actual λ from MPS (Tables 4.5-4.8): all ≤ 1 u/hr
  Impact: Dashboard shows both modes clearly

CORRECTION 3: S=156+ Server Count
  Original: Formula-computed S needed for stability was 156+
  Resolved: NOT applicable — factory uses real S=[5,3,5]
  Reason: Capacity expansion = shifts, not servers (CL-11 Point 3)
  Impact: Simulation uses actual S=[5,3,5]

CORRECTION 4: F1/SP = 0.80 Universality
  Original: Appeared as universal constraint
  Resolved: Case-study-specific observation, not a rule
  Impact: General tool does not enforce this ratio

CORRECTION 5: SP = 25,000 in Rn Formula
  Original: SP_standard_parts = 25,000 included in cost
  Resolved: This represents variable imported parts — EXCLUDED
  Impact: Rn calculation uses NR directly, not SP-25000

CORRECTION 6: Table 4.9 "Hours" Column
  Original: Could be interpreted as service rate
  Resolved: = Total service TIME [hrs/unit] across ALL 3 stages
  Impact: Stage allocation uses hours × ratio, not rate
```

---

## SECTION C — VALIDATION RESULTS SUMMARY

```
MODULE             VALIDATION           RESULT
─────────────────────────────────────────────────────────
queue_engine.py    Stage 1 (20 models)  19/21 PASS
                   Stage 2 (Jackson)    ALL PASS
                   Stage 3 (policies)   ALL PASS
                   Gated E[L] reduction 67-97% ✓
                   Bottleneck = G.T3    ρ=0.333 ✓

capacity_planner   Table 22 λ**         7/7 EXACT MATCH ✓
                   S* optimizer         S*=8 all T ✓
                   NR_pu × S constant   CONFIRMED ✓

simpy_engine       M/M/1 deviation      < 3% ✓
                   M/M/2 deviation      < 3% ✓
                   Bottleneck (series)  EXACT MATCH ✓
                   G.T3 bottleneck      CONFIRMED ✓

dashboard          6 tabs functional    ALL PASS ✓
                   Syntax check         CLEAN ✓
                   All formulas embed   VERIFIED ✓

KNOWN DEVIATIONS (acceptable):
  MMSKK finite-pop: Ws=1/μ for K=4 (thesis interpretation)
  Rn absolute scale: proportional to NR_base parameter
  Stage 2 stability: very long service times with S=[5,3,5]
```

---

## SECTION D — GENERALIZATION TO OTHER FIELDS

```
The framework is GENERIC — same equations, different context:

PARAMETER MAPPING TABLE:
─────────────────────────────────────────────────────────────
Parameter   Manufacturing      Healthcare       Services
─────────────────────────────────────────────────────────────
λ           Production rate    Patient arrival  Customer rate
μ           Machine rate       Doctor rate      Agent rate
S           Machines/stage     Doctors/dept     Agents/desk
ρ           Machine util.      Doctor util.     Agent util.
Lq          WIP in queue       Patients waiting Customers wait
Wq          Queue wait time    Wait for doctor  Queue time
Ws          Total proc. time   Total care time  Total service
Rn          Net revenue        Cost savings     Net profit
Bottleneck  Slowest stage      Busiest dept     Slowest step
Policy      Exhaustive/Gated   FIFO/Priority    FIFO/Priority
─────────────────────────────────────────────────────────────

TEMPLATE STRUCTURE (from Roadmap document):
  Template 1: Single Server     ← Stage 1 (done ✓)
  Template 2: Series Stages     ← Stage 2 (done ✓)
  Template 3: General Job Shop  ← Stage 3 (done ✓)
  Template 4: Healthcare Systems      ← Future
  Template 5: Logistics & Warehousing ← Future
  Template 6: Supply Chain Networks   ← Future
  Future: Transportation, Call Centers, Smart Manufacturing,
          Airports, Ports, Maintenance Systems

KEY INSIGHT: The simulation ENGINE is the same.
Only the DOMAIN PARAMETERS change per template.
This is the power of the queueing theory foundation.
```

---

## SECTION E — FUTURE DEVELOPMENT ROADMAP

```
PHASE 1 (Current — Sessions 24-30):
  ✅ queue_engine.py      — All 3 stages analytical
  ✅ capacity_planner.py  — Economic optimization
  ✅ simpy_engine.py      — DES validation
  ✅ dashboard.py         — 6-tab interactive UI
  ⏳ distribution_fitting.py — Input layer (Session 30)

PHASE 2 — Digital Twin (Sessions 31-33):

  Session 31: live_simulation.py (Option B Phase 1)
    - SimPy backend runs in background thread
    - Streamlit shows live KPI updates
    - Machine status per stage (Busy/Idle/Queue count)
    - Bottleneck alert: ⚠️ Stage 2 SATURATED
    - Experiment runner: change S/policy/shifts → instant results
    - Real-time metrics: Lq, Wq, throughput, utilization

  Session 32: dashboard.py UPGRADE (Option B Phase 2)
    - Tab 7: 🔴 Live Simulation
        Run/Pause/Reset controls
        Real-time gauges and progress bars
        Machine utilization display
    - Tab 8: 📊 Statistical Reports
        Gantt chart (job scheduling visualization)
        Scenario A vs B comparison table
        Export results to CSV

  Session 33: animation_engine.py (Option C)
    - Plotly animated factory floor
    - Jobs (colored dots) moving Stage1→Stage2→Stage3
    - Machine busy/idle state visualization
    - Speed control slider
    - Product type color coding

PHASE 3 — Multi-Domain Templates (Future):
  - Adapt distribution_fitting.py for each domain
  - Create domain-specific input templates
  - Healthcare: patient flows, doctor schedules
  - Logistics: warehouse picking, shipping lanes
  - Services: call center, bank teller, help desk
  - Each template shares the SAME core engine

LONG-TERM VISION:
  One modular, reusable, scalable simulation platform
  Single engine → multiple application templates
  Configurable via domain parameters
  Suitable for: education, research, real-world decisions
```

---

## SECTION F — INPUT DATA DESIGN (for distribution_fitting.py)

```
TWO-LEVEL INPUT ARCHITECTURE:

LEVEL 1 — Sales Forecast (Strategic):
  Source: Sales Department
  Period: Annual / Quarterly
  Data:   Predicted demand [units/period]
  Transform: λ_i = demand_i / (working_days × hrs_per_shift)
  Used for: Capacity PLANNING (design targets)

LEVEL 2 — MPS (Operational):
  Source: Planning Department
  Period: Monthly / Weekly
  Data:   Confirmed production orders [units/month]
  Transform: λ_i = orders_i / (working_days × 8)
  Used for: Scheduling & CONTROL (actual rates)

THREE-STEP UI:
  Step 1: Demand → λ (generic product labels P1, P2, ...)
  Step 2: Service times → μ per stage
  Step 3: Cost input (Simple OR Detailed)
          Simple:   SP, F1 direct → NR = SP - F1
          Detailed: DL, DM, IDL, IDM, D_MAT → F1(S) computed
          NOTE: SP_standard_parts EXCLUDED from calculations

DISTRIBUTION FITTING:
  Arrivals:     Poisson assumed (thesis + real-world typical)
  Service time: Test Exponential → Gamma → Erlang → General
  Output: fitted λ_i, μ_j + recommended queue model type
```

---

## SECTION G — DASHBOARD CLEAN REFERENCE

```
The dashboard (dashboard.py) is kept CLEAN.
All CL references are in THIS document.
Dashboard uses brief tooltips (ℹ️) only.

TAB REFERENCE GUIDE:
  Tab 1 📊 Queue Analysis      → CL-6, CL-12
  Tab 2 💰 Capacity Planning   → CL-7, CL-8, CL-13
  Tab 3 📅 Monthly Schedule    → CL-11
  Tab 4 🔬 Case Study          → CL-9, CL-10
  Tab 5 🔗 Series Queues       → CL-10, CL-12
  Tab 6 🏭 Multi-Queue Engine  → CL-11, CL-12, CL-13

For detailed explanation of any CL item:
  → Refer to this document (Thesis_Modernization_Notes.md)
```

---

*Thesis_Modernization_Notes.md · Version 1.0 · June 2026*
*Covers Sessions 24-29 · All CL-1 to CL-13 consolidated*
*Corrections: 6 thesis ambiguities resolved*
*Future: Sessions 30-33 + Multi-domain templates*
