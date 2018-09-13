from sample import Sample


class Num:

    def f(x):
        return x

    def __init__(self, max, pairs=[], f=f):
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.sd = 0
        self.lo = 10**32
        self.hi = -10**32
        self.some = Sample(max)
        self.w = 1
        for x in pairs:
            self.symInc(f(x))

    def numInc(self,x):
        if x == "?":
            return x

        self.n += 1
        self.some.sampleInc(x)
        d = x - self.mu
        self.mu += d/self.n
        self.m2 += d*(x-self.mu)

        if x > self.hi:
            self.hi = x
        if x < self.lo:
            self.lo = x

        if self.n >=2:
            self.sd = (self.m2/(self.n - 1 + 10**-32))**0.5
        return x

    def numDec(self,x):
        if x == "?":
            return x

        if self.n == 1:
            return x

        self.n -= 1
        d = x - self.mu
        self.mu -= d/self.n
        self.m2 -= self.m2 - d*(x - self.mu)
        if self.n >= 2:
            self.sd = (self.m2/(self.n - 1 + 10**-32))**0.5
        return x

    def numNorm(self, x):
        if x == "?":
            return 0.5
        else:
            return (self.x -self.lo)/(self.hi- self.lo + 10**-32)
