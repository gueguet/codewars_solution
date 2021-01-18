# https://www.codewars.com/kata/5a2be17aee1aaefe2a000151/train/powershell

function array_plus_array($arr1,$arr2){
  return ($arr1 | Measure-Object -Sum).Sum + ($arr2 | Measure-Object -Sum).Sum
}


