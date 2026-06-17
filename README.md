# General-Physics-team-project-section01-team02

<div align="center">

# High-Speed Escape from a Circular Orbit

**Pedagogical Breakdown and Numerical Verification of Orbital Maneuvers**

Team Yerin (Group 2)

</div>

---

## 1. Overview
This project is an in-depth analysis and reconstruction of Philip R. Blanco and Carl E. Mungan's papers **"High-speed escapes from a circular orbit" (AJP, 89, 72, 2021)**.

Existing complex orbital dynamics are solved through undergraduate-level physics principles (energy conservation, angular momentum conservation) and the fuel efficiency ($\Delta v$) of the three strategies **Direct Escape**, **Oberth Maneuver** and **Edelbaum Maneuver** have been numerically validated.

## 2. Key Findings
- **OBERTH EFFECT VERIFY **: IMPULSE APPLICATION DEEP IN GRAVITY FIELD MAXIMIZES FINAL kinetic energy.
- **Data-driven decision**: As a result of our analysis, we have derived a clear boundary value ($\prox 0.61, $1.34), where the optimal strategy depends on the escape rate ($v_{\infty}/v_{2}$).
- **Edelbaum's edge**: In the area of very high escape velocity, we have visualized that Edelbaum manoeuvres show the most efficient fuel economy.

<div align="center">
<p><i>Figure: $\Delta v$ efficiency comparison and fuel saving analysis</i></p>
</div>

## 3. Repository Structure
orbital-escape-project/
├-- data/# numerical analysis data
├── src/
│   ├-- analysis.py # $\Delta v$ Calculation and Numerical Simulation
│   └-- plotting.py # Create a paper-style graph
├-- report/# Project Final Report (PDF)
└── README.md

## 4. Team Members
| Name | Role |
| :--- | :--- |
| **Yerin Kwon** | Derivations & Mathematical Layout |
| **Junghae Kim** | Physical Approximations |
| **Jieun Yu** | Critical Analysis & Commentary |
| **Jeongwon Lim** | Contextual Background & Computational Modeling |

## 5. Reference
Blanco, P. R., & Mungan, C. E. (2021). "High-speed escape from a circular orbit." *American Journal of Physics*, 89, 72.
