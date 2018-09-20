import re
from sym import Sym
from num import Num


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

                if re.search('[<>$]', x):
                    self.nums[c] = Num(1024, [])
                else:
                    self.syms[c] = Sym([])

                if re.search('<', x):
                    self.w[c] = -1
                elif re.search('>', x):
                    self.w[c] = 1
                elif re.search('!', x):
                    self._class = c
                else:
                    self.indeps.append(c)

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


""" read the file and display result"""
def rows1(src):
    first = True
    data = Data()
    if src[-3:] in ["csv"]:
        with open(src) as file:
            for line in file:
                line = re.sub('[\t\r\n]*|#.*', "", line)
                cells = [i.strip() for i in line.split(',')]
                if len(cells) > 0:
                    if first:
                        data.header(cells)
                    else:
                        data.row(cells)
                    first = False

    print("\t\t\tn\tmode\tfrequency\n")
    for index, value in data.syms.items():
        print(f'{index}\t{data.name[index]}\t\t{value.n}\t{value.mode}\t{value.most}')
    print("\n\t\t\tn\tmu\tsd\n")
    for index, value in data.nums.items():
        print(f'{index}\t{data.name[index]}\t\t{value.n}\t{value.mu:.2f}\t{value.sd:.2f}')


def rows(s):
    rows1(s)

