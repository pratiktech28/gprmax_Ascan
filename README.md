<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ASCN Architecture | Trident Pipeline</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; max-width: 900px; margin: auto; padding: 20px; background-color: #f4f7f6; }
        .header { background: #24292e; color: white; padding: 20px; text-align: center; border-radius: 8px; }
        .section { background: white; padding: 20px; margin-top: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        h2 { color: #0366d6; border-bottom: 2px solid #eaecef; padding-bottom: 10px; }
        table { width: 100%; border-collapse: collapse; margin: 20px 0; }
        th, td { border: 1px solid #dfe2e5; padding: 12px; text-align: left; }
        th { background-color: #f6f8fa; }
        .img-container { text-align: center; margin: 20px 0; }
        .img-container img { max-width: 100%; border-radius: 5px; border: 1px solid #ddd; box-shadow: 0 4px 8px rgba(0,0,0,0.2); }
        .badge { background: #28a745; color: white; padding: 5px 10px; border-radius: 20px; font-size: 0.8em; }
    </style>
</head>
<body>

    <div class="header">
        <h1>🔱 ASCN: Asynchronous Scalable Computing Node</h1>
        <p>Architecting Physics-Based Regression at Scale | GSoC 2026</p>
    </div>

    <div class="section">
        <h2>🚀 Project Overview</h2>
        <p>The <strong>ASCN (Asynchronous Scalable Computing Node)</strong> is a critical component of the Trident Pipeline. It leverages a distributed architecture to handle high-intensity <strong>gprMax</strong> simulations without blocking the main CI/CD workflow.</p>
        
        <div class="img-container">
            <img src="ascan_logic_flow.png" alt="ASCN Architecture Flow">
            <p><em>Figure 1: High-Level ASCN Logic & Task Queue Flow</em></p>
        </div>
    </div>

    <div class="section">
        <h2>📊 A-scan Comparison & Validation</h2>
        <p>Automation is meaningless without precision. ASCN performs real-time A-scan comparison to ensure that every simulation matches the "Golden Truth" metadata stored in our SQL database.</p>
        
        <div class="img-container">
            <img src="ascan_comparison.png" alt="A-scan Comparison Graph">
            <p><em>Figure 2: Physics-Based Validation (Simulated vs. Reference Data)</em></p>
        </div>

        <table>
            <thead>
                <tr>
                    <th>Component</th>
                    <th>Technology Stack</th>
                    <th>Role in Trident Pipeline</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Message Broker</td>
                    <td><strong>RabbitMQ</strong></td>
                    <td>Decoupling task submission from execution.</td>
                </tr>
                <tr>
                    <td>Task Scheduling</td>
                    <td><strong>Apache Airflow</strong></td>
                    <td>Managing complex simulation DAGs.</td>
                </tr>
                <tr>
                    <td>State Management</td>
                    <td><strong>Redis</strong></td>
                    <td>Real-time tracking of node health & task status.</td>
                </tr>
                <tr>
                    <td>Elastic Scaling</td>
                    <td><strong>Kubernetes HPA</strong></td>
                    <td>Dynamic scaling from 10x to 100x nodes.</td>
                </tr>
            </tbody>
        </table>
    </div>

    <div class="section">
        <h2>🛠️ Core Technical Logic</h2>
        <p>By implementing an asynchronous model, we eliminate system timeouts and resource starvation. The system is designed for <strong>high-throughput</strong> processing of electromagnetic wave models, ensuring 100% reliability for researchers worldwide.</p>
    </div>

    <footer style="text-align: center; margin-top: 40px; font-size: 0.9em; color: #666;">
        <p>Developed by <strong>Prateek Sharma</strong> | GSoC '26 Applicant @gprMax</p>
    </footer>

</body>
</html>
