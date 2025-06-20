// Input 1: nums = [1,2,3,4]
// Output 1: [1,3,6,10]
// Explanation 1: Running sum is obtained
// as follows: [1, 1+2, 1+2+3, 1+2+3+4].

// In-place modification (No extra space)
var solve = function (arr) {
     for (let i=1; i<arr.length; i++){
          arr[i] += arr[i-1]
     }
    return arr
};
