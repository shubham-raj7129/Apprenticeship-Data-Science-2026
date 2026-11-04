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
subprocess.run("python3 IN404_Unit7_1_Solution.py & python3 IN404_Unit7_2_Solution.py", shell=True)
