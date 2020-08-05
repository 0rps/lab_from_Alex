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
            data[i - 1] = calculate(float(data[i - 1]), data[i], float(data[i + 1]))
            del data[i]
            del data[i]
        else:
            i += 2

    while 1 < len(data):
        data[0] = calculate(float(data[0]), data[1], float(data[2]))
        del data[1]
        del data[1]

    return data[0]


def eval_expr(data):
    operators = "+-*/%"
    i, start, finish, count = 0, 0, 0, 0
    if data[0] == "-":
        data[0] = data[0] + data[1]
        del data[1]
    while i < len(data):
        if not is_number(data[i]) and data[i] not in operators:
            if data[i][0] == "(":
                position_brackets = 0
                if count == 0:
                    start = i
                    data[i] = data[i][1:]
                    count += 1
                while True:
                    if data[i][position_brackets] == "(":
                        count += 1
                        position_brackets += 1
                        continue
                    break

            elif data[i][-1] == ")":
                position_brackets = 1
                while True:
                    if data[i][len(data[i])-position_brackets] == ")":
                        count -= 1
                        position_brackets += 1
                        continue
                    break
                if count == 0:
                    finish = i
                    data[i] = data[i][:len(data[i]) - 1]
                    
            if count == 0 and finish != 0:
                data[start] = eval_expr(data[start:finish+1])
                k = len(data[start:finish])
                i -= k
                while k > 0:
                    del data[start + 1]
                    k -= 1
        i += 1

    if len(data) == 1:
        return data[0]
    return calculate_result(data)


def main():
    while True:
        data = input("Enter arithmetic expression: ").split()
        if len(data) == 0:
            print("Error. Empty line. Try again.")
            continue
        break
    print(eval_expr(data))


if __name__ == "__main__":
    main()
