# https://www.codewars.com/kata/563b662a59afc2b5120000c6/train/powershell

function nb-year([int]$p0, [double]$percent, [int]$aug, [int]$p)
{

  $n = 0
  
  while ($p0 -lt $p)
  {
    $p0 = ($p0 + ($percent/100) * $p0) + $aug
    $n = $n + 1
  }

  Write-Output $n
  
}

nb-year 1500 5 100 5000