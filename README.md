# Python Log Analyzer

A simple Python project that analyzes log files and generates a summary.

## Features

- Counts INFO messages
- Counts WARNING messages
- Counts ERROR messages
- Lists all error messages
- Saves report to summary.txt

## Project Structure

```
python-log-analyzer/
├── log_analyzer.py
├── sample.log
├── summary.txt
├── requirements.txt
└── README.md
```

## Run

```bash
python log_analyzer.py
```

## Sample Output

```
========================================
LOG ANALYSIS REPORT
========================================

INFO : 4
WARNING : 2
ERROR : 3

Error Messages

- Failed to connect to Redis
- Authentication failed
- Database timeout

Summary saved to summary.txt
```