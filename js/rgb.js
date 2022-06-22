function rgb(r, g, b){
  // complete this function
  console.log([r,g,b].join(','))
  return dec2hex(r) + dec2hex(g) + dec2hex(b)
}

function dec2hex(c){
    if (c > 255){
        return 'FF'
    } else if (c < 0){
        return '00'
    } else {
        h = c.toString(16).toUpperCase()
        return h.length == 1 ? '0' + h : h
    }
}

console.log(rgb(300,0,0)) // 'ADFF2F'