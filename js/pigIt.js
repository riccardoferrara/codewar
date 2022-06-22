function pigIt(str){
    var letters = /^[A-Za-z]+$/;
    str = str.split(' ').map(e => {
        if (e.match(letters)) {
            l = e.split('')
            end = l.shift()
            end += 'ay'
            e = l.join('') + end
        }
        return e
    })
    return str.join(' ')
  }




str = 'Pig latin is cool'
console.log(pigIt(str)) // 'igPay atinlay siay oolcay')
