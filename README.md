# PythonHealthCheck

Fetch Health Checker
====================

Overview
--------

This program is a **Site Reliability Engineering (SRE) health checker** that monitors the availability of specified HTTP endpoints. It:

*   Reads a list of endpoints from a YAML configuration file.
    
*   Sends periodic health check requests.
    
*   Logs results to a file and console.
    
*   Tracks **long-term availability trends**.
    
*   **Visualizes uptime trends** in a dynamically updated graph.
    
*   **Sends email alerts** when availability drops below a threshold.
    

Features
--------

✅ **Asynchronous HTTP health checks** (fast & non-blocking)✅ **Tracks uptime percentages** over time✅ **Saves structured reports** in CSV & JSON format✅ **Auto-generates visual graphs** for availability trends✅ **Sends email alerts** for critical failures✅ **Logs detailed results** in the logs/ directory

📂 Project Structure
--------------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   FetchHealthCheck/  │── health_checker/           # Core logic  │   │── __init__.py             │   │── checker.py            # Main health checker script  │── tests/                    # Unit tests  │── config/                   # Configuration files  │   │── sample_config.yaml    # Example YAML configuration  │── logs/                     # Generated reports & logs  │── visualize_trends.py       # Graph generation script  │── requirements.txt          # Dependencies  │── README.md                 # Documentation  │── run.py                    # Entry point script   `

🛠️ Setup & Installation
------------------------

### **1️⃣ Install Dependencies**

Ensure you have Python 3.8+ installed. Then run:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pip install -r requirements.txt   `

### **2️⃣ Configure Endpoints**

Create a **YAML configuration file** (or use config/sample\_config.yaml):

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   - name: Fetch Index Page    url: https://fetch.com/    method: GET    headers:      user-agent: Mozilla/5.0  - name: Fetch Careers Page    url: https://fetch.com/careers    method: GET    headers:      user-agent: fetch-synthetic-monitor   `

🚀 Running the Program
----------------------

### **1️⃣ Start the Health Checker**

Run the script to begin monitoring:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python run.py config/sample_config.yaml --interval 15   `

Expected behavior:

*   Console logs **real-time status updates**.
    
*   **Logs are saved** in logs/health\_checker.log.
    
*   **Alerts trigger** if availability drops below 80%.
    
*   **Data is stored** in logs/availability\_report.csv & .json.
    
*   **A graph is generated** (logs/availability\_trends.png).
    

📊 Viewing Reports & Graphs
---------------------------

### **1️⃣ Check the Logs**

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   cat logs/health_checker.log   `

### **2️⃣ Open Availability Reports**

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   cat logs/availability_report.csv  cat logs/availability_report.json   `

### **3️⃣ View the Uptime Trends Graph**

Run:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python visualize_trends.py   `

Expected outcome:

*   **Graph appears showing uptime trends**.
    
*   **Red markers** highlight low availability (< 80%).
    
*   **Graph is saved as logs/availability\_trends.png**.
    

🛠️ Customization
-----------------

### **Adjusting Alert Threshold**

Modify checker.py:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   ALERT_THRESHOLD = 85.0  # Change threshold from 80% to 85%   `

### **Changing Health Check Interval**

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python run.py config/sample_config.yaml --interval 30  # Check every 30 seconds   `

🚀 Future Enhancements
----------------------

*   **Add Slack alerts** for failures
    
*   **Enhance web dashboard monitoring**
    
*   **Support API-based alert integrations**