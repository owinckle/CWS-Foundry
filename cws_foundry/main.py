import pandas as pd
import numpy as np
import requests

SHEET_ID = "1cgxhu1fPK-VuuQPApwVWyM1e1mWdSXWvLPaeZvC9PZs"
sheet_url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv&gid=0"

# Load sheet data starting from row 2 (header=1)
df = pd.read_csv(sheet_url, header=1)
df = df.replace({np.nan: None})

headers = df.columns.tolist()

data_dicts = []
for row in df.values.tolist():
    row_dict = dict(zip(headers, row))
    if not row_dict.get("ID"):  # Stop if no ID in this row
        break
    data_dicts.append(row_dict)

print(f"Loaded {len(data_dicts)} rows from the sheet")

# Example: Update Status field for ID "1.0"
webhook_url = "https://script.google.com/macros/s/AKfycbw29moWDjYUYy3r3d3LaJHEJnuJd5Rn2Oe_4T0dyM7OVfav6Mrp2r_Ggfg-Gg0ksfiU/exec"

payload = {
    "ID": "1.0",
    "Status": "Thinking"
}

try:
    response = requests.post(webhook_url, json=payload)
    print("POST status code:", response.status_code)
    print("Response text:", response.text)
    try:
        print("Response JSON:", response.json())
    except Exception:
        print("Response is not JSON format")
except Exception as e:
    print("Request failed:", e)
