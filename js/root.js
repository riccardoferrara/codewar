function digital_root(n) {
  while (n.toString().length > 1){
    n = n.toString().split('').map(e => Number(e)).reduce((a,b)=>a+b)
  }
  return n
}


n = 16 // 2
console.log(digital_root(456))