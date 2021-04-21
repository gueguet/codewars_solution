# https://www.codewars.com/kata/56a5d994ac971f1ac500003e/train/powershell

function LongestConsec([string[]] $strarr, [int]$k) 
{

  $longest_concatenate = 0


  for($i = 0; $i -lt $strarr.length-1-$k; $i++)
  {

    $current_concatenate = ""
    
    for($j = 0; $j -lt $k; $j++) {
      $current_concatenate = $current_concatenate + $strarr[$j].length
    }

    if ($current_concatenate -gt $longest_concatenate) {

      Write-Output "yessss"

      $res = ""
      $longest_concatenate = $current_concatenate
      Write-Output $res
      $res = $strarr[$i] + $strarr[$i+1]
      for($j = 0; $j -lt $k; $j++) {
        Write-Output $strarr[$j]
        $res = $res + $strarr[$j]
      }
    }

  }

  Write-Output $res
  # return $res
}




LongestConsec ("zone", "abigail", "theta", "form", "libe", "zas") 2
# LongestConsec ("ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh") 1