# Floor-Sum
# https://atcoder.jp/contests/practice2/submissions/16749655
def Floor_sum(n, m, a, b):
    ans = 0
    if a >= m:
        ans += n * (n - 1) // 2 * (a // m)
        a %= m
    if b >= m:
        ans += b // m * n
        b %= m
    y_max = (a * n + b) // m
    x_max_divA = y_max * m - b
    if y_max == 0:
        return ans
    else:
        ans += Floor_sum(y_max, a, m, a * n - x_max_divA)
        return ans
