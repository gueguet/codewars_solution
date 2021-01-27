function Convert-StringToCamelCase($String)
{

  $StringSplit = $String -split "[_-]"
  
  $StringRes = $StringSplit[0]

  foreach ($SubString in ($StringSplit | select -skip 1)) {
    if ($SubString -ne "") {
      $StringRes += $SubString.substring(0,1).toupper() + $SubString.substring(1)
    }
  }

  $StringRes
}

Convert-StringToCamelCase("the_Cat-was_Hungry")

# problem because of testing in powershell...
# https://www.codewars.com/kata/517abf86da9663f1d2000003/discuss#label-issue