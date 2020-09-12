
if __name__ == "__main__":
    a = [0, 1, 2, 3, 4, 5]
    it = (x for x in a)

    # <generator object <genexpr> at 0x7f99a724b580>
    print(it)

    for i in it:
        print(i)
