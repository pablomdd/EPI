# Jon Bentley implementation

def bsearch (t: int, A: list[int]) -> int:
    L, U = 0, len(A) - 1

    while L <= U:
        M = L + (U-L) / 2

        if A[M] < t:
            L = M + 1
        elif A[M] == t:
            return M
        else:
            U = M - 1
    return -1