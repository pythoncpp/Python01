class Complex:

    def __init__(self, real, imaginary):
        self._real = real
        self._imaginary = imaginary

        # print('type of real: ', type(self._real))
        # print('type of imaginary: ', type(self._imaginary))


    def __str__(self):
        return "{} + {}i".format(self._real, self._imaginary)

    def __add__(self, other):
        real = self._real + other._real
        imaginary = self._imaginary + other._imaginary
        return Complex(real, imaginary)

    def __sub__(self, other):
        real = self._real - other._real
        imaginary = self._imaginary - other._imaginary
        return Complex(real, imaginary)


# 5 + 3i
c1 = Complex(5, 3)
print(c1)

# 6 + 2i
c2 = Complex(6, 2)
print(c2)

print('c1 + c2 = ',  c1 + c2)
print('c1 - c2 = ',  c1 - c2)