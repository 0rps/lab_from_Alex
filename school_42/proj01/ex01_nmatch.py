# The aim of this function is to count the amount of times two string match.
# When we have two or more stars, multiple string combinations can be suitable.
# nmatch calculates the total amount of combinations.
# nmatch returns the number of combinations that match.


def nmatch(s1, s2):
    res = 0
    if s2 == "*" or s1 == s2:
        return 1
    elif s1[0] != s2[0] and s2[0] != "*":
        return 0
    elif s1[0] == s2[0]:
        res += nmatch(s1[1:], s2[1:])
    else:
        for i in range(len(s1)+1):
            res += nmatch(s1[i:], s2[1:])
    return res


def main():
    s1 = input("Enter s1: ")
    s2 = input("Enter s2: ")
    print(nmatch(s1, s2))


if __name__ == "__main__":
    main()
