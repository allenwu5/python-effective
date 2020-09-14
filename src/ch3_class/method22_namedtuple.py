from collections import namedtuple

if __name__ == "__main__":
    GenderAge = namedtuple('GenderAge', ('gender', 'age'))
    ga = GenderAge('female', 27)
    print(ga.gender)
    print(ga.age)
