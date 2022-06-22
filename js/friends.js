//friends.js
function friend(friends){
    return friends.filter(e => e.length == 4)
  }


friends = ["Ryan", "Kieran", "Mark"] //`shouldBe` ["Ryan", "Mark"]
console.log(friend(friends))