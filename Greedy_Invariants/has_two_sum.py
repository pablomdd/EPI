# Determine if there are two entries in the array  (not necesarrily distinc) that add up to target

def has_two_sum(A: list[int], t: int) -> bool:
    i, j = 0, len(A) - 1

    while i <= j:
        if A[i] + A[j] == t:
            return True
        elif A[i] + A[j] < t:
            i += 1
        else: #sum > t
            j -= 1
    return False

# Sorted Array, 
array = [-2, 1, 2, 4, 7, 11]
target = 7

print(has_two_sum(array, target))