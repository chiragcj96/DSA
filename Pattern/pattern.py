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

# Input 1: N = 4
# Output 1:
# a
# ab
# abc
# abcd

class Pattern:
    def __init__(self, n):
        self.n = n

    def solve(self):
        pattern = []
        for i in range(self.n + 1):
            row = ''
            for j in range(i):
                row += chr(ord('a') + j)
            pattern.append(row)
        return pattern

# Input 1: N = 4
# Output 1:
# 1
# 12
# 123
# 1234

def pattern5(n):
    pattern = []
    for i in range(1, n + 1):
        row = ''
        for j in range(1, i + 1):
            row += str(j)
        pattern.append(row)
    return pattern

# Input 1: N = 4
# Output 1:
# * * * *
# *     *
# *     *
# * * * *
#
# Input 2: N = 3
# Output 2:
# * * *
# *   *
# * * *

def solve(self):
    pattern = []
    for i in range(self.n):
        row = ''
        for j in range(self.n):
            if (i == 0 or i == self.n - 1) or (j == 0 or j == self.n - 1):
                row += '*'
            else:
                row += " "
        pattern.append(row)
    return pattern

def solve(self):
    return [
        ''.join(
            '*' if (i == 0 or i == self.n - 1 or j == 0 or j == self.n - 1) else ' '
            for j in range(self.n)
        )
        for i in range(self.n)
    ]

