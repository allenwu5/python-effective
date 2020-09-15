class A():
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value * 1.0

    @value.setter
    def value(self, value):
        self._value = value
        print(f'set value {value} by setter')


if __name__ == "__main__":
    a = A(3)
    # a.value is not callable
    # print(a.value())
    print(a.value)
    a.value = 4
    print(a.value)
