from __future__ import division
import random, math


class Sample:

    def __init__(self, max=1024):
        self.max = max
        self.rank = 1
        self.n = 0
        self.sorted = False
        self.some = []

    def sampleInc(self, x):
        self.n += 1
        now = len(self.some)
        if now < self.max:
            self.sorted = False
            self.some.append(x)
        elif random.random() < now / self.n:
            self.sorted = False
            self.some[math.floor(random.random() * now)] = x
            # self.some[math.floor(0.5 + random.random()*now)] = x
        return x

    def sampleSorted(self):
        if not self.sorted:
            self.sorted = True
            self.some.sort()
        return self.some

    def nth(self, n):
        s = self.sampleSorted()
        return s[min(len(s), max(1, math.floor(0.5 + len(s) * n)))]

    def sampleLt(self, s1, s2):
        return self.nth(s1, 0.5) < self.nth(s2, 0.5)
