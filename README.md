<h2>Overview</h2>
<p>This program is a <strong>Site Reliability Engineering (SRE) health checker</strong> that monitors the availability of specified HTTP endpoints. It:</p>
<ul>
    <li>Reads a list of endpoints from a YAML configuration file.</li>
    <li>Sends periodic health check requests.</li>
    <li>Logs results to a file and console.</li>
    <li>Tracks <strong>long-term availability trends</strong>.</li>
    <li><strong>Visualizes uptime trends</strong> in a dynamically updated graph.</li>
    <li><strong>Sends email alerts</strong> when availability drops below a threshold.</li>
</ul>

<h2>Features</h2>
<ul>
    <li>✅ <strong>Asynchronous HTTP health checks</strong> (fast & non-blocking)</li>
    <li>✅ <strong>Tracks uptime percentages</strong> over time</li>
    <li>✅ <strong>Saves structured reports</strong> in CSV & JSON format</li>
    <li>✅ <strong>Auto-generates visual graphs</strong> for availability trends</li>
    <li>✅ <strong>Logs detailed results</strong> in the <code>logs/</code> directory</li>
</ul>

<h2>📂 Project Structure</h2>
<pre>
FetchHealthCheck/
│── health_checker/           # Core logic
│   │── init.py│   │── checker.py            # Main health checker script
│── tests/                    # Unit tests
│── config/                   # Configuration files
│   │── sample_config.yaml    # Example YAML configuration
│── logs/                     # Generated reports & logs
│── visualize_trends.py       # Graph generation script
│── requirements.txt          # Dependencies
│── README.md                 # Documentation
│── run.py                    # Entry point script

<h2>🛠️ Setup & Installation</h2>
<h3>1️⃣ Install Dependencies</h3>
<p>Ensure you have Python 3.8+ installed. Then run:</p>
<pre><code>pip install -r requirements.txt</code></pre>

<h3>2️⃣ Configure Endpoints</h3>
<p>Create a <strong>YAML configuration file</strong> (or use <code>config/sample_config.yaml</code>):</p>
<pre><code>- name: Fetch Index Page
<h2>🚀 Running the Program</h2>
<h3>1️⃣ Start the Health Checker</h3>
<p>Run the script to begin monitoring:</p>
<pre><code>python run.py config/sample_config.yaml --interval 15</code></pre>
<p><strong>Expected behavior:</strong></p>
<ul>
    <li>Console logs <strong>real-time status updates</strong>.</li>
    <li><strong>Logs are saved</strong> in <code>logs/health_checker.log</code>.</li>
    <li><strong>Alerts trigger</strong> if availability drops below 80%.</li>
    <li><strong>Data is stored</strong> in <code>logs/availability_report.csv</code> & <code>.json</code>.</li>
    <li><strong>A graph is generated</strong> (<code>logs/availability_trends.png</code>).</li>
</ul>

<h2>📊 Viewing Reports & Graphs</h2>
<h3>1️⃣ Check the Logs</h3>
<pre><code>cat logs/health_checker.log</code></pre>
<h3>2️⃣ Open Availability Reports</h3>
<pre><code>cat logs/availability_report.csv

<h2>🚀 Future Enhancements</h2>
<ul>
    <li>🔜 **Add Slack alerts** for failures</li>
    <li>🔜 **Enhance web dashboard monitoring**</li>
    <li>🔜 **Support API-based alert integrations**</li>
</ul>
