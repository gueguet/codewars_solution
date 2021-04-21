# https://www.codewars.com/kata/56a5d994ac971f1ac500003e/train/powershell

function LongestConsec([string[]] $strarr, [int]$k) 
{

  $longest_concatenate = ""


  for($i = 0; $i -lt $strarr.length-$k+1; $i++)
  {

    $current_concatenate = ""
    
    for($j = $i; $j -lt $i+$k; $j++) {
      $current_concatenate = $current_concatenate + $strarr[$j]
    }

    if ($current_concatenate.Length -gt $longest_concatenate.Length) {
      $longest_concatenate = $current_concatenate
    }
  }

  return $longest_concatenate

}




LongestConsec ("zone", "abigail", "theta", "form", "libe", "zas") 2
# LongestConsec ("ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh") 1