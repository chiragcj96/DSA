# Input:  [[1, 1, 0],
#          [1, 0, 1],
#          [0, 0, 1]]
#
# Flipped: [[0, 1, 1],
#           [1, 0, 1],
#           [1, 0, 0]]
#
# Inverted : [[1, 0, 0],
#             [0, 1, 0],
#             [0, 1, 1]]

class FlipandInvert:
    def __init__(self, arr):
        self.arr = arr

    def solve(self):
        flipped = [row[::-1] for row in self.arr]
        # 1-0 = 1 so inverted 0 to 1
        # 1-1 = 0 so inverted 1 to 0
        return [[1 - bit for bit in r] for r in flipped]

#  we can also do this on one place without using two spaces like-
return [[1 - row[i] for i in reversed(range(len(row)))] for row in self.arr]
