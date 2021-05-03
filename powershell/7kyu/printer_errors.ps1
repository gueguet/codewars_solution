# https://www.codewars.com/kata/56541980fa08ab47a0000040/train/python

function printer-error($s)
{
  $possible_letters = @("abcdefghijklm")
  $nb_err = 0

  for ($i = 0; $i -lt $s.length; $i++) {
 
    if ($possible_letters.ToCharArray() -contains $s[$i]) {
    } else {
      $nb_err = $nb_err + 1 
    }
    
  }
  
  $string_length = $s.length
  Write-Output "$nb_err/$string_length"

}

printer-error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz")


<# * * Way better :
function printer-error($s) {
  $errors = ($s.ToCharArray() -gt 'm').length
  return "$errors/$($s.length)"
#>