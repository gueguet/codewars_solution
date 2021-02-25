# https://www.codewars.com/kata/525f47c79f2f25a4db000025/train/powershell

function Get-PhoneNumberValidation([String]$PhoneNumber)
{
  $PhoneNumber -match '^\([0-9]{3,}\) [0-9]{3}-[0-9]{4,}$'
}

Get-PhoneNumberValidation "(123) 456-7890"
Get-PhoneNumberValidation "(1111)5X5 2345"

<# 
* Clever Solution

You could use d instead of [0-9]
$PhoneNumber -match '^\(\d{3}\) \d{3}-\d{4}$'
#>