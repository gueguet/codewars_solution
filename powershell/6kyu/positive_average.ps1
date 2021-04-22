# https://www.codewars.com/kata/59f4a0acbee84576800000af/train/powershell

function pos-average($s) 
{

  $total_char = 0
  $common_char = 0
  $split_array = $s.split(", ")

  for ($i = 0; $i -lt $split_array.length; $i++) {

    $total_char += $split_array[$i].Length

    for ($j = $i+1; $j -lt $split_array.length; $j++) {

      for ($k = 0; $k -lt $split_array[$j].Length; $k ++) {
        if ($split_array[$i][$k] -eq $split_array[$j][$k]) {
          $common_char += 1
          Write-Output "Same $($split_array[$i]) - $($split_array[$j])"
          Write-Output $split_array[$i][$k]
        }
      }

      Write-Output "--------------------------"
      Write-Output "Yosh"


    }

  }

  $res = ($common_char/$total_char)*100
  Write-Output $common_char
  Write-Output $total_char

}



# pos-average "6900690040, 4690606946, 9990494604"
pos-average "466960, 069060, 494940, 060069, 060090, 640009, 496464, 606900, 004000, 944096"
