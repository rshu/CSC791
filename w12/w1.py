from __future__ import division
import re, traceback, random, types, pytest
from collections import defaultdict
from collections import Counter
from functools import partial, reduce


class O:
    y=n=0

    @staticmethod
    def report():
        print("\n# pass= %s fail= %s %%pass = %s%%"  % (
          O.y,O.n, int(round(O.y*100/(O.y+O.n+0.001)))))\

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
def testingFailure():
    """this one must fail.. just to test if the  unit test system is working"""
    assert 1==2

@O.k
def testingSuccess():
    """if this one fails, we have a problem!"""
    assert 1==1


"""testcase Page 5"""
long_winded_computation = (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 +
                            13 + 14 + 15 + 16 + 17 + 18 + 19 + 20)

@O.k
def testLongWindedComputation():
    """test long winded computation"""
    assert long_winded_computation == 210


"""testcase Page 6"""
match = 10

@O.k
def testMatchFromRe():
    """test match value in the re module"""
    assert re.match == 10


"""testcase Page 7"""

@O.k
def testDivision():
    """test division after import division module"""
    assert 5/2 == 2.5


"""testcase Page 8"""

def substract(a=0, b=0):
    return a - b

@O.k
def testSubstract():
    """test function substract"""
    assert substract(b=5) == -5


"""testcase Page 9"""

not_tab_string = r"\t"

@O.k
def testStringLength():
    """test string length"""
    assert len(not_tab_string) == 2


"""testcase Page 10"""

@O.k
def testZeroDivision():
    """test throwing an exception"""
    with pytest.raises(ZeroDivisionError) as e:
        1/0
    assert 'division by zero' in str(e.value)


"""testcase Page 11"""

sample_List = [1, 2, 3, 4, 5]

@O.k
def testElementInList():
    """test if 3 is in the list"""
    assert 3 in sample_List


"""testcase Page 12"""

_, y= [1, 2]

@O.k
def testUnpackList():
    """test unpacking the list"""
    assert y == 2


"""testcase Page 13"""

def sum_and_product(x, y):
    return (x + y),(x * y)

s, p = sum_and_product(5, 10)

@O.k
def testTuple():
    """test tuple"""
    assert p == 50


"""testcase Page 14"""

grades = { "Joel" : 80, "Tim" : 95 }

@O.k
def testElementInDictionary():
    """test element in dictionary"""
    assert "Tim" in grades


"""testcase Page 15"""

documents = ["a", "quick", "brown", "fox", "jumps", "over",
             "the", "lazy", "dog"]

word_counts = defaultdict(int)

for word in documents:
    word_counts[word] += 1

@O.k
def testDefaultDict():
    """test the defaultdict"""
    assert word_counts["dog"] == 1


"""testcase Page 16"""

word_counts_by_counter = Counter(documents)

@O.k
def testCounter():
    """test counter"""
    assert word_counts_by_counter["fox"] == 1


"""testcase Page 17"""

s = set()
s.add(1)
s.add(2)
s.add(3)

@O.k
def testElementInSet():
    """test element in set"""
    assert 2 in s


"""testcase Page 18"""

if 1 > 2:
    message = "if only 1 were greater than two…"
elif 1 > 3:
    message = "elif stands for 'else if'"
else:
    message = "when all else fails use else (if you want to)"

@O.k
def testControlFlow():
    """test control flow"""
    assert message == "when all else fails use else (if you want to)"


"""testcase Page 19"""

true_equlas_false = True == False

@O.k
def testTruthiness():
    """test truthiness"""
    assert true_equlas_false == False


"""testcase Page 20"""

@O.k
def testAllFunction():
    """test the all function"""
    assert all([True, 1, { 3 }]) == True


"""testcase Page 22"""

x = sorted([-4,1,-2,3], key=abs, reverse=True)

@O.k
def testSorted():
    """test the sorted function"""
    assert x[-1] == 1


"""testcase Page 23"""

square_dict = { x : x * x for x in range(5) }

@O.k
def testListComprehensions():
    """test list comprehensions"""
    assert square_dict.get(4) == 16


"""testcase Page 24"""

def lazy_range(n):
    i = 0
    while i < n:
        yield i
        i += 1

lazy_evens_below_20 = (i for i in lazy_range(20) if i % 2 == 0)

@O.k
def testGenerator():
    """test if it is a generator object"""
    assert isinstance(lazy_evens_below_20, types.GeneratorType)


"""testcase Page 25"""

@O.k
def testRandomness():
    """test randomness with different seeds"""
    random.seed(10)
    a = random.random()
    random.seed(9)
    b = random.random()
    assert a == b


"""testcase Page 26"""

@O.k
def testRegularExpression():
    """test Regular Expression"""
    assert all([ not re.match("a", "cat"),
                 re.search("a", "cat"),
                 not re.search("c", "dog"),
                 3 == len(re.split("[ab]", "carbs")),
                 "R-D-" == re.sub("[0-9]", "-", "R2D2")
                 ])


"""testcase Page 27"""

class Set:
    def __init__(self, values=None):
        self.dict = {}

        if values is not None:
            for value in values:
                self.add(value)

    def __repr__(self):
        return "Set: " + str(self.dict.keys())

    def add(self, value):
        self.dict[value] = True

    def contains(self, value):
        return value in self.dict

    def remove(self, value):
        del self.dict[value]

s = Set([1,2,3])
s.add(4)

@O.k
def testOOP():
    """test object oriented programming"""
    assert s.contains(4) == True


"""testcase Page 28"""

def exp(base, power):
    return base ** power

two_to_the = partial(exp, 2)

@O.k
def testFunctionalTools():
    """test functional tools"""
    assert two_to_the(3) == 8


"""testcase Page 29"""

xs = [1, 2, 3, 4]

def multiply(x, y):
    return x * y

x_product = reduce(multiply, xs)

@O.k
def testReduce():
    """test the reduce function"""
    assert x_product == 24


"""testcase Page 30"""

for i, document in enumerate(documents):
    if i == 3:
        my_tuple = (i, document)

@O.k
def testEnumerate():
    """test enumerate"""
    assert my_tuple == (3, "fox")


"""testcase Page 31"""

def add(a, b):
    return a + b

@O.k
def testArgumentUnpacking():
    """test argument unpacking"""
    assert add(*[1, 2]) == 3

"""testcase Page 32"""

def other_way_magic(x, y, z):
    return x + y + z

x_y_list = [1, 2]
z_dict = { "z" : 3 }

@O.k
def testArgsAndKwargs():
    """test args and kwargs"""
    assert other_way_magic(*x_y_list, **z_dict) == 6


"""testcase Page 33"""

def f2(x, y):
    return x + y

def doubler_correct(f):
    def g(*args, **kwargs):
        return 2 * f(*args, **kwargs)
    return g

g = doubler_correct(f2)

@O.k
def testArbitraryArguments():
    """test arbitrary arguments"""
    assert g(1,2) == 6

if __name__== "__main__":
    O.report()
