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
job shop.

### The Journey: 1999 → 2026

```
1999 (Original Thesis)              2026 (This Platform)
─────────────────────               ────────────────────────────────
📄 20 pages + hand calculations  →  💻 6 Python modules (3,900+ lines)
📊 Static tables & charts        →  📊 9-tab interactive dashboard
🔢 M/M/S analytical formulas     →  🔴 Real-time SimPy simulation
🏭 Single case study             →  🔬 Experiment runner (∞ scenarios)
📋 Paper document                →  🌐 Professional web application
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

### 📊 9-Tab Interactive Dashboard

| Tab | Feature | Description |
|-----|---------|-------------|
| 1 | 📊 Queue Analysis | 20 single-server models (M/M/1, M/G/1, M/D/1, M/Ek/1...) |
| 2 | 💰 Capacity Planning | Optimal server count S* via Eqs 3.8-3.10 |
| 3 | 📅 Monthly Schedule | Priority loading, shift selection, Exhaustive vs Gated |
| 4 | 🔬 Case Study | 6-product job shop pre-loaded & ready |
| 5 | 🔗 Series Queues | Jackson Network — per-stage bottleneck analysis |
| 6 | 🏭 Multi-Queue Engine | **MAIN ENGINE** — N products × M stages × S servers |
| 7 | 🔴 Live Simulation | SimPy DES with real-time machine status |
| 8 | 📊 Statistical Reports | Scenario comparison + CSV export |
| 9 | 🔧 Input & Fit | 4-step data pipeline: demand → λ → μ → model |

### 🏗️ 3-Stage Analytical Engine

```
Stage 1: Single-Server Survey      Stage 2: Multi-Server          Stage 3: Main Engine
────────────────────────────       ──────────────────────          ─────────────────────
M/M/1   M/M/S   M/G/1              Series (Jackson)               N queues × M stages
M/D/1   M/Ek/1  M/Gamma/1          Parallel servers               S servers per stage
M/M/∞   M/M/S/K Priority           Bottleneck detection           Exhaustive policy
M/H₂/1  G/G/1   ...                Per-stage Wq, Ws, Lq           Gated policy
```

### 🔴 Live Simulation (Digital Twin)

```
[Job arrives] → [Stage 1: Cutting S=5] → [Stage 2: Punching S=3] → [Stage 3: Bending S=5]
                      ████░                    ███ ⚠️BUSY                  ████░
                   4/5 busy                 3/3 busy!                  4/5 busy
                   Queue: 2                 Queue: 8 ← BOTTLENECK      Queue: 0
```

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    dashboard.py (9 tabs)                        │
│    Streamlit + Plotly Interactive Web Application               │
└──────────┬──────────────────────────────────────┬──────────────┘
           │                                      │
┌──────────▼──────────┐              ┌────────────▼────────────┐
│   ANALYTICAL ENGINE  │              │   SIMULATION ENGINE     │
│                      │              │                         │
│  queue_engine.py     │              │  simpy_engine.py        │
│  ├─ Stage 1 (20 mdl) │              │  ├─ Layer 1: M/M/S      │
│  ├─ Stage 2 (Jackson)│              │  ├─ Layer 2: Series      │
│  └─ Stage 3 (Multi-Q)│              │  └─ Layer 3: Job Shop    │
│                      │              │                         │
│  capacity_planner.py │              │  live_simulation.py     │
│  ├─ Eq 3.8: λ**      │              │  ├─ Machine status       │
│  ├─ Eq 3.9: Rs**     │              │  ├─ KPI snapshots        │
│  └─ Eq 3.10: Rn(S)   │              │  └─ Experiment runner    │
└──────────────────────┘              └─────────────────────────┘
           │
┌──────────▼──────────────────────────────────────────────────────┐
│                    INPUT LAYER                                   │
│              distribution_fitting.py                            │
│  Step 1: Demand → λ  │  Step 2: Service → μ  │  Step 3: Cost   │
│  Step 4: Fit (Poisson/Exp/Gamma/Erlang) + Export               │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📐 Mathematical Foundation

### Core Queueing Equations (Eqs 3.1–3.7)

$$\rho = \frac{\lambda}{S \cdot \mu}, \quad
L_q = \frac{a \cdot \rho^S \cdot P_0}{(S-1)!(1-\rho)^2}, \quad
W_q = \frac{L_q}{\lambda}$$

### Capacity Planning Equations (Eqs 3.8–3.10)

$$\lambda^{**} = \frac{2T(S\mu)^2}{1 + 2TS\mu} \quad \text{(Eq 3.8)}$$

$$R_s^{**} = \lambda_{int} \times SP \quad \text{(Eq 3.9)}$$

$$R_n = \lambda_{int} \times NR(S), \quad NR(S) = \frac{NR_{base}}{S} \quad \text{(Eq 3.10)}$$

### Service Policies (Eqs 3.11–3.12)

| Policy | Mechanism | Effect |
|--------|-----------|--------|
| **Exhaustive** | Serve until queue empty | Higher throughput |
| **Gated** | Serve only queued at poll start | **65-97% E[L] reduction** ✓ |

---

## 🔬 Case Study — Job Shop (6 Products × 3 Stages)

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

---

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/queueing-capacity-planning.git
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
from core.queue_engine import run_model
from core.capacity_planner import optimize_S
from core.live_simulation import LiveSimulation, run_experiment

# Single queue analysis
result = run_model(model_id=2, lam=2.0, mu=9.23, S=3)
print(f"Lq={result['Lq']}, Wq={result['Wq']}, ρ={result['rho']}")

# Optimize server count
opt = optimize_S(mu=9.23, SP=25000, NR_base=48.4, T=0.4)
print(f"Optimal S*={opt['S_opt']}, Max Rn={opt['Rn_max']:.2f}")

# Run experiment comparison
scenarios = [
    {"name":"Baseline",    "S_stages":[5,3,5], "policy":"exhaustive"},
    {"name":"Add server",  "S_stages":[5,4,5], "policy":"exhaustive"},
    {"name":"Gated",       "S_stages":[5,3,5], "policy":"gated"},
]
from core.live_simulation import PRODUCTS_EXP
results = run_experiment(PRODUCTS_EXP, scenarios, sim_time=1000)
```

---

## 📁 Project Structure

```
queueing-capacity-planning/
│
├── dashboard.py                    # 9-tab Streamlit application
│
├── core/
│   ├── queue_engine.py             # 20 queue models (Stages 1,2,3)
│   ├── capacity_planner.py         # Economic optimization (Eqs 3.8-3.10)
│   ├── simpy_engine.py             # SimPy DES validation engine
│   ├── distribution_fitting.py     # Input data pipeline (4 steps)
│   └── live_simulation.py          # Live KPI engine + experiment runner
│
├── docs/
│   ├── Thesis_Modernization_Notes.md  # All clarifications CL-1→13
│   ├── architecture_diagram.md        # System architecture
│   └── validation_results.md          # Full validation report
│
├── tests/
│   └── run_all_validations.py      # Run all module tests
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
| Plotly | Interactive charts | Latest |
| SimPy | Discrete-event simulation | 4.1.2 |
| SciPy | Distribution fitting | Latest |
| Pandas | Data manipulation | Latest |
| NumPy | Numerical computing | Latest |

---

## 🔮 Future Development Roadmap

```
Phase 3 (Planned):
  🎬 animation_engine.py    — Plotly animated factory floor
                              (jobs moving stage1→stage2→stage3)

Domain Templates (Planned):
  🏥 healthcare_template.py — Patient flow, doctor scheduling
  🚚 logistics_template.py  — Warehouse, shipping lanes
  ☎️  callcenter_template.py — Agent queues, customer service
  🏦 banking_template.py    — Transaction queues, teller scheduling

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
- **Discrete-Event Simulation** (SimPy DES)

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
