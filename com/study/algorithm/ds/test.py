
class A(object):

    def __init__(self,a,b):
        self._a = a
        self._b = b

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, a):
        self._a = a

if __name__ == '__main__':
    aa = A(1,2)
    print(aa.a)
