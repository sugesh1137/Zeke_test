class Complex(object):
    def __init__(self, real = 0.0, img=0.0):
        self.real = real
        self.img = img

    def printcomplex(self):
        print self.real,"+ i",self.img

    def __add__(self, other):
        return Complex(self.real + other.real,
                       self.img + other.img)

    def __sub__(self, other):
        return Complex(self.real - other.real,
                       self.img - other.img)

    def __mul__(self, other):
        return Complex(self.real*other.real - self.img*other.img,
                       self.img*other.real + self.real*other.img)

    def __div__(self, other):
        sr, si, otr, oi = self.real, self.img, \
                         other.real, other.img # short forms
        r = float(otr**2 + oi**2)
        return Complex((sr*otr+si*oi)/r, (si*otr-sr*oi)/r)

    def __abs__(self):
        return sqrt(self.real**2 + self.img**2)

    def __neg__(self):
        return Complex(-self.real, -self.img)

    def __eq__(self, other):
        return self.real == other.real and self.img == other.img

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return '(%g, %g)' % (self.real, self.img)