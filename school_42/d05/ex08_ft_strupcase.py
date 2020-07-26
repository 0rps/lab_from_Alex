# Create a function that transforms every letter of every word to uppercase.


def create_uppercase(data_str):
    upper_str = ""
    delta_between_big_and_little_letters = ord("a") - ord("A")
    for i in data_str:
        if ord("a") <= ord(i) <= ord("z"):
            symbol = chr(ord(i) - delta_between_big_and_little_letters)
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
