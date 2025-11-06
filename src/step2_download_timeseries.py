# -*- coding: utf-8 -*-
"""
STEP 2 — Download Parquet time-series files from NREL OEDI

Requires:
    filtered_buildings.csv (generated in STEP 1)

Output:
    A folder with parquet files, one per building
"""

import pandas as pd
import requests
from pathlib import Path

# Load filtered buildings from STEP 1
ev = pd.read_csv("filtered_buildings.csv")
ev["state"] = None  # add column to track state found

# URL template for NREL endpoint
base_url = (
    "https://oedi-data-lake.s3.amazonaws.com/nrel-pds-building-stock/"
    "end-use-load-profiles-for-us-building-stock/2025/"
    "resstock_amy2018_release_1/timeseries_individual_buildings/by_state/"
    "upgrade%3D28/state%3D"
)

states = [
    "AK","AL","AR","AZ","CA","CO","CT","DC","DE","FL",
    "GA","HI","IA","ID","IL","IN","KS","KY","LA","MA",
    "MD","ME","MI","MN","MO","MS","MT","NC","ND","NE",
    "NH","NJ","NM","NV","NY","OH","OK","OR","PA","RI",
    "SC","SD","TN","TX","UT","VA","VT","WA","WI","WV"
]

# Folder where files will be saved
output_folder = Path("nrel_downloads")
output_folder.mkdir(exist_ok=True)

for bldg_id in ev["bldg_id"]:
    file_name = f"{bldg_id}-28.parquet"
    file_path = output_folder / file_name

    for state in states:
        url = f"{base_url}{state}/{file_name}"
        r = requests.get(url, stream=True)

        if r.status_code == 200:
            with open(file_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

            print(f"✅ Download completed: {file_name} (state: {state})")
            ev.loc[ev["bldg_id"] == bldg_id, "state"] = state
            break  # stop after finding correct state
