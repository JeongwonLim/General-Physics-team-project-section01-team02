import numpy as np
import matplotlib.pyplot as plt

v_inf = np.linspace(0.0, 3.0, 500)
r_in = 0.05
r_out = 2.5  

dv_direct = np.sqrt(2 + v_inf**2) - 1
dv_oberth = 1 + np.sqrt(v_inf**2 + 2 / r_in) - np.sqrt(2 + 2 / r_in)
dv_edelbaum = np.sqrt(v_inf**2 + 2 / r_in) + np.sqrt(2 + 2 / r_out) - np.sqrt(2 / r_in + 2 / r_out - 1)

savings_oberth = dv_direct - dv_oberth
savings_edelbaum = dv_direct - dv_edelbaum

# Savings = 0
idx_do = np.argwhere(np.diff(np.sign(savings_oberth))).flatten()
# Same Savings
savings_diff = dv_oberth - dv_edelbaum
idx_oe = np.argwhere(np.diff(np.sign(savings_diff))).flatten()

plt.figure(figsize=(10, 6))
plt.plot(v_inf, savings_oberth, 'purple', linestyle='--', linewidth=2.5, label='Savings: Oberth vs Direct')
plt.plot(v_inf, savings_edelbaum, 'b-.', linewidth=2.5, label='Savings: Edelbaum vs Direct')
plt.axhline(0, color='black', linewidth=1.5, linestyle='-')

# Crossover
if len(idx_do) > 0:
    v_cross_do = v_inf[idx_do[0]]
    plt.plot(v_cross_do, 0, 'ro', markersize=8, label=f'Direct-Oberth Crossover ($v_\infty \\approx {v_cross_do:.2f}$)')

if len(idx_oe) > 0:
    v_cross_oe = v_inf[idx_oe[0]]
    plt.plot(v_cross_oe, savings_oberth[idx_oe[0]], 'go', markersize=8, label=f'Oberth-Edelbaum Crossover ($v_\infty \\approx {v_cross_oe:.2f}$)')

plt.xlim(0.0, 3.0)
plt.xlabel(r'Final Speed at Infinity ($v_\infty / v_0$)', fontsize=14, fontweight='bold')
plt.ylabel(r'Fuel Savings ($\Delta v / v_0$)', fontsize=14, fontweight='bold')
plt.title('Figure 2: Fuel Savings and Crossover Regimes', fontsize=16, fontweight='bold', pad=15)
plt.legend(fontsize=12, loc='best')
plt.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()