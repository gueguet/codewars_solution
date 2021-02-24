# https://www.codewars.com/kata/5656b6906de340bd1b0000ac/train/powershell

function longest($a1, $a2)
{
  $res = ""

  for($i = 0; $i -lt $a1.length; $i++)
  { 
    $res = $res + $a1[$i]
  }

  for($i = 0; $i -lt $a2.length; $i++)
  { 
    $res = $res + $a2[$i]
  }

  $res = $res.ToCharArray() | Sort-Object -Unique
  $final_res = New-Object System.String ($res,0,$res.Length)
  Write-Output $final_res
}

longest "aretheyhere" "yestheyarehere" 

<#
* Clever solutions *
( [char[]]$a1 + [char[]]$a2 | Sort-Object -Unique ) -join ''
#>