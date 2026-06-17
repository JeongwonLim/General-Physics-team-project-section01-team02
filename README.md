# General-Physics-team-project-section01-team02

<div align="center">

# 🛰️ High-Speed Escape from a Circular Orbit

**Pedagogical Breakdown and Numerical Verification of Orbital Maneuvers**

<p>
<a href="https://www.python.org"><img src="https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white"></a>
<img src="https://img.shields.io/badge/NumPy-Computational%20Analysis-4DABCF?logo=numpy&logoColor=white">
<img src="https://img.shields.io/badge/Matplotlib-Visualization-11557C">
<img src="https://img.shields.io/badge/LaTeX-Report-008080?logo=latex&logoColor=white">
</p>

*Team Yerin (Group 2) · DGIST General Physics I*

</div>

---

## 📝 Overview
본 프로젝트는 Philip R. Blanco와 Carl E. Mungan의 논문 **"High-speed escape from a circular orbit" (Am. J. Phys. 89, 72, 2021)**를 심층 분석하고 재구성한 연구입니다. 

기존의 복잡한 궤도 역학을 학부 수준의 물리학 원리(에너지 보존, 각운동량 보존)를 통해 풀어내고, **Direct Escape**, **Oberth Maneuver**, **Edelbaum Maneuver** 세 가지 전략의 연료 효율성($\Delta v$)을 수치적으로 검증하였습니다.

## 📊 Key Findings
- **Oberth 효과 검증**: 중력장 깊은 곳에서의 임펄스 적용이 최종 운동 에너지를 극대화함을 확인했습니다.
- **데이터 기반 의사결정**: 분석 결과, 탈출 속도($v_{\infty}/v_{0}$)에 따라 최적의 전략이 달라지는 명확한 경계값($\approx 0.61, 1.34$)을 도출했습니다.
- **Edelbaum의 우위**: 매우 높은 탈출 속도 영역에서는 Edelbaum 기동이 가장 효율적인 연료 경제성을 보임을 시각화했습니다.

<div align="center">
<p><i>Figure: $\Delta v$ 효율성 비교 및 연료 절감(Fuel Savings) 분석</i></p>
</div>

## 📂 Repository Structure
