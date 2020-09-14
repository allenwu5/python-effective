class A():
    def __init__(self, value):
        self.__value = value

    def value(self):
        return self.__value


class B(A):
    def __init__(self, value):
        super().__init__(value)
        self._value = value

    def value(self):
        return self.__value

    def protected_value(self):
        return self._value


if __name__ == "__main__":
    a = A(3)

    # 'A' object has no attribute '__value'
    # print(a.__value)

    print(a._A__value)

    print(a.value())

    b = B(4)

    # 'B' object has no attribute '_B__value'
    # print(b.value())

    print(b.protected_value())
