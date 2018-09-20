import re, traceback, random
from num import Num
from sym import Sym
from sample import Sample
from rows import rows


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
def test_Rows():
    print("\nweather.csv\n")
    rows("weather.csv")
    print("\nweatherLong.csv\n")
    rows("weatherLong.csv")
    print("\nauto.csv\n")
    rows("auto.csv")
