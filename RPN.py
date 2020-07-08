def is_number(str):    # check the number
    try:
        float(str)
        return True
    except ValueError:
        return False

def math_operation(operand_1, operand_2, operator):  # perform a math operation
    if operator == "+":
        return operand_1 + operand_2
    elif operator == "-":
        return operand_1 - operand_2
    elif operator == "*":
        return operand_1 * operand_2
    elif operator == "/":
        return operand_1 / operand_2
    elif operator == "%":
        return operand_1 % operand_2


def main():
    data = input("Enter expression to calculate. ").split()
    if len(data) > 2:
        operators = "+-/%*"
        i = 2
        while i < len(data):
            if data[i] in operators:
                if is_number(data[i-1]) and is_number(data[i-2]):   # check the number
                    data[i-2] = str(math_operation(float(data[i-2]), float(data[i-1]), data[i]))  # rewrite the operand_1
                    del data[i-1]    # delete operand_2
                    del data[i-1]    # delete operation
                    i -= 1
                else:
                    print('Error. Not a number.')
                    return
            else:
                i += 1

        if len(data) > 1:
            print('Error. The number of operators and operands does not match.')
        else:
            print(f"Result: {round(float(data[0]),2)}")

    else:
        print("Error. Low data.")


if __name__ == "__main__":
    main()