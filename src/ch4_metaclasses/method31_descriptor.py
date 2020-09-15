from weakref import WeakKeyDictionary


class Grade():
    def __init__(self):
        # Memory leak ...
        # self._values = {}
        self._values = WeakKeyDictionary()

    def __get__(self, instance, instance_type):
        return self._values[instance]

    def __set__(self, instance, value):
        self._values[instance] = value
        print(f'assign {value}')


class Exam():
    g1 = Grade()
    g2 = Grade()
    g3 = Grade()


if __name__ == "__main__":
    e1 = Exam()
    e1.g1 = 1
    e1.g2 = 2
    e1.g3 = 3

    e2 = Exam()
    e2.g1 = 1+10
    e2.g2 = 2+10
    e2.g3 = 3+10

    print(e1.g3)
    print(e2.g3)
