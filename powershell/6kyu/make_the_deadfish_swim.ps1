# https://www.codewars.com/kata/51e0007c1f9378fa810002a9/train/powershell

function Eval-DeadFish {
  param (
      [Parameter(Mandatory)]
      [string]$data
  )

  [long[]] $res = @()

  $value = 0

  foreach ($letter in $data.ToCharArray()) {
    if ($letter -eq "o") {
      $res += $value
    }

    if ($letter -eq "i") {
      $value += 1
    }

    if ($letter -eq "d") {
      $value -= 1
    }

    if ($letter -eq "s") {
      $value = $value * $value
    }
  }

  $res

}


# Eval-DeadFish "ooo"
Eval-DeadFish "ioioio"