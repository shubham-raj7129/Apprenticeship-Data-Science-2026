import os
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))

# ── 1. Read both CSV files into separate dataframes ──
master_df = pd.read_csv(os.path.join(script_dir, "PigsFlyPolls.csv"))
update_df = pd.read_csv(os.path.join(script_dir, "PigsFlyPolls_update.csv"))

# ── 2. Print each dataframe ──
print("=== Master Polls ===")
print(master_df)
print("\n=== Update Polls ===")
print(update_df)

# ── 3. Merge updates into master (update existing, append new) ──
# Set Pollster as index on both so we can use update()
master_df = master_df.set_index("Pollster")
update_df = update_df.set_index("Pollster")

# update() overwrites matching rows in-place
master_df.update(update_df)
print("\n=== After update() – existing rows refreshed ===")
print(master_df)

# Find new pollsters that aren't in the master and append them
new_rows = update_df.loc[~update_df.index.isin(master_df.index)]
master_df = pd.concat([master_df, new_rows])
print("\n=== After appending new pollsters ===")
print(master_df)

# Reset index so Pollster is a regular column again
master_df = master_df.reset_index()

# ── 4. Print the updated master dataframe ──
print("\n=== Updated Master DataFrame ===")
print(master_df)

# ── 5. Sort alphabetically by Pollster ──
master_df = master_df.sort_values("Pollster").reset_index(drop=True)
print("\n=== Sorted Alphabetically ===")
print(master_df)

# ── 6. Write to CSV ──
master_df.to_csv(os.path.join(script_dir, "PigsFlyPolls2.csv"), index=False)
print("\nWritten to PigsFlyPolls2.csv")

# ── 7. Print datatypes (they are strings because of the % signs) ──
print("\n=== Data Types ===")
print(master_df.dtypes)

# ── 8. Convert percentage strings to numeric and compute averages ──
pct_cols = ["Yes", "No", "Undecided"]
for col in pct_cols:
    master_df[col] = master_df[col].str.replace("%", "").astype(float)

print("\n=== After converting to numeric ===")
print(master_df.dtypes)

averages = master_df[pct_cols].mean()
print("\n=== Averages ===")
print(averages)

# ── 9. Add averages as the last row ──
avg_row = pd.DataFrame([{"Pollster": "Average",
                          "Yes": averages["Yes"],
                          "No": averages["No"],
                          "Undecided": averages["Undecided"]}])
master_df = pd.concat([master_df, avg_row], ignore_index=True)

print("\n=== Final DataFrame with Averages ===")
print(master_df)

# ── 10. Write to Excel ──
master_df.to_excel(os.path.join(script_dir, "PigsFlyPolls.xlsx"), index=False)
print("\nWritten to PigsFlyPolls.xlsx")
