function arrayDiff(a, b) {
  b.forEach((e,i) => {
      if (a.includes(e)) {
        removeItemAll(a, e)
      }
    });
    return a
}


a = [1,2,2,2,3]
b = [1]

arrayDiff(a,b)
console.log(a)