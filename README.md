# 🏭 Queueing-Oriented Capacity Planning System

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?logo=streamlit)](https://streamlit.io)
[![SimPy](https://img.shields.io/badge/SimPy-DES%20Engine-green)](https://simpy.readthedocs.io)
[![SciPy](https://img.shields.io/badge/SciPy-Statistical%20Fitting-orange)](https://scipy.org)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

> **Modernizing a 1999 M.Sc. Thesis into a Professional Digital Twin Platform**
>
> *"A Queueing-Oriented Decision Process for Capacity Planning in a Job Shop Environment"*
>
> *Ain Shams University · Faculty of Engineering · Cairo, Egypt · 1999*

---

## 🎯 Project Overview

This project transforms a **1999 M.Sc. thesis** in Industrial Engineering into a
**fully interactive, modern decision-support and simulation platform**.

What began as a static analytical study using queueing theory has been rebuilt
from the ground up using Python, SimPy, Streamlit, and Plotly — turning
25-year-old mathematical models into a **live digital twin** of a manufacturing
job shop, now generalized beyond the original 3-stage case study to support
any number of stages, any number of products, and real economic patience
(reneging) behavior grounded in the thesis's own equations.

### The Journey: 1999 → 2026

```
1999 (Original Thesis)              2026 (This Platform)
─────────────────────               ────────────────────────────────
📄 20 pages + hand calculations  →  💻 7 Python modules (6,900+ lines)
📊 Static tables & charts        →  📊 10-tab interactive dashboard
🔢 M/M/S analytical formulas     →  🔴 Real-time SimPy simulation
🏭 Fixed 3-stage case study      →  🔧 Configurable N-stage / M-queue engine
📋 Paper document                →  🎬 Animated factory floor (per-job tracking)
```

### 💬 The Real Story

> *"I wrote this thesis at Ain Shams University in 1999 as part of my M.Sc. in*
> *Mechanical Engineering. Twenty-five years later, I decided to rebuild it —*
> *not for any degree or obligation — but because I believed the work deserved*
> *to live again in modern form.*
>
> *I rebuilt everything from scratch: the mathematics, the simulation engine,*
> *the economic optimization model, and the interactive dashboard.*
>
> *This is what happens when an engineer refuses to let good work stay on a shelf."*
>
> — **Eng. Mohammed Mohammed Sayed Mohammed**, Cairo 2026

---

## ✨ Key Features

### 📊 10-Tab Interactive Dashboard

| Tab | Feature | Description |
|-----|---------|-------------|
| 1 | 📊 Queue Analysis | 20 single-server models (M/M/1, M/G/1, M/D/1, M/Ek/1...) |
| 2 | 💰 Capacity Planning | Optimal server count S* via Eqs 3.8-3.10 |
| 3 | 📅 Monthly Schedule | Priority loading, shift selection, Exhaustive vs Gated |
| 4 | 🔬 Case Study | Fixed 6-product / 3-stage reference — the original thesis case study, kept unchanged as a baseline |
| 5 | 🔗 Series Queues | Jackson Network — per-stage bottleneck analysis |
| 6 | 🏭 Multi-Queue Engine | **MAIN ENGINE** — N products × configurable M stages × S servers |
| 7 | 🔴 Live Simulation | SimPy DES with real-time machine status, reneging, per-stage shifts |
| 8 | 📊 Statistical Reports | Scenario comparison, patience/T sensitivity, CSV export |
| 9 | 🔧 Input & Fit | 4-step data pipeline: demand → λ → μ → model, feeds Tabs 1-8/10 |
| 10 | 🎬 Animation | Live-animated factory floor — exact per-job tracking, not aggregate approximation |

### 🔧 Configurable N-Stage / M-Queue Engine

Originally hardcoded to exactly 3 stages (matching the thesis's Sheet Metal
Dept. case study), the engine now generalizes to **any number of stages**,
with **editable stage names** — so the same validated math can model a
different department (e.g. Mechanical Workshop, Cupper Workshop) just by
reconfiguring stage count, names, and server counts, without touching code.
Tabs 6, 7, 8, and 10 all support this; **Tab 4 is deliberately kept fixed**
as the original thesis's unchanging reference case.

### ⏱️ Finite-Patience Reneging (Eq 3.8)

The DES engine now implements genuine finite-patience behavior: a job that
waits longer than a configurable patience time `T` at any stage abandons
the queue, matching the thesis's own `λ**` (effective arrival rate) formula
instead of assuming customers wait forever. This closes a real structural
gap between the original analytical model and the simulation engine.

### 🎬 Animated Factory Floor (Digital Twin)

Plotly-based live animation of the job shop, built directly on the SimPy
DES engine — jobs are tracked with **exact per-job identity** (not a
statistical approximation), colored by product, moving through
configurable stages with live queue-length and waiting-time readouts.

### 🔗 Global Product Source

Tab 9's distribution-fitting pipeline (Poisson/Exponential/Gamma/Erlang-k)
can feed its fitted product parameters directly into Tabs 1-8 and 10 via a
shared toggle — including part-level Erlang-k service-time fitting, which
correctly models a product's total processing time as the sum of many
small part operations (low-variance, near-deterministic) rather than a
single high-variance Exponential draw.

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    dashboard.py (10 tabs)                       │
│    Streamlit + Plotly Interactive Web Application                │
└──────────┬──────────────────────┬───────────────────┬───────────┘
           │                      │                   │
┌──────────▼──────────┐  ┌────────▼────────────┐ ┌────▼─────────────┐
│   ANALYTICAL ENGINE  │  │   SIMULATION ENGINE  │ │  ANIMATION ENGINE │
│                      │  │                      │ │                   │
│  queue_engine.py     │  │  simpy_engine.py     │ │ animation_engine  │
│  ├─ Stage 1 (20 mdl) │  │  ├─ Layer 1: M/M/S   │ │  .py              │
│  ├─ Stage 2 (Jackson)│  │  ├─ Layer 2: Series  │ │  ├─ Per-job         │
│  ├─ Stage 3 (Multi-Q)│  │  └─ Layer 3: Job Shop│ │  │  identity tracking│
│  └─ MEkS_approx      │  │                      │ │  └─ N-stage layout │
│     (multi-server     │  │  live_simulation.py  │ │                   │
│      Erlang-k)        │  │  ├─ Reneging (Eq 3.8)│ └───────────────────┘
│                      │  │  ├─ N-stage generic   │
│  capacity_planner.py │  │  ├─ Erlang-k service  │
│  ├─ Eq 3.8: λ**      │  │  ├─ Machine status    │
│  ├─ Eq 3.9: Rs**     │  │  └─ Experiment runner │
│  └─ Eq 3.10: Rn(S)   │  │                      │
└──────────────────────┘  └──────────────────────┘
           │
┌──────────▼──────────────────────────────────────────────────────┐
│                    INPUT LAYER                                   │
│              distribution_fitting.py                            │
│  Step 1: Demand → λ  │  Step 2: Service → μ (+ part-level k)   │
│  Step 3: Cost → NR    │  Step 4: Fit + Export (Global Product   │
│                        │           Source, feeds all tabs)      │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📐 Mathematical Foundation

### Core Queueing Equations (Eqs 3.1–3.7)

$$\rho = \frac{\lambda}{S \cdot \mu}, \quad
L_q = \frac{a \cdot \rho^S \cdot P_0}{(S-1)!(1-\rho)^2}, \quad
W_q = \frac{L_q}{\lambda}$$

### Capacity Planning Equations (Eqs 3.8–3.10)

$$\lambda^{**} = \frac{2T(S\mu)^2}{1 + 2TS\mu} \quad \text{(Eq 3.8 — now also the basis for DES reneging)}$$

$$R_s^{**} = \lambda_{int} \times SP \quad \text{(Eq 3.9)}$$

$$R_n = \lambda_{int} \times NR(S), \quad NR(S) = \frac{NR_{base}}{S} \quad \text{(Eq 3.10)}$$

### Service Policies (Eqs 3.11–3.12)

| Policy | Mechanism | Effect |
|--------|-----------|--------|
| **Exhaustive** | Serve until queue empty | Higher throughput |
| **Gated** | Serve only queued at poll start | **65-97% E[L] reduction** ✓ |

---

## 🔬 Case Study — Job Shop (6 Products × 3 Stages)

Tab 4 keeps this exact configuration fixed as the thesis's original reference
case — every other N-stage-capable tab defaults to it too, but can be
reconfigured away from it.

| Product | μ [u/hr] | λ [u/hr] | ρ | NR [$/u] |
|---------|---------|---------|---|----------|
| 8BD | 80 | 2 | 0.025 | $9,000 |
| 8BK | 120 | 4 | 0.033 | $11,000 |
| 8FJ500 | 80 | 6 | 0.075 | $5,000 |
| 8AS10 | 16 | 4 | 0.250 | $3,000 |
| 3CF12KVA | 8 | 2 | 0.250 | $600 |
| **G.T3** | **6** | **2** | **0.333** | **$1,600** |

> **G.T3 = System Bottleneck** (highest ρ = 0.333) ✓

**Factory configuration (CL-12 machine groups):**
```
Stage 1 — Cutting  machines (Group 1): S=5  → M/M/5
Stage 2 — Punching machines (Group 2): S=3  → M/M/3  ← Bottleneck
Stage 3 — Bending  machines (Group 3): S=5  → M/M/5
Stage ratios: [0.2 : 0.5 : 0.3] × total machining hours
```

Beyond this fixed reference case, the same engine also models other
departments per the factory's real machine-type table (e.g. Mechanical
Workshop: Turning/Milling/Grinding/Drilling; Cupper Workshop:
Cutting/Punching/Bending) as independent N-stage configurations.

---

## ✅ Validation Results

| Module | Tests | Result |
|--------|-------|--------|
| `queue_engine.py` | 21 tests | **19/21 PASS** |
| `capacity_planner.py` | 13 tests | **13/13 PASS** ✓ |
| `simpy_engine.py` | 6 tests | **6/6 PASS** ✓ |
| `distribution_fitting.py` | 17 tests | **17/17 PASS** ✓ |
| `live_simulation.py` | 4 tests | **4/4 PASS** ✓ |

**Key validations:**
- λ** (Table 22): **Exact match** for all 7 S values ✓
- SimPy vs Analytical: **< 3% deviation** ✓
- Bottleneck detection: **G.T3 confirmed** ✓
- Gated E[L] reduction: **67–97%** ✓
- N-stage generalization: **bit-identical** to the original 3-stage engine
  when N=3, verified against pre-generalization output on the same seed ✓
- Reneging (Eq 3.8): DES-measured effective arrival rate cross-checked
  against the analytical λ** formula, computed independently per stage ✓

---

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/mohamedsayed980/queueing-capacity-planning.git
cd queueing-capacity-planning

# Install dependencies
pip install -r requirements.txt
```

### Run the Dashboard

```bash
streamlit run dashboard.py
# Opens at http://localhost:8501
```

### Use as Python Library

```python
from queue_engine import run_model, MEkS_approx
from capacity_planner import optimize_S
from live_simulation import LiveSimulation, run_experiment

# Single queue analysis (any of 20 classic models)
result = run_model(model_id=2, lam=2.0, mu=9.23, S=3)
print(f"Lq={result['Lq']}, Wq={result['Wq']}, ρ={result['rho']}")

# Multi-server Erlang-k approximation (Allen-Cunneen)
erlang_result = MEkS_approx(lam=7, mu=9.23, S=3, k=10)
print(f"Wq(Erlang-10)={erlang_result['Wq']}")

# Optimize server count
opt = optimize_S(mu=9.23, SP=25000, NR_base=48.4, T=0.4)
print(f"Optimal S*={opt['S_opt']}, Max Rn={opt['Rn_max']:.2f}")

# Run experiment comparison — now with configurable stages, shifts-per-
# stage, and patience (T) as per-scenario overrides
scenarios = [
    {"name":"Baseline",     "S_stages":[5,3,5], "policy":"exhaustive"},
    {"name":"Add server",   "S_stages":[5,4,5], "policy":"exhaustive"},
    {"name":"Gated",        "S_stages":[5,3,5], "policy":"gated"},
    {"name":"More patient", "S_stages":[5,3,5], "renege_T":2.0},
    {"name":"4-stage config","S_stages":[5,3,5,2],
     "stage_ratios":[0.2,0.4,0.25,0.15],
     "stage_names":["Plate Shears","Punching","Bending","Welding"]},
]
from live_simulation import PRODUCTS_EXP
results = run_experiment(PRODUCTS_EXP, scenarios, sim_time=1000)
```

---

## 📁 Project Structure

```
queueing-capacity-planning/
│
├── dashboard.py                    # 10-tab Streamlit application
│
├── queue_engine.py                 # 20 queue models + MEkS_approx (Stages 1,2,3)
├── capacity_planner.py             # Economic optimization (Eqs 3.8-3.10)
├── simpy_engine.py                 # SimPy DES validation engine
├── distribution_fitting.py         # Input data pipeline (4 steps) + part-level Erlang-k
├── live_simulation.py              # DES engine: reneging, N-stage generic, experiment runner
├── animation_engine.py             # Animated factory floor (exact per-job tracking)
│
├── docs/
│   ├── Thesis_Modernization_Notes.md  # All clarifications CL-1→13
│   ├── architecture_diagram.md        # System architecture
│   └── validation_results.md          # Full validation report
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🛠️ Tech Stack

| Technology | Role | Version |
|-----------|------|---------|
| Python | Core language | 3.8+ |
| Streamlit | Web dashboard | Latest |
| Plotly | Interactive charts & animation | Latest |
| SimPy | Discrete-event simulation | 4.1.2 |
| SciPy | Distribution fitting | Latest |
| Pandas | Data manipulation | Latest |
| NumPy | Numerical computing | Latest |

---

## 🔮 Future Development Roadmap

```
Domain Templates (Planned):
  🏥 healthcare_template.py — Patient flow, doctor scheduling
  🚚 logistics_template.py  — Warehouse, shipping lanes
  ☎️  callcenter_template.py — Agent queues, customer service
  🏦 banking_template.py    — Transaction queues, teller scheduling

Sequential Batch Scheduling (Planned):
  📦 batch_sequencing_engine.py — Flow-shop-style sequential batch
                                   production (distinct from the
                                   current open-queueing-network model)

The SAME queueing engine powers all domains.
Only the domain parameters change.
```

---

## 📖 Academic Background

This project is based on the M.Sc. thesis:

> **"A Queueing-Oriented Decision Process for Capacity Planning
> in a Job Shop Environment"**
> M.Sc. thesis, Department of Mechanical Engineering, 1999

### Theoretical Foundation
- **M/M/S Queueing Theory** (Erlang-C formula)
- **Jackson Networks** (product-form solutions)
- **Polling Systems** (Exhaustive & Gated service)
- **Economic Optimization** (Net Revenue maximization)
- **Discrete-Event Simulation** (SimPy DES, with finite-patience reneging)

### Original Thesis
> Mohammed, M.M.S. (1999).
> **"A Queueing Oriented Decision Process for Capacity Planning
> in a Job Shop Environment"**.
> M.Sc. Thesis, Department of Mechanical Engineering (Production),
> Faculty of Engineering, Ain Shams University, Cairo, Egypt.
>
> Supervised by Prof. Amin K. ELkharbotly

### Key References
- Kleinrock, L. (1975). *Queueing Systems, Volume 1*
- Gross, D. & Harris, C. (1998). *Fundamentals of Queueing Theory*
- Takagi, H. (1991). *Vacation and Priority Systems*
- Banks, J. et al. (2001). *Discrete-Event System Simulation*

---

## 👤 Author

**Eng. Mohammed Mohammed Sayed Mohammed**

| | |
|--|--|
| 🎓 **Degree** | M.Sc. Mechanical Engineering (Production) |
| 🏛️ **University** | Ain Shams University, Faculty of Engineering, Cairo |
| 📅 **Original Thesis** | 1999 |
| 💻 **Platform Modernization** | 2026 |
| 👨‍🏫 **Thesis Supervisor** | Prof. Amin K. ELkharbotly |
| | Design & Production Engineering Dept., Ain Shams University |

> *"I wrote this thesis in 1999. 25 years later, I rebuilt it
> using modern Python, SimPy, and Streamlit — proving that
> good academic work never expires. It just needs modern tools to come alive."*

---

## 📄 License

This project is licensed under the MIT License.
See [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

Special thanks to the original thesis supervisors:
- **Prof. Amin K. ELkharbotly** — Design & Production Engineering Dept.
- **Dr. Nahed Sobhi Mohamed** — Design & Production Engineering Dept.
- **Dr. Mahmoud Abd El-Moemen Atalla** — Engineering Physics & Mathematics Dept.

*Faculty of Engineering, Ain Shams University, Cairo, Egypt (1999)*

---

Built 25 years later with the conviction that
**good academic work never expires — it just needs modern tools to come alive.**

> *"The equations were written in 1999. The platform is new. The insight endures."*

---

⭐ **If this project helped you, please give it a star!**

```
pip install streamlit plotly pandas simpy scipy
streamlit run dashboard.py
```
