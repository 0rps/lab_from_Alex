# Create a function that displays all different combination of N numbers by ascending order.
# 0 < n < 10

def print_comb():
    while True:
        try:
            n = int(input("Enter the number. "))
            if n < 0 or n > 10:
                print("0 < n < 10")
                continue
            break
        except:
            print("Error. There must be a number. Try again.")

    result = []
    number = ''
    i = 0

    while len(number) < n:
        number += str(i)
        i += 1

    result.append(number)

    pos = 0
    while pos < len(number):
        previous_number = int(number[-1-pos])
        if previous_number == 9 - pos:
            pos += 1
        else:
            if pos == 0:
                for j in range(previous_number + 1, 10):
                    number = number[:-1 - pos] + str(j)
                    result.append(number)
                pos += 1
            else:
                last_numbers = number[-1 - pos:]
                number = number[:-1 - pos]
                for j in range(len(last_numbers)):

                    number += str(previous_number + j + 1)
                result.append(number)

                pos = 0

    for i in result:
        print(i)




if __name__ == "__main__":
    print_comb()