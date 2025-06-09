// Input 1: accounts = [[1,2,3],[3,2,1]]
// Output 1: 6
// Explanation 1: 1st customer has wealth = 1 + 2 + 3 = 6
// 2nd customer has wealth = 3 + 2 + 1 = 6
// Both customers are considered the richest
// with a wealth of 6 each, so return 6.
//
// Input2: accounts = [[1, 5], [7, 3], [3, 5]]
// Output2: 10

var solve = function (input) {
   let n = input[0].length;
   let m = input.length;
   let max=0;

   for(let i =0; i<m; i++) {
     let sum =0;
     for(let j=0; j<n; j++) {
       sum += input[i][j];
     }
     if(sum>max) max = sum;
   }
   return max;
};