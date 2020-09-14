from collections.abc import Sequence

class MySeq(Sequence):

    def __getitem__(self, index):
        pass

    def __len__(self):
        pass

class MySeq2(list):
    pass

if __name__ == "__main__":
    s = MySeq()
    # 'MySeq' object has no attribute 'append'
    # s.append(1)

    s = MySeq2()
    s.append(1)
    print(s)