# IN501_Raj_Unit3_Assignment.py

# 1) Square: 5 lines of 10 asterisks
for _ in range(5):
    print("*" * 10)
print()

# 2) Triangle
for row in range(5):
    stars = 2 * row + 1
    print(" " * (4 - row) + "*" * stars)
print()

# 3) Capital letter A
star_counts = {0: 3, 1: 5, 4: 11, 5: 13}
middle_spaces_map = {2: 3, 3: 5, 6: 11, 7: 13, 8: 15}

for row in range(9):
    leading_spaces = 8 - row
    if row in star_counts:
        print(" " * leading_spaces + "*" * star_counts[row])
    else:
        print(" " * leading_spaces + "**" + " " * middle_spaces_map[row] + "**")