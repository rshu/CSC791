import re, traceback, random
from dom import mainDom
from unsuper import mainUnsuper


class O:
    y = n = 0

    @staticmethod
    def report():
        print("\n# pass= %s fail= %s %%pass = %s%%" % (
            O.y, O.n, int(round(O.y * 100 / (O.y + O.n + 0.001)))))

    @staticmethod
    def k(f):
        try:
            print("\n-----| %s |-----------------------" % f.__name__)
            if f.__doc__:
                print("# " + re.sub(r'\n[ \t]*', "\n# ", f.__doc__))
            f()
            print("# pass")
            O.y += 1
        except:
            O.n += 1
            print(traceback.format_exc())
        return f


@O.k
def testDomWeather():
    random.seed(1)
    print("\nweatherLong.csv\n")
    mainDom("weatherLong.csv")


@O.k
def testDomAuto():
    random.seed(1)
    print("\nauto.csv\n")
    mainDom("auto.csv", True)


@O.k
def testUnsuper():
    print("\nweatherLong.csv\n")
    mainUnsuper("weatherLong.csv")
