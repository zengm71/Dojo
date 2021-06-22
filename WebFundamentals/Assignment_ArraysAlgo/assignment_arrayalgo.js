var testArr = [6,3,5,1,2,4]
var s = 0
for(var i=0; i<testArr.length; i++){
    s = s + testArr[i]
    console.log('Num:', testArr[i], 'Sum:', s)
}

newArr = []
for(var i=0; i<testArr.length; i++){
    newArr.push(testArr[i] * i)
}
console.log(newArr)
