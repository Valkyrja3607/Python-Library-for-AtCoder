# Floor-Sum
# https://atcoder.jp/contests/practice2/submissions/16749655
def Floor_sum(N, M, A, B):
    ANS = 0
    if A >= M:
        ANS += N * (N - 1) // 2 * (A // M)
        A %= M
    if B >= M:
        ANS += B // M * N
        B %= M
    y_max = (A * N + B) // M
    x_max_divA = y_max * M - B
    if y_max == 0:
        return ANS
    else:
        ANS += Floor_sum(y_max, A, M, A * N - x_max_divA)
        return ANS
