# Input 1: accounts = [[1,2,3],[3,2,1]]
# Output 1: 6
# Explanation 1: 1st customer has wealth = 1 + 2 + 3 = 6
# 2nd customer has wealth = 3 + 2 + 1 = 6
# Both customers are considered the richest
# with a wealth of 6 each, so return 6.
#
# Input2: accounts = [[1, 5], [7, 3], [3, 5]]
# Output2: 10

class RichestCustomerWealth:
    def __init__(self, arr):
        self.arr = arr

    def solve(self):
        result = 0
        n = len(self.arr)
        m = len(self.arr[0])

        for i in range(n):
             sum = 0
             for j in range(m):
                  sum+=self.arr[i][j]
             if(sum>result): result = sum
        return result

class RichestCustomerWealth2:
    def __init__(self, arr):
        self.arr = arr

    def solve(self):
        return max(map(sum, self.arr))