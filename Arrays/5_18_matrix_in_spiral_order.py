def matrix_in_spiral_order(A: list[list[int]]) -> list[int]:
    i, j = 0 , 0
    






matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9] ]
# output = [1, 2, 3 , 6, 9, 8 , 7, 4 ,5]
# clockwise movement
# right
# [[4, 5, 6], [7, 8, 9] ]
# down
# [[4, 5], [7, 8] ] - n-1 x m-1 matrix
# left
# [[4, 5]] - n-1 row
# up 
# [[5]] - n-2 row x m-2 columns
# repeat
