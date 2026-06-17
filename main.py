import numpy as np
import matplotlib.pyplot as plt

# x axis: v_inf / v_0
v_inf = np.linspace(0.0, 3.0, 500)

# Given parameters
r_in = 0.05
r_out = 2.5  

# Delta v / v_0
# (a) - Direct Escape
dv_direct = np.sqrt(2 + v_inf**2) - 1

# (b) - Oberth Maneuver
dv_oberth = 1 + np.sqrt(v_inf**2 + 2 / r_in) - np.sqrt(2 + 2 / r_in)

# (c) - Edelbaum Maneuver
dv_edelbaum = np.sqrt(v_inf**2 + 2 / r_in) + np.sqrt(2 + 2 / r_out) - np.sqrt(2 / r_in + 2 / r_out - 1)

# (d) - No gravity
dv_nograv = v_inf - 1
dv_nograv[dv_nograv < 0] = np.nan # ignore when v_inf < v_0
plt.figure(figsize=(10, 7))

plt.plot(v_inf, dv_direct, 'g:', linewidth=2.5, label='Direct (Eq. 7)')
plt.plot(v_inf, dv_oberth, 'purple', linestyle='--', linewidth=2.5, label=r'Oberth ($r_{in}=0.05 r_0$)')
plt.plot(v_inf, dv_edelbaum, 'b-.', linewidth=2.5, label=r'Edelbaum ($r_{out}=2.5 r_0, r_{in}=0.05 r_0$)')
plt.plot(v_inf, dv_nograv, 'gray', linestyle=':', linewidth=2, label='No Gravity')

plt.xlim(0.0, 3.0)
plt.ylim(0.0, 2.3)
plt.xlabel(r'Final Speed at Infinity ($v_\infty / v_0$)', fontsize=14, fontweight='bold')
plt.ylabel(r'Total Required Speed Change ($\Delta v / v_0$)', fontsize=14, fontweight='bold')
plt.title('Figure 1: Delta-V Efficiency of Orbital Escape Strategies', fontsize=16, fontweight='bold', pad=15)
plt.legend(fontsize=12, loc='upper left')
plt.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()
