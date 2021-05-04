# https://github.com/Automedon/CodeWars-7-kyu-Soluitions/blob/master/Easy%20wallpaper

function wallpaper([double]$l, [double]$w, [double]$h)
{
    $numbers = @('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')

    if ($l * $h * $w -eq 0) {
        Write-Output $numbers[0]
    }

    else {
        Write-Output $numbers[[Math]::ceiling(($l * $h * 2 + $w * $h * 2) * 1.15 / 5.2)]
    }
}