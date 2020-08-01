def is_number(number):
    try:
        float(number)
        return True
    except ValueError:
        return False


def calculate(arg1, op, arg2):
    if op == "+":
        return arg1 + arg2
    elif op == "-":
        return arg1 - arg2
    elif op == "/":
        return arg1 / arg2
    elif op == "%":
        return arg1 % arg2
    elif op == "*":
        return arg1 * arg2


def calculate_result(data):
    operators_priority = "*/%"
    i = 1
    while i < len(data):
        if data[i] in operators_priority:
            data[i - 1] = str(calculate(float(data[i - 1]), data[i], float(data[i + 1])))
            del data[i]
            del data[i]
        else:
            i += 2

    while 1 < len(data):
        data[0] = str(calculate(float(data[0]), data[1], float(data[2])))
        del data[1]
        del data[1]

    return data[0]


def eval_expr(data):
    operators = "+-*/%"
    i, start, finish, count = 0, 0, 0, 0
    flag = False
    while i < len(data):
        if not is_number(data[i]) and data[i] not in operators:
            if data[i][0] == "(":
                if count == 0:
                    start = i
                    data[i] = data[i][1:]
                count += 1
                flag = True
            elif data[i][-1] == ")":
                count -= 1
                if count == 0:
                    finish = i
                    data[i] = data[i][:len(data[i])-1]
            if count == 0 and flag:
                data[start] = eval_expr(data[start:finish+1])
                k = len(data[start:finish])
                while k > 0:
                    del data[start + 1]
                    k -= 1
        i += 1

    if not flag:
        return calculate_result(data)
    elif len(data) == 1:
        return data
    else:
        return calculate_result(data)


def main():
    while True:
        data = input("Enter arithmetic expression: ").split()     # test 1 * 5 / 2 + (21 % 6 * 3 + 100 - (5 * 3 / 5 * 3 + 41) - 2) + 2
        if len(data) == 0:
            print("Error. Empty line. Try again.")
            continue
        break
    print(eval_expr(data))


if __name__ == "__main__":
    main()
