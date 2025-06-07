// Find Greatest Common Divisor of Array

// Input 1: nums = [2,5,6,9,10]
// Output 1: 2
// #Explanation 1: The smallest number in nums is 2. The largest number in nums is 10.
// The greatest common divisor of 2 and 10 is 2.

const solve = function (nums) {
    let a = Math.min(...nums);
    let b = Math.max(...nums);

    while (b) {
        let temp = b
        b = a % b;
        a = temp;
    }
    return a;
};

