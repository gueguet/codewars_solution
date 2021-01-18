# https://www.codewars.com/kata/5715eaedb436cf5606000381/train/powershell

function Get-SumOfPositive($NumberArray)
{
  $sum = 0

  foreach ($element in $NumberArray) {
    if ($element -gt 0) {
      $sum = $sum + $element
    }
  }
  Write-Output($sum)
}


$test = @(1, 2, 3, 4, 5)
Get-SumOfPositive $test