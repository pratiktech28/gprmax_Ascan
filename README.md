[![A-scan Validation CI](https://github.com/pratiktech28/gprmax_Ascan/actions/workflows/main.yml/badge.svg)](https://github.com/pratiktech28/gprmax_Ascan/actions/workflows/main.yml)
![download](https://github.com/user-attachments/assets/e4cb7568-886e-4caf-a1a7-79e89849cfd0)
![download](https://github.com/user-attachments/assets/671e69ad-19c1-4e87-95a1-345359280c7f)
**⚡ ASCN: Asynchronous Scalable Computing Node for gprMax**
**🎯 Overview**
ASCN is the core execution engine of the Trident Pipeline. It handles heavy-duty gprMax physics simulations asynchronously, ensuring high availability and fault-tolerant processing. By decoupling task submission from execution, ASCN allows the system to scale horizontally across distributed cloud nodes._
---
**🏗️ Technical Architecture**
The ASCN node operates as a high-performance worker that consumes simulation tasks from a distributed message broker.

**🔌 Key Components:**
Task Broker (RabbitMQ): Orchestrates asynchronous message passing between the CI/CD pipeline and the worker nodes.
In-Memory Cache (Redis): Manages transient task states, ensuring real-time monitoring of simulation progress.
Data Persistence (PostgreSQL): Stores detailed metadata and regression results for long-term analysis.
Workflow Engine (Airflow): Schedules and monitors the end-to-end simulation DAGs.


<img width="300" height="300" alt="ascan_comparison" src="https://github.com/user-attachments/assets/a3a55861-d91a-4cd1-9b19-04206214d11f" />


**🛠️ The "Asynchronous" Logic**
Producer: The Trident CI pipeline (GitHub Actions) pushes a simulation job into the Simulation_Queue.
Consumer (ASCN Worker): Multiple Dockerized workers listen to the queue.
Execution: An available worker pulls the job, runs the gprMax solver in an isolated container, and streams logs.
Validation: Results are pushed to the validation engine, and the task status is updated in Redis/Postgres.
---
📈 Scalability (10x to 100x)
ASCN is designed for Elastic Scaling. Using Kubernetes HPA, the number of ASCN worker nodes automatically increases based on the number of pending messages in RabbitMQ, allowing for massive parallelization of electromagnetic wave simulations.

**🚀 Deployment**
Local Development (Docker)
Bash
# Build and run the ASCN worker environment
docker-compose up --build
Environment Variables
Ensure you have the following configured:

RABBITMQ_URL: Connection string for the message broker.

REDIS_HOST: Tracking server address.

DB_CONNECTION: Postgres link for regression metadata.

**👨‍💻 Author**
**Prateek Sharma** GSoC '26 Applicant | Cloud-Native Infrastructure Engineer
