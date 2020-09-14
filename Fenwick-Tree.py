# Fenwick-Tree
# https://atcoder.jp/contests/practice2/submissions/16653892
size = (1 << 18) + 1
bit = [0] * size

# x(index)の値にvを足す
# indexは1スタート
def bit_update(x, v):
    while x < size:
        bit[x] += v
        x += x & -x  # 区間の長さ


# bit_1 + bit_2 + … + bit_nをO(log(n))で求める
def bit_sum(n):
    s = 0
    if n == 0:
        return 0
    x = n
    while x > 0:
        s += bit[x]
        x -= x & -x
    return s


# a_1 + a_2 + … + a_i >= x となるような最小のiを求める
def lower_bound(v):
    x, sx = 0, 0
    step = size - 1
    while step:
        y = x + step
        sy = sx + bit[y]
        if sy < v:
            x, sx = y, sy
        step >>= 1
    return x + 1


# k番目の数
# 追加
q = [1, 2, 4, 7, 2, 3, 5, 7, 8, 3]
for i in q:
    bit_update(i, 1)

# 消す
for i in [3, 3, 5, 2]:
    bit_update(i, -1)

# k番目に小さい数
for k in [1, 2, 3, 4]:
    print(lower_bound(k))
