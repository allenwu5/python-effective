from itertools import zip_longest

if __name__ == "__main__":
    a = ["a", "b", "c", "d", "e"]
    b = ["1", "2", "3", "4"]

    for i, c in zip(a, b):
        print(i, c)

    for i, c in zip_longest(a, b):
        print(i, c)
