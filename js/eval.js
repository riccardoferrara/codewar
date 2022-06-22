function zero(f) {
    return numFunct(0, f)
}
function one(f) {
    return numFunct(1, f)
}
function two(f) {
    return numFunct(2, f)
}
function three(f) {
    return numFunct(3, f)
}
function four(f) {
    return numFunct(4, f)
}
function five(f) {
    return numFunct(5, f)
}
function six(f) {
    return numFunct(6, f)
}
function seven(f) {
    return numFunct(7, f)
}
function eight(f) {
    return numFunct(8, f)
}
function nine(f) {
    return numFunct(9, f)
}

function numFunct(n, f){
    if(f == undefined){
        res = n
    } else {
        f+=n
        res = eval(f.split('').reverse().join(''))
    }
    return Math.floor(res)
}

function plus(a) {return a+='+'}
function minus(a) {return a+='-'}
function times(a) {return a+='*'}
function dividedBy(a) {return a+='/'}

// console.log(two(times(one())))
console.log(eight(minus(three())))

