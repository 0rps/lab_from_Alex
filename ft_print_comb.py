# Create a function on display all different combination of three different digits in ascending order,
# listed by ascending order - yes, repetition is voluntary.

def print_comb():
    result = []
    number = ''
    for i in range(10):
        for k in range(i+1, 10):
            for l in range(k+1, 10):
                number = str(i) + str(k) + str(l)
                if len(result) == 0:
                    result.append(number)
                else:
                    j = 0
                    flag = False
                    while j < len(result):
                        number_j = result[j]
                        if str(i) in number_j and str(k) in number_j and str(l) in number_j:
                            flag = True
                            break
                        j += 1
                    if flag == False:
                        result.append(number)

    for i in range(len(result)):
        if i == len(result)-1:
            print(result[i])
        else:
            print(result[i], end=', ')


if __name__ == "__main__":
    print_comb()