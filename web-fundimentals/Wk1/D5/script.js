function fizzBuzz(firstMultiplier, secondMultiplier) {
    let returnMultiplier ;
    for(let i = 1; i<=100; i++) {
        if(i%firstMultiplier==0 && i%secondMultiplier==0) {
            returnMultiplier += "FizzBuzz ";
        }
        else if (i%firstMultiplier==0){
            returnMultiplier += "Fizz ";
        }
        else if (i%secondMultiplier == 0) {
            returnMultiplier += "Buzz ";
        }
        else returnMultiplier += i + " ";
        console.log(i);
    }
}