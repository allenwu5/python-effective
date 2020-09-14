class GenericInputData():
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls):
        raise NotImplementedError


class PathInputData(GenericInputData):
    def read(self):
        return print(f'read: {self.path}')

    @classmethod
    def generate_inputs(cls):
        return cls('path input data')


if __name__ == "__main__":
    given_classes = [PathInputData]
    for class_ in given_classes:
        a = class_.generate_inputs()
        a.read()
