from __future__ import division
import re, sys
from num import Num
from sym import Sym


class Data:

    def __init__(self):
        self.w = {}
        self.syms = {}
        self.nums = {}
        self._class = None
        self.rows = []
        self.name = []
        self._use = []
        self.indeps = []

    """independent columns"""

    def indep(self, c):
        return c not in self.w and self._class != c

    """dependent columns"""

    def dep(self, c):
        return not self.indep(c)

    """read and processes special symbols that define a table"""

    def header(self, cells):
        for index, x in enumerate(cells):
            if not re.match(r'^\?', x):
                c = len(self._use)
                self._use.append(index)
                self.name.append(x)

                if re.search("[<>$]", x):
                    self.nums[c] = Num()
                else:
                    self.syms[c] = Sym()

                if re.search("<", x):
                    self.w[c] = -1
                elif re.search(">", x):
                    self.w[c] = 1
                elif re.search("!", x):
                    self._class = c
                else:
                    self.indeps.append(c)
        return self

    """add a row"""

    def row(self, cells):
        r = len(self.rows)
        self.rows.append([])
        for c, c0 in enumerate(self._use):
            x = cells[c0]
            if x != "?":
                if c in self.nums:
                    try:
                        x = int(x)
                    except ValueError:
                        x = float(x)
                    self.nums[c].numInc(x)
                else:
                    self.syms[c].symInc(x)
            self.rows[r].append(x)
        return self


"""return lines in csv file"""


def lines(src=None):
    if not src:
        for line in sys.stdin:
            yield line
    elif src[-3:] in ["csv"]:
        with open(src) as fs:
            for line in fs:
                yield line
    else:
        for line in src.splitlines():
            yield line


""" read the file and display result"""


def rows1(src):
    first = True
    data = Data()
    for line in src:
        line = re.sub(r'([ \n\r\t]|#.*)', "", line)
        cells = line.split(",")
        if len(cells) > 0 and cells[0] != "":
            if first:
                data.header(cells)
            else:
                data.row(cells)
            first = False
    return data


def rows(s):
    return rows1(lines(s))
