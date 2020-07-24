# Create a function which, for a given ints array, applies a function on all elements of the array.
# This function will be applied following the array's order.

def function(number):
    return number**2

def foreach(number_data, f):
    for i in number_data:
        print(f(i), end = " ")

def main():
    while True:
        try:
            data = list(map(int, input("Enter numbers separated by a space. ").split()))
        except:
            print("Error. Enter only numbers. Try again. ")
            continue
        break

    foreach(data, function)

if __name__ == "__main__":
    main()