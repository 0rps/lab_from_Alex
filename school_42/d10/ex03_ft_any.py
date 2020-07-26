# Create a function which will return 1 if, passed to the function, at least one element of the array returns 1.
# Else, it should return 0.

def f(element):
    if element > 10:
        return 1
    else:
        return 0

def ft_any(data):
    for i in data:
        if f(i) == 1:
            return 1
    return 0

def main():
    while True:
        try:
            data = list(map(int, input("Enter the numbers. ").split()))
        except:
            print("Error. Use only number. Try again. ")
            continue
        break

    print(ft_any(data))

if __name__ == "__main__":
    main()