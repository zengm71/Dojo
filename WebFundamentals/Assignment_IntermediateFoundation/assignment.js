function sigma(num) {
    var s = 0
    for (let index = 1; index <= num; index++){
        s = s + index
    }
    return(s)
}
console.log("Sigma ", sigma(3))

function factorial(num) {
    var f = 1
    for (let index = 1; index <= num; index++){
        f = f * index
    }
    return(f)
}
console.log("Factorial ", factorial(5))

function fibonacci(num) {
    var f = 0
    if (num <=1) {
        f = num
    } else{
        f = fibonacci(num - 1) + fibonacci(num - 2)
    }

    return(f)
}
console.log("Fibonacci ", fibonacci(7))

function second2last(array) {
    if (array.length < 2) {
        return null
    } else {
        return array[array.length - 2]
    }
}
console.log("Second to last", second2last([42, true, 4, "Liam", 7]))

function nth2last(array, n) {
    if (array.length < n) {
        return null
    } else {
        return array[array.length - n]
    }
}
console.log("nTh to last", nth2last([5,2,3,6,4,9,7],3))

function secondLargest(array){
    if (array.length < 2) {
        return null
    } else {
        if (array[0] < array[1]) {
            s = array[0]
            f = array[1]
        } else {
            s = array[1]
            f = array[0]
        }
        for (let index = 2; index < array.length; index++) {
            if(array[index] > f){
                s = f
                f = array[index]
            } else if (array[index] < f & array[index] > s){
                s = array[index]
            }           
        }
    }
    return(s)
}
console.log('Second largest', secondLargest([42,1,4,14,7]))

function doubleTrouble(array){
    var returnArray = []
    for (let index = 0; index < array.length; index++) {
        returnArray.push(array[index])
        returnArray.push(array[index])
    }
    return(returnArray)
}
console.log("Double Trouble", doubleTrouble([4, "Ulysses", 42, false]))