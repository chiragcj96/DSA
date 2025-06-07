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

// Input 1: N = 4
// Output 1:
// *
// **
// ***
// ****