class LazyDB():
    def __init__(self):
        self.exists = 5


    def __getattr__(self, name):
        print('Call __getattr__')
        value = f'Value for {name}'
        setattr(self, name, value)
        return value

    def __setattr__(self, name, value):
        # print(f'__setattr__ {name} {value}')
        super().__setattr__(name, value)

class LazyDB2(LazyDB):
    def __getattribute__(self, name):
        print('Call __getattribute__')
        value = f'Value for {name}'
        setattr(self, name, value)
        return value


if __name__ == "__main__":
    l = LazyDB()

    print(l.field)

    print(l.field)

    l2 = LazyDB2()

    print(l2.field2)

    print(l2.field2)
