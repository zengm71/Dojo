// get 1 to 255
function get1to255() {
    return(Array.from(Array(255), (_, i) => i + 1))
}
console.log(get1to255())

// get even 1000
function geteven1000() {
    var s = 0
    for (var i = 1; i <= 1000; i++){
        if(i % 2 == 0){
            s = s + i
        }
    }
    return(s)
}
console.log(geteven1000())

// sum odd 5000
function getodd5000() {
    var s = 0
    for (var i = 1; i <= 5000; i++){
        if(i % 2 == 1){
            s = s + i
        }
    }
    return(s)
}
console.log(getodd5000())

// Iterate an array
function iterateArray(arr){
    var s = 0
    for (index = 0; index < arr.length; index++) {
        s = s + arr[index];
    }
    return(s)
}
console.log(iterateArray([1,2,3]))

// find max
function findMax(arr){
    var m = 0   
    for(index = 0; index < arr.length; index++){
        if(m < arr[index]){
            m = arr[index]
        }
    }
    return(m)
}
console.log(findMax([-3,3,5,7]))

// find average
function findAverage(arr){
    var avg = 0
    for(index = 0; index < arr.length; index++){
        avg = avg + arr[index]
    }
    return(avg/index)
}
console.log(findAverage([1,3,5,7,20]))

// array odd
function arrayOdd(){
    var arr = []
    for(index = 1; index <= 50; index++){
        if(index % 2 == 1){
            arr.push(index)
        }
    }
    return(arr)
}
console.log(arrayOdd())

// 8. greater than y
function greaterThanY(arr, Y){
    var n = 0
    for(index = 0; index <= arr.length; index++){
        if(arr[index] > Y){
            n++
        }
    }
    return(n)
}
console.log(greaterThanY([1,3,5,7],3))

// 9 squares
function squares(arr){
    for(index = 0; index < arr.length; index++){
        arr[index] = arr[index] * arr[index]
    }
    return(arr)
}
console.log(squares([1,5,10,-2]))

// negatives
function negatives(array) {
    for (let index = 0; index < array.length; index++) {
        if (array[index] < 0) {
            array[index] = 0
        }
    }
    return(array)
}
console.log(negatives([1,5,10,-2]))

// max/min/avg
function maxMinAvg(array) {
    max = array[0]
    min = array[0]
    avg = 0
    for (var index = 0; index < array.length; index++) {
        if (array[index] > max) {
            max = array[index]
        }
        if (array[index] < min) {
            min = array[index]
        }
        avg = avg + array[index]
    }
    avg = avg/index
    return([max, min, avg])   
}
console.log(maxMinAvg([1,5,10,2]))

// swap value
function swapFunction(array) {
    first = array[0]
    array[0] = array[array.length-1]
    array[array.length-1] = first
    return(array)
}
console.log(swapFunction([1,5,10,-2]))

// number to string
function numberToString(array){
    for (let index = 0; index < array.length; index++) {
        if (array[index] < 0) {
            array[index] = 'Dojo'
        }
    }
    return(array)
}
console.log(numberToString([-1,-3,2]))