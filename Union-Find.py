# Union-Find
# https://atcoder.jp/contests/practice2/submissions/16585456
par = [-1 for i in range(n)]  # par<0なら自身が親で要素の個数,par>=0なら子で親の位置示す


def root(a):
    if par[a] < 0:
        return a
    else:
        return root(par[a])


def size(a):
    return -par[root(a)]


def connect(a, b):
    a = root(a)
    b = root(b)
    if a == b:
        return False
    if size(a) < size(b):
        a, b = b, a
    par[a] += par[b]
    par[b] = a
    return True

