/*var arr2d = [[2, 5, 8],
[3, 6, 1],
[5, 7, 7]];

// We can console.log the `8` in this array if we
//console.log(arr2d[0][3]);
// the first index `0` will select the `[2, 5, 8]` sub-array
// the second index `2` will select the `8` out of that sub-array


//loops over the outer array
for (var i = 0; i < arr2d.length; i++) {
    var inner = arr2d[i]
    //loop over the inner array
    for (var y = 0; inner.length; y++) {
        console.log(arr2d[i][y])

    }

}


// Flatten Array
// Given a 2 dimensional array (an array containing 
//arrays), return a new array containing just the 
//values from inside the sub-arrays. Don't assume 
//the array will always be the same size, or that 
//the sub-arrays are all the same length (the array 
//might be jagged). Don't use built-in methods like 
//Array.prototype.flat() but feel free to use 
//.push(value) and/or .pop() where needed.
*/
// complete the following function
function flatten(arr2d) {
    var flat = [];
    for (var i = 0; i < arr2d.length; i++) {
        var inner = arr2d[i]
        //loop over the inner array
        for (var y = 0; y < inner.length; y++) {
            var numbertoadd = (arr2d[i][y])
            flat.push(numbertoadd)
        }
    
    }// your code here

    return flat;
}

var result = flatten([[2, 5, 8], [3, 6, 1], [5, 7, 7]]);
console.log(result); // we expect to get back [2, 5, 8, 3, 6, 1, 5, 7, 7]