# Create a function on display all different combination of three different digits in ascending order,
# listed by ascending order - yes, repetition is voluntary.

def print_comb():
    number = ''
    flag = False

    for i in range(10):
        for k in range(i+1, 10):
            for l in range(k+1, 10):
                number = str(i) + str(k) + str(l)
                if flag:
                    print(', ' + number, end = "")
                else:
                    print(number, end = '')
                    flag = True


if __name__ == "__main__":
    print_comb()