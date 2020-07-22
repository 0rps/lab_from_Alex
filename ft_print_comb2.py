# Create a function that displays all different combination of two digits between 00 and 99, listed by ascending order.

def print_comb():
    all_numbers = []
    number = ''
    for i in range(10):
        for j in range(10):
            number = str(i) + str(j)
            all_numbers.append(number)

    pairs_of_numbers = []
    for i in range(len(all_numbers)-1):
        for j in range(i+1,len(all_numbers)):
            pairs_of_numbers.append(tuple((all_numbers[i], all_numbers[j])))

    for i in range(len(pairs_of_numbers)):
        if i == len(pairs_of_numbers)-1:
            print(f'{pairs_of_numbers[i][0]} {pairs_of_numbers[i][1]}')
        else:
            print(f'{pairs_of_numbers[i][0]} {pairs_of_numbers[i][1]}', end=', ')

if __name__ == "__main__":
    print_comb()