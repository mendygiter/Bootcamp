// Generating a random number
for(var i=0; i<10; i++) {
    var random = Math.floor(Math.random() * 11) + 1;
    console.log(random);
}
var random = Math.floor(Math.random() * 11) + 1;
// add + 1 to make it 1-12 you would add + 1 or to make it 1-10 you would just say * 10 + 1 and then the math.floor function would round down

Math.ceil(9.51)
Math.ceil(9.1)

Math.floor(8.45)
Math.floor(8.99)

//Generating a random number
for(var i =0;i<10;i++){

    var random = Math.floor(Math.random() * 10 + 1) ;
    console.log(random)

}

// Dice Roller
// Using what we've learned about the Math library in JavaScript, complete the following function that should return a value between 1 through 6 at random.

function d6() {
//This is the function^
    var roll = Math.floor(Math.random() * 6 +1);
    return roll;
}
    
var playerRoll = d6();
console.log("The player rolled: " + playerRoll);
//We call the function


// Consult the Oracle
// Using the following array, write a function that will answer all of our questions by randomly choosing a response

var lifesAnswers = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes – definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
];

var result = lifesAnswers[Math.floor(Math.random() * lifesAnswers.length)];
console.log(result);
