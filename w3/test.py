import re,traceback,random
from num import Num
from sym import Sym
from sample import Sample


class O:
    y=n=0

    @staticmethod
    def report():
        print("\n# pass= %s fail= %s %%pass = %s%%"  % (
            O.y,O.n, int(round(O.y*100/(O.y+O.n+0.001)))))

    @staticmethod
    def k(f):
        try:
            print("\n-----| %s |-----------------------" % f.__name__)
            if f.__doc__:
                print("# "+ re.sub(r'\n[ \t]*',"\n# ",f.__doc__))
            f()
            print("# pass")
            O.y += 1
        except:
            O.n += 1
            print(traceback.format_exc())
        return f


@O.k
def testNum():
    n = Num(1024, [4,10,15,38,54,57,62,83,100,100,174,190,215,225,
       233,250,260,270,299,300,306,333,350,375,443,475,
       525,583,780,1000])
    assert abs(n.mu - 270.3) < 0.01
    assert abs(n.sd - 231.946) < 0.01
    print(n.mu, n.sd)


@O.k
def testSample():
    random.seed(1)
    s = [Sample(2**i) for i in range(5, 10)]

    for i in range(10000):
        y = random.random()
        for _, t in enumerate(s):
            t.sampleInc(y)

    for _, t in enumerate(s):
        print(t.max, t.nth(0.5))
        assert abs(t.nth(0.5)-0.5) < 0.33


@O.k
def testSym():
    s = Sym(['y','y','y','y','y','y','y','y','y',
             'n','n','n','n','n'])
    assert abs(s.symEnt() - 0.9403) < 0.01
    print(s.symEnt())

