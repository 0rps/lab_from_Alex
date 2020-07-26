# Create a function that capitalize the first letter of each word and transforms all other letter to lowercase


def is_letter(letter):
    if letter >= ord('a') and letter <= ord("z") or (letter >= ord("A") and letter <= ord("Z")):
        return True
    else:
        return False


def create_capitalize(data_str):
    capitalize_str = ""
    separators = " ,.=+-:;?!&"
    delta_between_big_and_little_letters = ord("a") - ord("A")
    for i in range(len(data_str)):
        if i == 0:
            if ord(data_str[i]) >= ord("a") and ord(data_str[i]) <= ord("z"):
                symbol = chr(ord(data_str[i]) - delta_between_big_and_little_letters)
            else:
                symbol = data_str[0]
        elif data_str[i-1] in separators and is_letter(ord(data_str[i])):
            symbol = chr(ord(data_str[i]) - delta_between_big_and_little_letters)
        else:
            if is_letter(ord(data_str[i])) and ord(data_str[i]) >= ord("A") and ord(data_str[i]) <= ord("Z"):
                symbol = chr(ord(data_str[i]) + delta_between_big_and_little_letters)
            else:
                symbol = data_str[i]
        capitalize_str += symbol

    return capitalize_str


def main():
    while True:
        data = input("Enter your string. ")
        if len(data) == 0:
            print("Error. The string must not be empty.")
            continue
        break

    print(create_capitalize(data))


if __name__ == "__main__":
    main()
