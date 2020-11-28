# Optimal:
def has_tree_sum(A: list[int], t: int) -> bool:
    # O(nlogn)
    A.sort()
    
    # Now, we fix i and seach for indices j,k such as  A[j] + A[k] = t -A[i]
    j, k = 0, len(A) - 1
    
    # O(n2)
    for i in A:
        while j <= k:
            if A[j] + A[k] == t - A[i]:
                return True
            elif A[j] + A[k] < t - A[i]:
                j += 1
            else: # sum A t-A[i]
                k -= 1
    return False

    # Final Time: O(n2)
    # Space: O(1)


