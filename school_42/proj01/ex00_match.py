# The purpose of this function is to find out whether two strings match.
# s1 and s2 are considered to match when s1 and s2 are identical.
# If s2 contains a star ("*"), we can replace this star by any chareacters string (even empty) to make s1 and s2 indentical.
# s2 may hold as many stars as you'd like.
# It must return 1 if s1 and s2 match, or 0 if they don't.


def match(s1, s2):
    i_s1 = 0
    j_s2 = 0
    flag = False
    while i_s1 < len(s1) and j_s2 < len(s2):
        if s1[i_s1] == s2[j_s2]:
            i_s1 += 1
            j_s2 += 1
        else:
            if s2[j_s2] != "*":
                return 0
            else:
                flag = True
                if j_s2+1 >= len(s2):
                    return 1
                else:
                    j_s2 += 1
                    i_s1 += 1
                    while i_s1 < len(s1):
                        if i_s1 == len(s1)-1 and s1[i_s1] != s2[j_s2]:
                            return 0
                        elif s1[i_s1] != s2[j_s2]:
                            i_s1 += 1
                            continue
                        break

    if len(s1) == len(s2) or flag:
        return 1
    return 0


def main():
    s1 = input("Enter s1: ")
    s2 = input("Enter s2: ")

    print(match(s1, s2))


if __name__ == "__main__":
    main()
