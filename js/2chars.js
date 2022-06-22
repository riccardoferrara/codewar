function solution(str){
   str.length % 2 != 0? str += '_':str
   out = []
   for (let i = 0; i < str.length; i += 2) {
       out.push(str[i] + str[i+1])
   }
   return out
}






str = 'abc' //=>  ['ab', 'c_']
console.log(solution(str))

str = 'abcdef' //=> ['ab', 'cd', 'ef']
console.log(solution(str))

str = 'abcdefg' //=> ['ab', 'cd', 'ef']
console.log(solution(str))