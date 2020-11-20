# A = [0,1,2,0,2,1,1]
#          i

# First Solution
# Brute force memory: O(n)

# Took 2 min to think implementation

# B = []
# queue = [] empty queue -> greater than pivot
# B = [0, 1, 0 , 1 , 1]
# queue = [2, 2,]

# -> A = [B, queue]


# Time: O(n)
# Mem: O(1)

def dutch_flag(pivot_index, A):
    pivot = A[pivot_index]

#  Move elements less that pivor to the beginning of the array
# pointers are used to keep track of the last element found
    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1

#  Move elements greater that pivot to the end of the array
    larger = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        elif A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1
    return A


    
A = [0,1,2,0,2,1,1]
print(dutch_flag(1 , A))