# Segment-Tree

# 配列Aで初期化。O(N)
def init_max(init_max_val):
    # set_val
    for i in range(n):
        seg_max[i + num_max - 1] = init_max_val[i]
    # built
    for i in range(num_max - 2, -1, -1):
        seg_max[i] = max(seg_max[2 * i + 1], seg_max[2 * i + 2])


# A[k]をxに変更 O(logN)
def update_max(k, x):
    k += num_max - 1
    seg_max[k] = x
    while k:
        k = (k - 1) // 2
        seg_max[k] = max(seg_max[k * 2 + 1], seg_max[k * 2 + 2])


# A[p]~A[q-1]の最大値 O(logN)
def query_max(p, q):
    if q <= p:
        return ide_ele_max
    p += num_max - 1
    q += num_max - 2
    res = ide_ele_max
    while q - p > 1:
        if p & 1 == 0:
            res = max(res, seg_max[p])
        if q & 1 == 1:
            res = max(res, seg_max[q])
            q -= 1
        p = p // 2
        q = (q - 1) // 2
    if p == q:
        res = max(res, seg_max[p])
    else:
        res = max(max(res, seg_max[p]), seg_max[q])
    return res


n = 5
A = [1, 4, 3, 2, 4]

# 単位元
# Aの最小値より小さいもの。(元々-1)
ide_ele_max = -(10 ** 10)

# num_max:n以上の最小の2のべき乗
num_max = 2 ** (n - 1).bit_length()
seg_max = [ide_ele_max] * 2 * num_max

# init
init_max(A)
# A[1]~A[3]の最大値
print(query_max(1, 4))  # 4
# A[3]を5に変更
update_max(3, 5)
# A[1]~A[3]の最大値
print(query_max(1, 4))  # 5

