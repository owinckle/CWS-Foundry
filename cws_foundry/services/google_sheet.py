import pandas as pd
import numpy as np
import requests

from config.settings import Settings

# SHEET_ID = "1cgxhu1fPK-VuuQPApwVWyM1e1mWdSXWvLPaeZvC9PZs"
# sheet_url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv&gid=0"

# # Load sheet data starting from row 2 (header=1)
# df = pd.read_csv(sheet_url, header=1)
# df = df.replace({np.nan: None})

# headers = df.columns.tolist()

# data_dicts = []
# for row in df.values.tolist():
#     row_dict = dict(zip(headers, row))
#     if not row_dict.get("ID"):  # Stop if no ID in this row
#         break
#     data_dicts.append(row_dict)

# print(f"Loaded {len(data_dicts)} rows from the sheet")

# # Example: Update Status field for ID "1.0"
# webhook_url = "https://script.google.com/macros/s/AKfycbw29moWDjYUYy3r3d3LaJHEJnuJd5Rn2Oe_4T0dyM7OVfav6Mrp2r_Ggfg-Gg0ksfiU/exec"

# payload = {
#     "ID": "1.0",
#     "Status": "Thinking"
# }

# try:
#     response = requests.post(webhook_url, json=payload)
#     print("POST status code:", response.status_code)
#     print("Response text:", response.text)
#     try:
#         print("Response JSON:", response.json())
#     except Exception:
#         print("Response is not JSON format")
# except Exception as e:
#     print("Request failed:", e)


WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbw29moWDjYUYy3r3d3LaJHEJnuJd5Rn2Oe_4T0dyM7OVfav6Mrp2r_Ggfg-Gg0ksfiU/exec"
SPREADSHEET_URL = f"https://docs.google.com/spreadsheets/d/{Settings.GS_SPREADSHEET_ID}/export?format=csv&gid=0"


class GSM:
    def __init__(self):
        self.tasks = []

    """Fetch the data from the sheet"""
    def fetch(self):
        # Load sheet data starting from row 2 (header=1)
        df = pd.read_csv(SPREADSHEET_URL, header=1)
        df = df.replace({np.nan: None})
        
        # Map the headers
        headers = df.columns.tolist()

        # Retrieve the rows
        data_dicts = []
        for row in df.values.tolist():
            row_dict = dict(zip(headers, row))
            if not row_dict.get("ID"): # Stop if no ID in this row
                break
            data_dicts.append(row_dict)

        self.tasks = data_dicts

    """Find the next task and return it"""
    def get_next_task(self):
        next_task = None

        for task in self.tasks[::-1]:
            status = task["Status"]
            if status == "Ready to publish":
                next_task = task
            elif status == "Ready":
                next_task = task
        
        return next_task

    """Update a specific task, given an ID"""
    def update_task(self, payload):
        if not payload["ID"]:
            return False # No ID wa passed, failed request

        try:
            response = requests.post(WEBHOOK_URL, json=payload)
            print("POST status code:", response.status_code)
            print("Response text:", response.text)
            try:
                print("Response JSON:", response.json())
            except Exception:
                print("Response is not JSON format")
        except Exception as e:
            print("Request failed:", e)