import subprocess

#Run the subprocess.run command with the two file path and names
#   python3 IN404_Unit7_1.py & python3 IN404_Unit7_2.py.
#
#   As well as shell=True

# Easiest if the files are all in the same directory or folder

import sys
from pathlib import Path

#Use the same Python interpreter that runs this driver, and run from this
# file's folder so both programs can find IN404_Reviews.csv.
#&& runs the programs one after the other so their output does not interleave.
PYTHON = f'"{sys.executable}"'
result = subprocess.run(f"{PYTHON} IN404_Unit7_1.py && {PYTHON} IN404_Unit7_2.py",
                        shell=True, cwd=Path(__file__).resolve().parent)

#If either program fails, report it and exit with the same non-zero status
# so the driver never looks successful after an incomplete run.
if result.returncode != 0:
    print(f"Driver: a program failed (exit status {result.returncode}).",
          file=sys.stderr)
sys.exit(result.returncode)
