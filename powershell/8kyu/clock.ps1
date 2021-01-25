# https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a/powershell

function Past([int] $h, [int] $m, [int] $s) {
  return ($h * 60*60 * 1000 + $m * 60 * 1000 + $s * 1000)
}