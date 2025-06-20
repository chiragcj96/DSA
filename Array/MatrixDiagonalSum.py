# Given a square matrix mat, return the sum of the
# matrix diagonals. Only include the sum of all the
# elements on the primary diagonal and all the
# elements on the secondary diagonal that are not
# part of the primary diagonal.

# Input 1: mat = [[1,2,3], [4,5,6], [7,8,9]]
# Output 1: 25
# Explanation 1: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25.
# Notice that element mat[1][1] = 5 is counted only once.

# 00 01 02 03
# 10 11 12 13
# 20 21 22 23
# 30 31 32 33
# we need to sum only those ele which either have i and j equal like 2,2 or 3,3
# or we need to sum ele with their indexed summing to length of matrix.

class MatrixDiagonalSum:
    def __init__(self, arr):
        self.arr = arr

    def solve(self):
        total = 0
        for i in range(len(self.arr)):
            for j in range(len(self.arr)):
                if i == j or i + j == len(self.arr) - 1:
                    total += self.arr[i][j]
        return total

# this is O[n^2] solution

# For O[n] solution, we only loop through the external loop like this
    def solveOptimized(self):
        n = len(self.arr)
        total = 0
        for i in range(n):
            total += self.arr[i][i]  # Primary diagonal
            total += self.arr[i][n - 1 - i]  # Secondary diagonal

        # Avoid double-counting the center element (only for odd n)
        if n % 2 == 1:
            total -= self.arr[n // 2][n // 2]
        return total
