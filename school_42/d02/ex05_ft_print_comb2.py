# Create a function that displays all different combination of two digits between 00 and 99, listed by ascending order.

def print_comb():
    all_numbers = []
    number = ''
    for i in range(10):
        for j in range(10):
            number = str(i) + str(j)
            all_numbers.append(number)

    flag = False
    for i in range(len(all_numbers)-1):
        for j in range(i+1, len(all_numbers)):
            if flag:
                print(", " + all_numbers[i] + " " + all_numbers[j], end = "")
            else:
                print(all_numbers[i] + " " + all_numbers[j], end="")
                flag = True


if __name__ == "__main__":
    print_comb()