function validBraces(braces){
    let l_start = braces.length
    let l_end = 0
    while (l_start != l_end){
        l_start = braces.length
        braces = braces.toString().replace("[]","")
        braces = braces.toString().replace("()","")
        braces = braces.toString().replace("{}","")
        l_end = braces.length
    }
    if (braces.length == 0) {
        return true
    } else {
        return false
    }
  }


  console.log(validBraces("()))"))