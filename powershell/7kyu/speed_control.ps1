# https://www.codewars.com/kata/56484848ba95170a8000004d/train/powershell

function get-gps($s, $x) 
{

  $all_time_array = @()
  
  for($i = 0; $i -lt $x.length-1; $i++)
  { 
    $speed = 3600*($x[$i+1]-$x[$i])/$s
    $all_time_array += $speed
  }

  Write-Output ($all_time_array | Measure -Max).Maximum

}



$x = 0.0, 0.19, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25

get-gps 15 $x