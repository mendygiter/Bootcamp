function bubbleSort(arr) {

    for (var i = 0; i < arr.length - 1; i++) {
        for (var j = 0; j < arr.length - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                var temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
            }
        }
    }
}

var x = [1,3,6,3,7,2,9];
bubbleSort(x)
console.log('after sprt: ${x}');