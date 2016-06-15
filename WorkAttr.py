class Num(object):
    def __init__(self, v = 1):
        self.v = v
    def pow(self, p):
        return self.v**p


if __name__ == '__main__':
    n = Num()
    fn = getattr(n, 'pow')
    print fn(2)
    n.v = 3
    print fn(2)