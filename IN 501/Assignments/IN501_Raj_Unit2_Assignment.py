# Project Hours Lookup Program

projects = {
    "101": ("Website Redesign", {
        "Alice": 25, "Bob": 40, "Charlie": 30, "Diana": 35, "Eve": 20
    }),
    "102": ("Mobile App Development", {
        "Alice": 15, "Frank": 50, "Grace": 40, "Bob": 20, "Hank": 45
    }),
    "103": ("Marketing Campaign", {
        "Diana": 20, "Ivy": 35, "Charlie": 15, "Eve": 25, "Grace": 30
    }),
    "104": ("Data Analysis", {
        "Hank": 50, "Frank": 35, "Ivy": 40, "Bob": 25, "Charlie": 20
    }),
    "105": ("Product Launch", {
        "Alice": 30, "Diana": 25, "Eve": 40, "Grace": 20, "Hank": 35
    }),
}

project_number = input("Enter a project number: ").strip()
employee_name = input("Enter the employee's name: ").strip().capitalize()

if project_number not in projects:
    print("That is not a valid project number.")
else:
    project_name, employees = projects[project_number]
    if employee_name not in employees:
        print(f"{employee_name} is not listed on project {project_number}, {project_name}.")
    else:
        hours = employees[employee_name]
        print(f"{employee_name} has worked {hours} hours on project {project_number}, {project_name}.")