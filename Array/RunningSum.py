# Input 1: nums = [1,2,3,4]
# Output 1: [1,3,6,10]
# Explanation 1: Running sum is obtained
# as follows: [1, 1+2, 1+2+3, 1+2+3+4].

def sum(self):
    result = [self.arr[0]]
    for i in range(1, len(self.arr)):
        result.append(self.arr[i] + result[i - 1])
    return result


# In-place modification (No extra space)
def running_sum(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums