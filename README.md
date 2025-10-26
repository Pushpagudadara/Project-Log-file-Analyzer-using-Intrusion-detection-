# Project-Log-file-Analyzer-using-Intrusion-detection-
This project helps to detect suspicious activities from server log files using Python. 

🗂️ Repository Structure

Repository name:
log-file-analyzer

Folder layout:

log-file-analyzer/
│
├── README.md
├── log_analyzer.py
├── requirements.txt
├── sample_logs/
│   ├── apache_access.log
│   ├── ssh_logs.log
│
├── output/
│   ├── suspicious_ips.csv
│   ├── incident_report.txt
│   └── visualization.png
│
└── report/
    └── Internship_Project_Report.pdf


---

📝 README.md

# 🕵️‍♂️ Log File Analyzer for Intrusion Detection

## 🎯 Objective
Build a Python tool to detect suspicious or malicious patterns in log files (Apache, SSH, etc.) and visualize security incidents.

---

## 🧰 Tools & Libraries
- Python  
- regex (for pattern matching)  
- pandas (for data analysis)  
- matplotlib (for visualization)

---

## 🧠 Features
1. Parse and analyze Apache and SSH logs.  
2. Detect brute-force, scanning, and DoS patterns.  
3. Visualize access frequency and anomalies (by IP and time).  
4. Cross-reference IPs against public blacklists.  
5. Export suspicious IPs and incident reports.  

---

## ⚙️ Steps Involved
1. **Read log files:** Load `.log` data using Python and parse lines with regex.  
2. **Pattern detection:** Identify repeated login failures, DoS attempts, or suspicious requests.  
3. **Visualization:** Use matplotlib to generate frequency/time-based graphs.  
4. **Blacklist comparison:** Match identified IPs with known malicious IPs.  
5. **Export:** Save flagged results as `.csv` or `.txt` reports.

---

## 📄 Sample Output

[INFO] Log File Loaded: apache_access.log [INFO] Total Entries: 3521 [ALERT] Suspicious IPs detected: 7 [EXPORT] Report saved to: output/incident_report.txt

---

## 📦 Installation
```bash
pip install pandas matplotlib


---

▶️ Run the Analyzer

python log_analyzer.py --input sample_logs/apache_access.log

(Optional: visualize patterns)

python log_analyzer.py --visualize


---

🧩 Deliverables

A Python tool that:

Processes server logs

Flags brute-force and scanning attempts

Visualizes attack frequency

Exports incident summaries



---

📚 Internship Report

Full report available at:
report/Internship_Project_Report.pdf


---

✨ Author

PUSHPA
Elevate Labs Internship Project – Phase 1

---
