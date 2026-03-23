# 🔱 ASCN: Asynchronous Scalable Computing Node

<div align="center">
  <img src="https://img.shields.io/badge/GSoC-2026-orange?style=for-the-badge&logo=google" />
  <img src="https://img.shields.io/badge/RabbitMQ-FF6600?style=for-the-badge&logo=rabbitmq&logoColor=white" />
  <img src="https://img.shields.io/badge/Kubernetes-326ce5?style=for-the-badge&logo=kubernetes&logoColor=white" />
</div>

---

## 🚀 Project Overview
The **ASCN (Asynchronous Scalable Computing Node)** is the core engine of the Trident Pipeline. It leverages a distributed architecture to handle high-intensity **gprMax** simulations asynchronously.

### 🏗️ Technical Architecture flow
<div align="center">
  <img src="image_5ab864.png" width="800px" alt="ASCN Logic Flow">
  <p><i>Figure 1: High-Level ASCN Logic & Task Queue Flow</i></p>
</div>

---

## 📊 A-scan Comparison & Validation
Automation is meaningless without precision. ASCN performs real-time A-scan comparison to ensure every simulation matches the **"Golden Truth"** metadata.

<div align="center">
  <img src="ascan_comparison.png" width="700px" alt="A-scan Comparison Graph">
  <p><i>Figure 2: Physics-Based Validation (Simulated vs. Reference Data)</i></p>
</div>

---

## 🛠️ Tech Stack & Role
| Component | Technology | Role in Trident Pipeline |
| :--- | :--- | :--- |
| **Message Broker** | `RabbitMQ` | Decoupling task submission from execution. |
| **State Management** | `Redis` | Real-time tracking of node health & task status. |
| **Task Scheduling** | `Airflow` | Managing complex simulation DAGs. |
| **Elastic Scaling** | `K8s HPA` | Dynamic scaling from 10x to 100x nodes. |

---

## ⚡ Core Technical Logic
By implementing an **Asynchronous Model**, we eliminate system timeouts and resource starvation. The system is designed for **high-throughput** processing, ensuring 100% reliability for researchers worldwide.

<p align="center">
  <b>Developed by Prateek Sharma | GSoC '26 Applicant @gprMax</b>
</p>
