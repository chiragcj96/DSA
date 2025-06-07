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

// Option 2 - Using a Helper gcd Function (Recursive Euclidean Algorithm)
function gcd(a, b) {
    return b === 0 ? a : gcd(b, a % b);
}

var solve = function (nums) {
    const minNum = Math.min(...nums);
    const maxNum = Math.max(...nums);

    return gcd(minNum, maxNum);
};

// option 3 - With Arrow Functions & Recursion
const solve = nums => {
    const gcd = (a, b) => b ? gcd(b, a % b) : a;
    return gcd(Math.min(...nums), Math.max(...nums));
};

