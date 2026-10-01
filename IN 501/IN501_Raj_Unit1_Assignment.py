def f_to_c(f):
    """Formula for Fahrenheit to Celsius conversion."""
    return (f - 32) * 5 / 9


def main():
    # Read three integer Fahrenheit temperatures
    f_temps = []
    for i in range(1, 4):
                value = int(input(f"Enter Fahrenheit temperature #{i}: "))
                f_temps.append(value)

    # Convert to Celsius
    c_temps = [f_to_c(f) for f in f_temps]

    # Compute averages
    avg_f = sum(f_temps) / len(f_temps)
    avg_c = sum(c_temps) / len(c_temps)

    # Output formatting
    print("\nFahrenheit | Celsius")
    print("-" * 32)

    for f, c in zip(f_temps, c_temps):
        print(f"{f:9d}  | {c:6.1f}")

    print("-" * 22)
    print(f"{avg_f:9.0f}  | {avg_c:6.1f} Average")


if __name__ == "__main__":
    main()