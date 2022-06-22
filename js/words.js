// function order(words){
//     if (words == ""){return ""}
//     words = words.split(' ')
//     let order = words.map(e => e.match(/\d/)[0])
//     let new_words = [...words]
//     words.forEach((e, i) => {
//         new_words[order[i]-1] = e
//     });
//     return new_words.join(' ')
// }

function order(words){
    return words.split(' ').sort((a, b) => a.match(/\d/) - b.match(/\d/) ).join(' ')
}


words = ""
console.log(order(words))


words = "is2 Thi1s T4est 3a" 
console.log(order(words))

words = "4of Fo1r pe6ople g3ood th5e the2"
console.log(order(words))

