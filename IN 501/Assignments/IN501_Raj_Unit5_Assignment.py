employees = [
    "Sarah Johnson", "Michael Brown", "Emily Wilson", "David White",
    "Jessica Walker", "James Anderson", "Olivia Taylor", "Daniel West",
    "Sophia Moore", "Christopher Wright", "Emma Lewis", "William Clark",
    "Ava Robinson", "Benjamin Williams", "Mia Hall", "Alexander Young",
    "Isabella Watson", "Ethan Wood", "Abigail Scott", "Jacob Green",
    "Chloe Adams", "Samuel Baker", "Lily Turner", "Henry Warren",
    "Grace Mitchell", "Elijah Campbell", "Zoe Parker", "Matthew Evans",
    "Hannah Collins", "Joshua Rivera"
]

customers = [
    "Alice Carter", "Brian Adams", "Charlotte Collins", "Dylan Brooks",
    "Eva Clark", "Franklin Hayes", "Grace Cooper", "Henry Bennett",
    "Isla Curtis", "Jack Miller", "Katherine Chapman", "Leo Harris",
    "Madeline Parker", "Noah Thompson", "Olivia Coleman", "Paul Stewart",
    "Quinn Foster", "Rachel King", "Samuel Curtis", "Tessa Bell",
    "Ulysses Scott", "Victoria Simmons", "Walter Chapman", "Xavier Foster",
    "Yara Lopez", "Zachary Carter", "Amelia Reed", "Brandon Price",
    "Cameron Myers", "Danielle Fisher"
]


def listSearch(nameList, char, index=0, results=None):
    if results is None:
        results = []

    if index >= len(nameList):
        return results

    lastName = nameList[index].split()[-1]
    if lastName[0].lower() == char.lower():
        results.append(nameList[index])

    return listSearch(nameList, char, index + 1, results)


def displayResults(results, listName, char):
    count = len(results)
    print(f"\nWe have found {count} {listName} whose last name begins with '{char.lower()}'.\n")

    results.sort(key=lambda name: name.split()[-1].lower())

    for person in results:
        print(person)


def main():
    print("Enter the number of the list you want to search.\n")
    print("1 for Employees")
    print("2 for Customers\n")
    choice = input("> ")

    if choice == "1":
        selectedList = employees
        listName = "Employees"
    elif choice == "2":
        selectedList = customers
        listName = "Customers"
    else:
        print("Invalid choice.")
        return

    char = input("\nEnter the letter you would like to use in the search. > ")

    if len(char) != 1 or not char.isalpha():
        print("Please enter a single letter.")
        return

    results = listSearch(selectedList, char)
    displayResults(results, listName, char)


main()
