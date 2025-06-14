// Input 1: N = 4
// Output 1:
// ****
// ****
// ****
// ****

// option 1 - use nested loops.
var solve = function(n){
     let pattern = [];
     var i = n;

     while (i>0) {
          let row = '';
          var j = n;

          while (j>0) {
               row += "* ";
               j-=1;
          }
          pattern.push(row);
          i-=1;
     }
     return pattern
};

// option 2 - use "*".repeat(n) → returns a string with "*" repeated n times.
var solve = function(n) {
    let pattern = [];
    for (let i = 0; i < n; i++) {
        pattern.push("* ".repeat(n));
    }
    return pattern;
};

// --------------------------------------------------------
// Input 1: N = 4
// Output 1:
// *
// **
// ***
// ****

var solve = function(n){
     let pattern = [];
     for (let i=1; i<n+1; i++) {
          pattern.push("*".repeat(i));
     }
     return pattern
};

// --------------------------------------------------------
// Input 1: N = 4
// Output 1:
// 1
// 12
// 123
// 1234

var solve4 = function(n){
     let pattern = []
     for (let i=1; i<n+1; i++){
          let row = ''
          for (let j=1; j<i+1; j++){
               row+=String(j)
          }
          pattern.push(row)
     }
     return pattern
};

// --------------------------------------------------------
// Input 1: N = 4
// Output 1:
// * * * *
// *     *
// *     *
// * * * *
//
// Input 2: N = 3
// Output 2:
// * * *
// *   *
// * * *

var solve = function(n){
     let pattern = [];

    for (let i = 0; i < n; i++) {
        let row = '';
        for (let j = 0; j < n; j++) {
            if (i === 0 || i === n - 1 || j === 0 || j === n - 1) {
                row += '*';
            } else {
                row += ' ';
            }
        }
        pattern.push(row);
    }
    return pattern;
};
