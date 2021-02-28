# https://www.codewars.com/kata/55d24f55d7dd296eb9000030/train/python

function Summation([int] $n) {

  $res = 0
  
  for($i = 1; $i -lt $n+1; $i++)
  { 
    $res = $res + $i
  }

  Write-Output $res
}

Summation 8


<#
* Good to know

return (1..$n | measure-object -sum).sum
#>