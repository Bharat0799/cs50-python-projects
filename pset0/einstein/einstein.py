SPEED_OF_LIGHT = 300_000_000

def main():
    mass = int(input("Mass (kg): "))
    energy = mass * SPEED_OF_LIGHT ** 2
    print(f"{energy}")


if __name__ == "__main__":
    main()
