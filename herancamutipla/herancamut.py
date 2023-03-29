class A():
    def m1(self):
        print('a')
class B(A):
    def m2(self):
        print('b')
class C(A):
    def m2(self):
        print('c')
class D(B, C):
    pass
