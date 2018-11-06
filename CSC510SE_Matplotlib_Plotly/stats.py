"""__author__: RAISE Lab, Fahmid"""

def pairs(lst):
    "Return all pairs of items i,i+1 from a list."
    last = lst[0]
    for i in lst[1:]:
        yield last, i
        last = i

def xtile(lst, lo=0, hi=1, width=10,
          chops=[0.1, 0.3, 0.5, 0.7, 0.9],
          marks=["-", " ", " ", "-", " "],
          bar="|", star="*", show=" %3.0f"):
    """The function _xtile_ takes a list of (possibly)
    unsorted numbers and presents them as a horizontal
    xtile chart (in ascii format). The default is a
    contracted _quintile_ that shows the
    10,30,50,70,90 breaks in the data (but this can be
    changed- see the optional flags of the function).
    """

    def pos(p):
        return ordered[int(len(lst) * p)]

    def place(x):
        return int(width * float((x - lo)) / (hi - lo + 0.00001))

    def pretty(lst):
        return ', '.join([show % x for x in lst])

    ordered = sorted(lst)
    lo = min(lo, ordered[0])
    hi = max(hi, ordered[-1])
    what = [pos(p) for p in chops]
    where = [place(n) for n in what]
    out = [" "] * width
    for one, two in pairs(where):
        for i in range(one, two):
            out[i] = marks[0]
        marks = marks[1:]
    out[int(width / 2)] = bar
    out[place(pos(0.5))] = star
    return '(' + ''.join(out) + ")," + pretty(what)


def median(lst, ordered=False):
    if not ordered: lst = sorted(lst)
    n = len(lst)
    p = n // 2
    if n % 2: return lst[p]
    q = p - 1
    q = max(0, min(q, n))
    return (lst[p] + lst[q]) / 2