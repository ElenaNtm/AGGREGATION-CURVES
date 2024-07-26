# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 10:57:31 2024

@author: Eleni
"""

"""
Libraries
"""

import requests
from datetime import datetime, timedelta
import os

"""
Scrapping Aggregation curves
For automated downloading of DAM aggregated curves file report use the following URL:
https://www.enexgroup.gr/documents/20126/200034/YYYYMMDD_EL-DAM_AggrCurves_EN_v##.xlsx
"""


base_url = "https://www.enexgroup.gr/documents/20126/200034/{date}_EL-DAM_AggrCurves_EN_v{version:02d}.xlsx"
save_directory = r"C:\Users\Eleni\OneDrive - Hellenic Association for Energy Economics (1)\GEARS TASKS\Market Prices Data\EnexGroup&Historical\Aggregation curves"

# Ensure the save directory exists
os.makedirs(save_directory, exist_ok=True)

# Function to download and save the file
def download_file(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded and saved: {save_path}")
        return True
    except requests.RequestException as e:
        print(f"Failed to download: {url} with error: {e}")
        return False

# Iterate through each day of 2024
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 7, 25)
current_date = start_date

while current_date <= end_date:
    date_str = current_date.strftime("%Y%m%d")
    save_path = os.path.join(save_directory, f"{date_str}_EL-DAM_AggrCurves_EN.xlsx")
    
    # Check if the file already exists
    if os.path.exists(save_path):
        print(f"File already exists: {save_path}")
    else:
        # Try versions from 01 to 05
        file_saved = False
        for version in range(1, 6):
            url = base_url.format(date=date_str, version=version)
            if download_file(url, save_path):
                file_saved = True
                break
        
        if not file_saved:
            print(f"No valid file found for date: {date_str}")
    
    current_date += timedelta(days=1)



