import os

import numpy as np
import pandas as pd


LOCAL_FILE = "applicants.csv"


def load_applicants_data():
	"""Load applicants from the local assignment folder."""
	script_dir = os.path.dirname(os.path.abspath(__file__))
	search_paths = [
		os.path.join(script_dir, LOCAL_FILE),
		os.path.join(os.path.dirname(script_dir), LOCAL_FILE),
	]

	for path in search_paths:
		if os.path.exists(path):
			return pd.read_csv(path)

	searched = "\n".join(search_paths)
	raise FileNotFoundError(
		f"{LOCAL_FILE} was not found. Checked these locations:\n{searched}"
	)


def build_report(scores):
	"""Return required statistics using NumPy."""
	return {
		"Mean": np.mean(scores),
		"Median": np.median(scores),
		"Standard Deviation": np.std(scores),
		"Variance": np.var(scores),
		"1st Percentile": np.percentile(scores, 1),
		"5th Percentile": np.percentile(scores, 5),
		"10th Percentile": np.percentile(scores, 10),
	}


def print_report(df):
	scores = df["SAT Score"].to_numpy()
	report = build_report(scores)

	print("\n=== College Applicant SAT Score Analysis ===")
	print(f"Total Applicants: {len(df)}")
	print("\nSummary Statistics")
	print("-" * 50)
	for label, value in report.items():
		print(f"{label:<22}: {value:>8.2f}")


def list_by_percentile(df):
	# Percentile rank where higher SAT score means higher percentile.
	df = df.copy()
	df["Percentile Rank"] = df["SAT Score"].rank(method="average", pct=True) * 100

	while True:
		response = input(
			"\nEnter minimum percentile to list applicants (0-100), or Q to quit: "
		).strip()

		if response.lower() == "q":
			print("Exiting percentile listing.")
			break

		try:
			min_percentile = float(response)
			if min_percentile < 0 or min_percentile > 100:
				print("Please enter a value between 0 and 100.")
				continue
		except ValueError:
			print("Invalid input. Enter a number from 0 to 100, or Q.")
			continue

		filtered = df[df["Percentile Rank"] <= min_percentile].sort_values(
			by=["SAT Score", "Last Name", "First Name"],
			ascending=[True, True, True],
		)

		if filtered.empty:
			print(f"No applicants found at or below the {min_percentile:.2f}th percentile.")
			continue

		print(
			f"\nApplicants at or below the {min_percentile:.2f}th percentile "
			f"({len(filtered)} found):"
		)
		print("-" * 78)
		print(f"{'SAT Score':>9}  {'Last Name':<15} {'First Name':<15} {'Percentile':>10}")
		print("-" * 78)

		for _, row in filtered.iterrows():
			print(
				f"{int(row['SAT Score']):>9}  "
				f"{row['Last Name']:<15} "
				f"{row['First Name']:<15} "
				f"{row['Percentile Rank']:>9.2f}%"
			)


def main():
	try:
		df = load_applicants_data()
	except Exception as exc:
		print(f"Could not load applicant data: {exc}")
		return

	required_cols = {"First Name", "Last Name", "SAT Score"}
	missing_cols = required_cols - set(df.columns)
	if missing_cols:
		print(f"Missing required columns: {', '.join(sorted(missing_cols))}")
		return

	df["SAT Score"] = pd.to_numeric(df["SAT Score"], errors="coerce")
	df = df.dropna(subset=["SAT Score"])

	if df.empty:
		print("No valid SAT scores found in the dataset.")
		return

	print_report(df)
	list_by_percentile(df)


if __name__ == "__main__":
	main()
