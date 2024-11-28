

# PHBS QPS 2024 - US CPI Inflation Analysis

## Repository URL
[GitHub Repository URL](https://github.com/williamLong-lgtm/phbs-qps-2024/blob/main)

## Setup and Running Instructions

### 1. Clone the repository:
Clone the repository to your local machine.

```bash
git clone https://github.com/williamLong-lgtm/phbs-qps-2024/tree/main
cd phbs-qps-2024
```

### 2. Set up a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  
# On Windows, use venv\Scripts\activate
```
### 3.Install Dependencies:
Make sure you have Python 3 and pip installed. Then, install the necessary dependencies using pip:
```bash
pip install pandas pandas_datareader
```

### 4. Run the script to fetch and calculate the last 4 quarters of inflation:
```bash
python scripts/fetch_cpi_data.py
```