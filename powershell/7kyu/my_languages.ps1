# https://www.codewars.com/kata/5b16490986b6d336c900007d/train/powershell
# help : https://stackoverflow.com/questions/9015138/looping-through-a-hash-or-using-an-array-in-powershell


function My-Languages ([hashtable] $results) {

    if ($results.Count -eq 0) {
        return @()
    }
        
    $sorted_res = $results.GetEnumerator() | Sort-Object -property:Value -Descending
    $res = [System.Collections.ArrayList]@()

    foreach ($lang in $sorted_res) {
        if ($lang.Value -ge 60) {
            $res = $res + $lang.Name
            # Write-Host $lang.Name.GetType() --> string
        }
    }

    $res
}

My-Languages @{"Java" = 10; "Ruby" = 80; "Python" = 65}
# My-Languages @{}


###
# * clever

function My-Languages ([hashtable] $results) {
    return ($results.GetEnumerator() | Where-Object Value -ge 60 | Sort-Object -Property Value -Descending | Select-Object -ExpandProperty Name)
}
###
