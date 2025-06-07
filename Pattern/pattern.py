# Input 1: N = 4
# Output 1:
# ****
# ****
# ****
# ****

class Pattern:
    def __init__(self, n):
        self.n = n

    def solve(self):
        pattern = []
        i = self.n
        while i > 0:
            row = ''
            j = self.n
            while j > 0:
                row += '*'
                j -= 1
            pattern.append(row)
            i -= 1
        return pattern

#  option 2 - elegant pythonic way using for loop
def solve2(num):
    for i in range(num):
        row = '* ' * num
        print(row)

#  option 3 - using list comprehension
def solve3(n):
    for _ in range(n): # we use _ because the loop variable is unused
        print('* ' * n)

# --------------------------------------------------------
# Input 1: N = 4
# Output 1:
# *
# **
# ***
# ****

# option 1:
def solve1(N):
 pattern = []
 for i in range(1, N + 1):
     row = "*" * i
     pattern.append(row)

 return pattern

#  option 2: concise and elegant
def solve2(N):
    return ['*' * i for i in range(1, N + 1)]
