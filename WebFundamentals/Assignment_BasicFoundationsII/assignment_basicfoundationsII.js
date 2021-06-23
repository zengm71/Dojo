// 1. biggie size
function biggieSize(array) {
    for (let index = 0; index < array.length; index++) {
        if(array[index] > 0){
            array[index] = 'big'
        }
    }    
    return(array)
}
console.log(biggieSize([-1,3,5,-5]))

// 2. printlow return high
function printLowReturnHigh(array) {
    min = array[0]
    max = array[0]
    for (let index = 0; index < array.length; index++) {
        if (array[index] < min) {
            min = array[index]
        }        
        if (array[index] > max) {
            max = array[index]
        }       
    }
    console.log(min)
    return(max)
}
console.log(printLowReturnHigh([1,2,3]))

// 3. print one return another
function printOneReturnAnother(array) {
    if (array.length < 2) {
        console.log('Array length less than 2')
    } else {
        console.log(array[array.length - 2])
    }
    for (let index = 0; index < array.length; index++) {
        if(array[index] % 2 == 1){
            firstOdd = array[index]
            break
        }        
    }
    if (typeof firstOdd === 'undefined'){
        console.log('No odd number')
    } else {
        return(firstOdd)
    }
}
console.log(printOneReturnAnother([2,1,4,6]))

// 4 double vision
function doubleVision(array) {
    for (let index = 0; index < array.length; index++) {
        array[index] = array[index] * 2        
    }
    return(array)
}
console.log(doubleVision([1,2,3]))

// 5 count positives
function countPositives(array) {
    var n = 0
    for (let index = 0; index < array.length; index++) {
        if(array[index] > 0){
            n++
        }
    }    
    array[array.length-1] = n
    return(array)
}
console.log(countPositives([-1,1,1,1]))

// 6 evens and odds
function evensAndOdds(array) {
    if (array.length < 3){
        console.log("Array not long enough")
    } else {
        for (let index = 2; index < array.length; index++) {
            var lastThree = [array[index-2]%2, array[index-1]%2, array[index]%2]
            if (lastThree[0] == 0 & lastThree[1] == 0 & lastThree[2] == 0){
                console.log('Even more so')
            } 
            if (lastThree[0] == 1 & lastThree[1] == 1 & lastThree[2] == 1){
                console.log("That's odd")
            }
        }
    }
}
console.log(evensAndOdds([1,11,1,2,2,2,2]))

// 7 increment the seconds
function incrementSecond(array) {
    for (let index = 0; index < array.length; index ++) {
        if(index % 2 == 1){
            array[index] = array[index] + 1
        }
        console.log(array[index])
    }
    return(array)
}
console.log(incrementSecond([1,2,2,3,4,4,5]))

// 8 previous lengths
function previousLengths(array) {
    for (let index = array.length - 1; index > 0; index--){
        array[index] = array[index -1].length       
    }
    return(array)
}
console.log(previousLengths(["hello", "dojo", "yoyoy"]))

// 9 add seven
function addSeven(array) {
    var newArrary = [array[0] + 7]
    for (let index = 1; index < array.length; index++){
        newArrary[index] = array[index] + 7
    }
    return(newArrary)
}
console.log(addSeven([1,2,3,4]))

// 10 reverse aarray
function reverseArray(array) {
    for (let index = 0; index < Math.floor(array.length/2); index++) {
        swap = array[index]
        array[index] = array[array.length - 1 - index]
        array[array.length - 1 - index] = swap
    }
    return(array)
}
console.log(reverseArray([1,2,3,4,5]))

// 11 outlook negative
function outlookNegative(array) {
    var newArrary = []
    for (let index = 0; index < array.length; index++) {
        if(array[index] > 0){
            newArrary.push(-array[index])
        } else {
            newArrary.push(array[index])
        }
    }
    return(newArrary)
}
console.log(outlookNegative([1,-3,4]))

// 12 always hungry
function alwaysHungry(array) {
    var nFood = 0
    for (let index = 0; index < array.length; index++) {
        if(array[index] == 'food'){
            console.log('yummy')
            nFood ++
        } 
    }    
    if (nFood == 0) {
        console.log("I'm hungry")
    }
}
console.log(alwaysHungry(['food','good','hood', 'food']))

// 13 swap toward center
function swapTowardsCenter(array) {
    for (let index = 0; index < Math.floor(array.length/2); index++) {
        if (index % 2 == 0) {
            swap = array[index]
            array[index] = array[array.length - 1 - index]
            array[array.length - 1 - index] = swap
        }
    }
    return(array)
}
console.log(swapTowardsCenter([true,42,"Ada",2,"pizza"]))
console.log(swapTowardsCenter([1,2,3,4,5,6]))

// 14 scale the array
function scaleArray(arr, num) {
    for (let index = 0; index < arr.length; index++) {
        arr[index] = arr[index] * num        
    }
    return(arr)
}
console.log(scaleArray([1,2,3], 3))
