# Create a function that transforms every letter of every word to uppercase.

def create_uppercase(data_str):
    upper_str = ""
    for i in data_str:
        if ord(i) >= 97 and ord(i) <= 122:
            symbol = chr(ord(i) - 32)
        else:
            symbol = i
        upper_str += symbol

    return upper_str

def main():
    while True:
        data = input("Enter your string. ")
        if len(data) == 0:
            print("Error. The string must not be empty.")
            continue
        break

    print(create_uppercase(data))

if __name__ == "__main__":
    main()
