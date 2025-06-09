# Given the array nums consisting of n(n will be even)
# elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].
#
# Input 1: nums = [2,5,1,3,4,7]
# Output 1: [2,3,5,4,1,7]
# Explanation 1: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7
# then the answer is [2,3,5,4,1,7].

class Shuffle:
    def __init__(self, arr):
        self.arr = arr

    def shuffle(self):
        result = []
        n = len(self.arr)
        for i in range(n // 2):
            result.append(self.arr[i])
            result.append(self.arr[i + n // 2])
        return result