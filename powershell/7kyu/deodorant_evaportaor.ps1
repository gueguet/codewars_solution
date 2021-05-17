# https://www.codewars.com/kata/5506b230a11c0aeab3000c1f/train/powershell

function evaporator([double]$content, [double]$evapperday, [double]$threshold) {
  # your code

  $day_count = 0
  $threshold = (($threshold/100) * $content )

  while ($content -gt $threshold) {
    $day_count ++    
    $content = $content - (($evapperday/100) * $content)
  }

  Write-Output $day_count

}


evaporator 10 10 10