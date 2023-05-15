def foo_1(a: int):
    aa = 1
    b = 2
    c = 3

    return a * a


def foo_2(b: int):
    pass


def main():
    foo_1(2)
    foo_2(3)


if __name__ == "__main__":
    main()
