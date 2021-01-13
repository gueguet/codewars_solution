# https://www.codewars.com/kata/5545f109004975ea66000086/train/powershell

function IsDivisible([int] $n, [int] $x, [int] $y) {
  If($n % $x -eq 0 -and $n % $y -eq 0){
    Write-Output($true)
  }
  else {
    Write-Output($false)
  }
}

IsDivisible -10 -2 -2


# in one line 
# return ($n % $x + $n % $y -eq 0)