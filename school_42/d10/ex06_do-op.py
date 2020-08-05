# Create a program called do-op.
# The program will be executed with three arguments: do-op, value1, operateur, value2.
# The operator character corresponds to the appropriate function within an array of pointers to function.
# Your directory should contain a Makefile with the all and clean rules.
# If the case of an invalid argument such as, the program 0.
# If the number of arguments is invalid, doesn't display anything.


def is_number(symbol):
    try:
        int(symbol)
        return True
    except ValueError:
        return False


def number(v):
    i = 0
    while i < len(v):
        if is_number(v[i]) or (i == 0 and v[i] == "-"):
            i += 1
        elif i == 0 and not is_number(v[i]):
            return 0
        elif v[i-1] == "-" and not is_number(v[i]):
            return 0
        else:
            return int(v[:i])
    return int(v)


def subtraction(v1, v2):
    return v1-v2


def addition(v1, v2):
    return v1+v2


def multiplication(v1, v2):
    return v1*v2


def division(v1, v2):
    return v1/v2


def do_op(v1, op, v2):
    operators = {"-": subtraction,
                 "+": addition,
                 "*": multiplication,
                 "/": division}

    if op in operators:
        v1 = number(v1)
        v2 = number(v2)
        if v2 == 0 and op == "/":
            return "Stop: modulo by zero!"
        else:
            return operators[op](v1, v2)
    else:
        return 0


def main():
    while True:
        try:
            value1, operator, value2 = input("Enter 3 arguments separated by space: value1 operatuer value2. ").split()
        except ValueError:
            print("Error. Try again.")
            continue
        break

    print(do_op(value1, operator, value2))


if __name__ == "__main__":
    main()
