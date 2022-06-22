// function isIsogram(str){
//     str = [...str.toLowerCase()]
//     for (let i = 0; i < str.length; i++) {
//             if (str.filter(f => f!=str[i]).length != str.length - 1){
//                 return false
//             }
//         }
//     return true
// }

function isIsogram(str){
    return new Set("Dermatoglyphics".toLowerCase()).size == str.length
}


str = "Dermatoglyphics"
a = isIsogram(str)
console.log(`${str} is an isogram? ${a}`)

str = "moOse"
a = isIsogram("moOse")
console.log(`${str} is an isogram? ${a}`)
