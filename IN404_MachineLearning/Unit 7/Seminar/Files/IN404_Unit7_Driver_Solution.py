import subprocess

#Run the subprocess.run command with the two file path and names
#   python3 IN404_Unit7_1.py & python3 IN404_Unit7_2.py.
#
#   As well as shell=True

# Easiest if the files are all in the same directory or folder

#For a student
#subprocess.run("python3 IN404_Unit7_1.py & python3 IN404_Unit7_2.py", shell=True)

#For the instructor
#Watch the directory path. Easier to put in the same directory as shown below
#subprocess.run("python3 IN404_Unit7_1_Solution.py & python3 IN404_Unit7_2_Solution.py", shell=True)

#On POSIX shells a single & backgrounds the first program, so the driver only
# waits for the second one and never sees the first one's exit status.
#&& runs them one after the other and stops at the first failure; the return
# code is passed back so a failed run is not reported as success.
import sys
from pathlib import Path

PYTHON = f'"{sys.executable}"'
result = subprocess.run(
    f"{PYTHON} IN404_Unit7_1_Solution.py && {PYTHON} IN404_Unit7_2_Solution.py",
    shell=True, cwd=Path(__file__).resolve().parent)

if result.returncode != 0:
    print(f"Driver: a program failed (exit status {result.returncode}).",
          file=sys.stderr)
sys.exit(result.returncode)
