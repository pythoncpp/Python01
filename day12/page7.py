def function1():
    num_1 = 10
    num_2 = 30
    print('num1 + num2 = ', (num_1 + num_2))


# function1()

def function2():
    str_1 = "sunbeam"
    str_2 = "infotech"
    print('str_1 + str_2 = ', (str_1 + str_2))


# function2()


class Point:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return "Point [x: {}, y: {}]".format(self._x, self._y)

    # operator overloading
    # - provide different implementation for + operator
    def __add__(self, point):
        x = self._x + point._x
        y = self._y + point._y
        return Point(x, y)

    def __sub__(self, point):
        x = self._x - point._x
        y = self._y - point._y
        return Point(x, y)

    def __gt__(self, other):
        return (self._x > other._x) and (self._y > other._y)

    def __mul__(self, point):
        x = self._x * point._x
        y = self._y * point._y
        return Point(x, y)

    def __div__(self, point):
        x = self._x * point._x
        y = self._y * point._y
        return Point(x, y)

    def __iadd__(self, point):
        x = self._x * point._x
        y = self._y * point._y
        return Point(x, y)

    def add(self, point):
        x = self._x + point._x
        y = self._y + point._y
        return Point(x, y)


p1 = Point(10, 5)
p2 = Point(20, 10)
p3 = Point(30, 40)

# p1 + p2 => p1.__add__(p2) => Point.__add__(p1, p2)
# print('p1 + p2 = ', (p1 + p2))
#
# # p1 - p2 => p1.__sub__(p2) => Point.__sub__(p1, p2)
# print('p1 - p2 = ', (p1 - p2))
#
# # print('p1 + p2 = ', p1.add(p2))
# # print(dir(Point))
#
#
# print('p1 > p2 = ', (p1 > p2))
#
# print('p1 * p2 = ', (p1 * p2))

# p1 + p2 + p3 => p1.__add__(p2) + p3 =>  p1.__add__(p2).__add__(p3)

# 3 + 4 + 5 = 7 + 5 = 12
print('p1 + p2 + p3 = ', (p1 + p2 + p3))


# l1 = [1, 2, 3, 4, 5]
