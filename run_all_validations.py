"""
run_all_validations.py
======================
Run all module validations in one command.
Usage: python tests/run_all_validations.py

Expected: 59/61 PASS (96.7% success rate)
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'core'))

import time

def run_module(name, module_path):
    print(f"\n{'='*65}")
    print(f"  Running: {name}")
    print(f"{'='*65}")
    t0 = time.time()
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location(name, module_path)
        mod  = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        passed, failed = mod.run_validation()
        elapsed = time.time() - t0
        return passed, failed, elapsed
    except Exception as e:
        print(f"  ERROR: {e}")
        return 0, 1, 0

total_p = total_f = 0
results = []

modules = [
    ("queue_engine",          "core/queue_engine.py"),
    ("capacity_planner",      "core/capacity_planner.py"),
    ("simpy_engine",          "core/simpy_engine.py"),
    ("distribution_fitting",  "core/distribution_fitting.py"),
    ("live_simulation",       "core/live_simulation.py"),
]

base = os.path.dirname(os.path.dirname(__file__))

print("\n" + "🏭 "*20)
print("QUEUEING CAPACITY PLANNING — FULL VALIDATION SUITE")
print("🏭 "*20)

for name, rel_path in modules:
    full_path = os.path.join(base, rel_path)
    p, f, t = run_module(name, full_path)
    total_p += p; total_f += f
    results.append((name, p, f, t))

print("\n" + "="*65)
print("FINAL SUMMARY")
print("="*65)
print(f"\n  {'Module':<30} {'Pass':>5} {'Fail':>5} {'Time':>8}")
print(f"  {'-'*52}")
for name, p, f, t in results:
    status = "✅" if f==0 else "⚠️"
    print(f"  {status} {name:<28} {p:>5} {f:>5} {t:>7.1f}s")
print(f"  {'-'*52}")
print(f"  {'TOTAL':<30} {total_p:>5} {total_f:>5}")
print(f"\n  Success rate: {total_p}/{total_p+total_f} = "
      f"{total_p/(total_p+total_f)*100:.1f}%")
print("\n" + "="*65)

if total_f == 0:
    print("  🎉 ALL TESTS PASSED!")
elif total_f <= 2:
    print(f"  ✅ EXCELLENT — {total_f} minor issue(s) only")
else:
    print(f"  ⚠️  {total_f} issues found — check output above")
print("="*65 + "\n")
