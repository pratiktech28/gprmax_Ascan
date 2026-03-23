
[![A-scan Validation CI](https://github.com/pratiktech28/gprmax_Ascan/actions/workflows/main.yml/badge.svg)](https://github.com/pratiktech28/gprmax_Ascan/actions/workflows/main.yml)#  ASCN: Asynchronous Scalable Computing Node
### *Core Engine of the Trident Pipeline for gprMax*

<div align="center">
  <img src="https://img.shields.io/badge/GSoC-2026-orange?style=for-the-badge&logo=google" />
  <img src="https://img.shields.io/badge/Architecture-Distributed-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/NRMSE-0.0-brightgreen?style=for-the-badge" />
</div>

---

## 📖 Overview
**ASCN** (Asynchronous Scalable Computing Node) is a high-performance infrastructure designed to automate and scale **gprMax** physics simulations. By decoupling simulation requests from execution using a message-broker architecture, it ensures that the research workflow remains robust, scalable, and reproducible.

---

## 🏗️ Core Architectural Logic
The system is built on a **Producer-Consumer** model to eliminate bottlenecks in high-intensity electromagnetic wave modelling.

<div align="center">
  <img src="image_5ab864.png" width="850" alt="ASCN Flowchart">
  <p><i>Figure 1: Distributed Workflow using RabbitMQ, Redis, and Dockerized Workers.</i></p>
</div>

### 🛠️ The Tech Stack
* **Orchestration:** Kubernetes (K8s) with **HPA** for 10x to 100x elastic scaling.
* **Messaging:** **RabbitMQ** for fault-tolerant task queuing.
* **Storage:** **PostgreSQL** for metadata and **Redis** for real-time state tracking.
* **Environment:** **Docker** for bit-for-bit identical physics execution.

---

## 📉 Waveform Fidelity & A-scan Validation
We don't just scale; we validate. Every simulation undergoes a rigorous **Physics Regression** check.

<div align="center">
  <img src="ascan_comparison.png" width="800" alt="A-scan Comparison">
  <p><i>Figure 2: Perfect alignment between 'Current' and 'Golden Reference' waveforms.</i></p>
</div>

### 🎯 Key Performance Indicators (KPIs)
| Metric | Value | Logic |
| :--- | :--- | :--- |
| **NRMSE** | `0.0` | Zero numerical drift across containerized nodes. |
| **Signal Integrity** | `100%` | Verified via automated A-scan accuracy checks. |
| **Scaling Latency** | `Minimal` | Rapid pod spin-up via optimized Docker layers. |

---

## 🔄 The Trident Workflow
1.  **Ingestion:** Simulation parameters are pushed to the **RabbitMQ** queue.
2.  **Execution:** Available **ASCN Workers** pull tasks and run `gprMax` in isolated Docker containers.
3.  **Validation:** Results are compared against **SQL Golden Truth** benchmarks.
4.  **Reporting:** Automated **Matplotlib** plots are generated for visual verification.

---

<div align="center">
  <p><b>Developed by Prateek Sharma</b><br>
  <i>GSoC '26 Applicant | Cloud-Native Infrastructure Engineer</i></p>
</div>
