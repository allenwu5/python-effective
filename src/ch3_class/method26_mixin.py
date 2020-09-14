class A(object):
    def do_a(self):
        print('do_a')


class B(object):
    def do_b(self):
        super().do_a()
        print('do_b')


class C(A):
    def do_c(self):
        super().do_a()
        print('do_a_by_c')


class D(C, B, A):
    pass


if __name__ == "__main__":
    d = D()
    d.do_a()
    d.do_b()
    d.do_c()
