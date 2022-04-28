//Print odds
var myArray = [];
for (var i = 1; i < 20; i += 2){
    myArray.push(i);
}
console.log(myArray);

//Decreasing Multiples of 3
var myArray = [];
for(var i = 100; i > 0; i-=3) {
    myArray.push(i);
}
console.log(myArray);

//Print the sequence
var arr = [4, 2.5, 1, -0.5, -2, -3.5];
for (var i=0; i < arr.length; i++) {
    console.log(arr[i]);
}

// Sigma
var sum = 0 
for (var i = 1; i <= 100; i++) {
    // sum += i;
    sum = sum + i;
}
console.log(sum);

// Factorial
var product = 1 
for (var i = 1; i <= 12; i++) {
    // sum += i;
    product = product * i;
}
console.log(product);