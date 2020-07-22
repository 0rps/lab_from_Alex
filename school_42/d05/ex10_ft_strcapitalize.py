# Create a function that capitalize the first letter of each word and transforms all other letter to lowercase

def is_letter(letter):
    if letter >= 65 and letter <= 90 or (letter >= 97 and letter <= 122):
        return True
    else:
        return False

def create_capitalize(data_str):
    capitalize_str = ""
    separators = " ,.=+-:;?!&"
    for i in range(len(data_str)):
        if i == 0:
            symbol = chr(ord(data_str[i]) - 32)
        elif data_str[i-1] in separators and is_letter(ord(data_str[i])):
            symbol = chr(ord(data_str[i]) - 32)
        else:
            if is_letter(ord(data_str[i])) and ord(data_str[i]) >= 65 and ord(data_str[i]) <= 90:
                symbol = chr(ord(data_str[i]) + 32)
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