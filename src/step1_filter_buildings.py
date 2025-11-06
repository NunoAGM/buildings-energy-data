# -*- coding: utf-8 -*-
"""
STEP 1 — Filter buildings with PV and EV charger

User action REQUIRED:
---------------------
➡️ Download the CSV (upgradeXX.csv) from NREL/ResStock Results Viewer
➡️ Update the path below with the location of your file

Output:
    filtered_buildings.csv
"""

import pandas as pd
from pathlib import Path

# ✅ CHANGE THIS TO THE PATH WHERE YOUR CSV IS SAVED
csv_path = Path("C:/Users/User/Downloads/upgrade28.csv/upgrade28.csv")

data = pd.read_csv(csv_path)

# Select only relevant columns
has_pv = data[[
    "bldg_id", "in.has_pv",
    "in.county_name", "in.county_and_puma",
    "in.electric_vehicle_charger"
]]

# Filter buildings that have PV
pv = has_pv[has_pv["in.has_pv"] == "Yes"]

# Filter buildings that have EV charger
ev = pv[pv["in.electric_vehicle_charger"] != "None"]

# Save filtered buildings for step 2
output_file = Path.cwd() / "filtered_buildings.csv"
ev.to_csv(output_file, index=False)

print(f"✅ Buildings filtered successfully.")
print(f"📄 Output saved to: {output_file}")
