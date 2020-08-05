# Create a function which, for a given ints array, applies a function on all elements of the array (in ordre)
# and returns values. This function will be applied following the array's order.

def function(number):
    return number**2

def ft_map(number_data, func):
    new_data = []
    for i in number_data:
        new_data.append(func(i))
    return new_data

def main():
    while True:
        try:
            data = list(map(int, input("Enter numbers separated by a space. ").split()))
        except:
            print("Error. Enter only numbers. Try again. ")
            continue
        break

    new_numbers = ft_map(data, function)

    for i in new_numbers:
        print(i, end=" ")

if __name__ == "__main__":
    main()