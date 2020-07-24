# Create a function which, for a given ints array, applies a function on all elements of the array.
# This function will be applied following the array's order.

def foreach(number):
    return number**2

def main():
    while True:
        try:
            data = list(map(int, input("Enter numbers separated by a space. ").split()))
        except:
            print("Error. Enter only numbers. Try again. ")
            continue
        break

    new_data = []
    for i in data:
        new_data.append(foreach(i))

    for i in new_data:
        print(i, end = " ")


if __name__ == "__main__":
    main()