// https://www.codewars.com/kata/59377c53e66267c8f6000027/train/javascript

function alphabetWar(fight)
{
  let leftDict = {"w": 4, "p": 3, "b": 2, "s": 1};
  let rigthDict = {"m": 4, "q": 3, "d": 2, "z": 1};

  let leftScore = 0;
  let rightScore = 0;

  // could have use fight.split('')
  // or : for char in fight 
  Array.from(fight).forEach((char) => {
    if (char in leftDict) {
      leftScore += leftDict[char]
    }
    if (char in rigthDict) {
      rightScore += rigthDict[char]
    }
  });


  if (leftScore > rightScore) {
    return "Left side wins!"
  }
  if (rightScore > leftScore) {
    return "Right side wins!"
  }
  return "Let's fight again!";
}
