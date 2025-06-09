// Given the array nums consisting of n(n will be even)
// elements in the form [x1,x2,...,xn,y1,y2,...,yn].
// Return the array in the form [x1,y1,x2,y2,...,xn,yn].
//
// Input 1: nums = [2,5,1,3,4,7]
// Output 1: [2,3,5,4,1,7]
// Explanation 1: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7
// then the answer is [2,3,5,4,1,7].

var solve = function (nums) {
     let result = []
     let n = nums.length
     for (let i=0; i<n/2; i++){
          result.push(nums[i]);
          result.push(nums[i+n/2]);
     }
     return result
};