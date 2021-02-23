# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039

function accum($s)
{
  $res = ""
  for($i = 0; $i -lt $s.length; $i++)
  { 
    $res = $res + $s.substring($i,1).toupper()
    for($j = 1; $j -lt $i+1; $j++) 
    {
      $res = $res + ($s.substring($i,1).tolower())
    }
    $res = $res + "-"
  }
  Write-Output $res.substring(0,$res.Length-1)
}

accum("ZpglnRxqenU")


# Super clever
# function accum($s) {
#   return ($s.ToCharArray() | ForEach-Object {$count = 1} {$_.ToString() * $count++}) -Join '-'
# }


# Other
# function accum($s)
# {
#     $s = ($s).ToCharArray()
#     $mumble=@()
#     $i = 1
#     foreach ($str in $s){
#         $mumble += (Get-Culture).TextInfo.ToTitleCase($str.ToString() * $i)
#         $i ++
#     }
#     $mumble -join "-"
# }