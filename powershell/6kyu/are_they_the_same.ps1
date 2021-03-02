# https://www.codewars.com/kata/550498447451fbbd7600041c/train/powershell

function comp($a1, $a2)
{
  
  if ($a1.Length -ne $a2.Length) {
    return $false
  }

  if ($a1.Length -eq $null) {
    return $false
  }

  if ($a2.Length -eq $null) {
    return $false
  }

  for ($i = 0; $i -lt $a1.Length; $i++) 
  {
    $a1[$i] = [math]::Abs($a1[$i])
  }

  $a1 = $a1 | Sort-Object
  $a2 = $a2 | Sort-Object

  for ($i = 0; $i -lt $a1.Length; $i++) 
  {
    if ([math]::Pow($a1[$i],2) -ne $a2[$i])
    {
      return $false
    }    
  }
  return $true
}


$a1 =  121, 144, 19, 161, 19, 144, 19, 11 
$a2 =  14641, 20736, 361, 25921, 361, 20736, 361, 121 
comp $a1 $a2
  


<#
* Wow clever

function comp($a1, $a2)
{
  -not (compare-object  @($a1 | % {$_*$_}) $a2)
}

function comp($a1, $a2)
{
    if( (-not $a1) -or (-not $a2)) { $false ; break }   
    $a = @()
    foreach ($i in $a1) { $a += $i*$i }
    (($a | Sort-Object) -join ' ') -eq (($a2|Sort-Object) -join ' ')
}

#>