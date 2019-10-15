class A:

    def __str__(self):
        return "A"


class B:

    def __str__(self):
        return "B"


class C:

    def __str__(self):
        return "C"


# a = A()
# print(a)
#
# b = B()
# print(b)
#
# c = C()
# print(c)


class P:

    def __str__(self):
        return "P"

    def my_method(self):
        print('my method')


class Q(P):

    def __str__(self):
        return "Q"


class R(Q):

    def __str__(self):
        return "R"


# p = P()
# print(p)
#
# q = Q()
# print(q)
#
# r = R()
# print(r)


print(dir(P))













