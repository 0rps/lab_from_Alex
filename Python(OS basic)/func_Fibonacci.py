def func(f1, f2, n):
    if n == 0:
        return f1 + f2
    else:
        return func(f2, f1 + f2, n-1)


if __name__ == "__main__":
    print(func(1, 1, int(input()) - 3))
