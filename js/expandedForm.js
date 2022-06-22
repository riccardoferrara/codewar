function expandedForm(num) {
    return num.toString().split('')
    .map((e, i) => Number(e)*10**(num.toString().length - i - 1))
    .filter(e => e!=0).join(' + ')
}

num = 70304
console.log(expandedForm(num))