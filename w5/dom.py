import random, math, operator
from rows import rows

samples = 100


def cap(x, lo, hi):
    return min(hi, max(lo, x))


def dump(a, sep="\t"):
    for i in a:
        i[len(i) - 1] = str("%.2f" % i[len(i) - 1])
        print(sep.join(str(e) for e in i))


def another(x, t):
    y = cap(math.floor(random.random() * len(t)), 0, len(t) - 1)
    if x == y:
        return another(x, t)
    if t[y]:
        return t[y]
    return another(x, t)


def dom(data, row1, row2):
    s1, s2 = 0, 0
    n = len(data.w)
    for c, w in data.w.items():
        a0 = row1[c]
        b0 = row2[c]
        a = data.nums[c].numNorm(a0)
        b = data.nums[c].numNorm(b0)
        s1 -= 10 ** (w * (a - b) / n)
        s2 -= 10 ** (w * (b - a) / n)
    return s1 / n < s2 / n


def doms(data, reduced):
    if len(data.w) == 0:
        return
    n = samples
    c = len(data.name)
    print("\t".join(data.name) + "\t>dom")
    for r1, row1 in enumerate(data.rows):
        row1.append(0)
        for i in range(n):
            row2 = another(r1, data.rows)
            s = dom(data, row1, row2) and 1 / n or 0
            row1[c] += s
    o = len(data.rows) - 20
    if reduced and o > 0:
        data.rows = sorted(data.rows, key=operator.itemgetter(len(data.rows[0]) - 1))
        dump(data.rows[:10])
        print("---- " + str(o) + " Lines here ----")
        dump(data.rows[-10:])
    else:
        dump(data.rows)


def main_dom(s, reduced=False):
    doms(rows(s), reduced)
