# -*- coding: utf-8 -*-
"""
STEP 3 — Export download metadata (optional)

Input:
    filtered_buildings.csv (modified during Step 2 if downloads were done)

Output:
    data_infos.xlsx
"""

import pandas as pd
from pathlib import Path

ev = pd.read_csv("filtered_buildings.csv")

output_path = Path("data_infos.xlsx")
ev.to_excel(output_path, index=False)

print(f"✅ Metadata exported to: {output_path}")
