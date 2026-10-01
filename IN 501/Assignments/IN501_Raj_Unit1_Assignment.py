def f_to_c(f):
    """Formula for Fahrenheit to Celsius conversion."""
    return (f - 32) * 5 / 9


def main():
    # Read three integer Fahrenheit temperatures
    f_temps = []
    for i in range(1, 4):
        while True:
            try:
                value = int(input(f"Enter Fahrenheit temperature #{i}: "))
                f_temps.append(value)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

    # Convert to Celsius
    c_temps = [f_to_c(f) for f in f_temps]

    # Compute averages
    avg_f = sum(f_temps) / len(f_temps)
    avg_c = sum(c_temps) / len(c_temps)

    # Output formatting
    print("\nFahrenheit | Celsius")
    # print("-" * 20)

    for f, c in zip(f_temps, c_temps):
        print(f"{f}  | {c:.1f}")

    print("-" * 20)
    print(f"{avg_f:.0f}  | {avg_c:.1f} Average")


if __name__ == "__main__":
    main()