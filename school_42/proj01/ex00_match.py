# The purpose of this function is to find out whether two strings match.
# s1 and s2 are considered to match when s1 and s2 are identical.
# If s2 contains a star ("*"), we can replace this star by any chareacters string (even empty) to make s1 and s2 indentical.
# s2 may hold as many stars as you'd like.
# It must return 1 if s1 and s2 match, or 0 if they don't.


def match(s1, s2):
    if s2 == "*" or s1 == s2:
        return 1
    elif s1[0] != s2[0] and s2[0] != "*":
        return 0
    elif s1[0] == s2[0]:
        return match(s1[1:], s2[1:])
    else:
        for i in range(len(s1) + 1):
            if match(s1[i:], s2[1:]) == 1:
                return 1
    return 0


def main():
    s1 = input("Enter s1: ")
    s2 = input("Enter s2: ")
    print(match(s1, s2))


if __name__ == "__main__":
    main()
