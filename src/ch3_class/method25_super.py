from pprint import pprint


class A():
    def __init__(self):
        print('Class A')


class B(A):
    def __init__(self):
        super().__init__()
        print('Class B')


class B2(A):
    def __init__(self):
        super().__init__()
        print('Class B2')


class C(B2, B):
    def __init__(self):
        super().__init__()
        print('Class C')


if __name__ == "__main__":
    # Class A
    # Class B
    # Class B2
    # Class C
    C()

    # Method resolution order
    # [<class '__main__.C'>,
    #  <class '__main__.B2'>,
    #  <class '__main__.B'>,
    #  <class '__main__.A'>,
    #  <class 'object'>]
    pprint(C.mro())
