from calculator.operations import add, subtract, multiply, divide


def repl():
    print("Welcome to the CLI Calculator")
    print("Type expressions like: 2 + 7 or type 'q' to quit")

    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    while True:
        user_input = input(">> ").strip()

        if user_input.lower() == "q":
            print("Goodbye!")
            break

        try:
            a, op, b = user_input.split()
            a = float(a)
            b = float(b)

            if op not in operations:
                print("Invalid operator.")
                continue

            result = operations[op](a, b)
            print(f"Result: {result}")

        except ValueError:
            print("Invalid format. Use: number operator number (e.g. 2 + 7)")
        except ZeroDivisionError as e:
            print(e)


# 🔴 THIS PART IS REQUIRED
if __name__ == "__main__":
    repl()
