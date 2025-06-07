# Find Greatest Common Divisor of Array

# Input 1: nums = [2,5,6,9,10]
# Output 1: 2
# Explanation 1: The smallest number in nums is 2. The largest number in nums is 10.
# The greatest common divisor of 2 and 10 is 2.

import math
class GCD:
    def __init__(self, arr):
        self.arr = arr

    def gcd(self):
        a = min(self.arr)
        b = max(self.arr)
        return math.gcd(a, b)