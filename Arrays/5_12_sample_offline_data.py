import random

def random_sampling(k:int, A:list[int]) -> list[int]:
    n = len(A)

# If k > n/2 then we can cut the number of random calls by "removing" from the subset
    if k < n // 2:
        for i in range(k):
            r = random.randint(i, n - 1)
            A[i], A[r] = A[r], A[i]
    else:
        for i in range(n - k):
            r = random.randint(i, n - 1)
            A[i], A[r] = A[r], A[i]
    
    return A
            

print(random_sampling(2, [3, 7, 5, 11, 23, 56, 12]))