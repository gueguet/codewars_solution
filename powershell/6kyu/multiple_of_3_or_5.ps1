# https://www.codewars.com/kata/514b92a657cdc65150000006/train/powershell

function Get-SumOfMultiples($Value)
{
  $sum = 0

  for($i = 0; $i -lt $Value; $i++)
  {
    if ($i%3 -eq 0 -or $i%5 -eq 0) {
      $sum = $sum + $i
    }
  }
  $sum
}

Get-SumOfMultiples 10