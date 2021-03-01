# https://www.codewars.com/kata/550527b108b86f700000073f/train/powershell

function iter-pi
{
  [OutputType([string])]
  Param ([double]$epsilon)

  $M_PI = 3.14159265358979323846  

  $denom = 1
  $iter = 0
  $estimated_pi = 0
  $sum = 0

  $diff = [Math]::Abs($estimated_pi-$M_PI)
  
  while($diff -gt $epsilon)
  {
    if ($iter % 2 -eq 0) {
      $sum = $sum + (1/$denom)
    }
    else {
      $sum = $sum - (1/$denom)
    }
    $denom = $denom + 2
    $iter = $iter + 1

    $estimated_pi = 4*$sum
    $diff = [Math]::Abs($estimated_pi-$M_PI)
  }
  
  $estimated_pi = [Math]::Round($estimated_pi, 10)

  Write-Output $estimated_pi
  Write-Output $estimated_pi.Length

  $res = "[$iter, $estimated_pi]"
  Write-Output $res
  # Write-Output $res.getType()
  # Write-Output [$iter"," $estimated_pi]
}

iter-pi 0.1


<#
* Notes

You can have problem with the Round function with some test --> not exactly 10 digit result

Next time check :
.ToString("N10")
Or using substring 
#>