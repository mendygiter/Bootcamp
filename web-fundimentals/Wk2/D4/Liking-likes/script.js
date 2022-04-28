// var count = 3;
// var countElement = document.querySelectorAll("#count")

// console.log(countElement);

// function add1() {
//     count++;
//     countElement.innerText = count + " Like(s)";
//     console.log(count);
// }

var likes = [3,3,3]
var query = [
    document.querySelector("#count1"),
    document.querySelector("#count2"),
    document.querySelector("#count3"),
]
function add1 (i) {
    likes[i]++
    query[i].innerText = likes[i] + " likes(s)";
}
