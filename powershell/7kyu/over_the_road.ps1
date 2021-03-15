# https://www.codewars.com/kata/5f0ed36164f2bc00283aed07/train/powershell

function overTheRoad($address, $n) {
    $left_array = @()
    $right_array = @()

    for ($i = 1; $i -lt $n*2+1; $i++) {
        if ($i % 2 -eq 0) {
            $right_array = $right_array + $i
        } else {
            $left_array = $left_array + $i
        }
    }

    $right_array = $right_array | Sort-Object -Descending

    Write-Output $right_array.indexof($address)
    Write-Output $left_array.indexof($address)



    # for ($i = 0; $i -lt $n; $i++) {
    #     if ($left_array[$i] -eq $address) {
    #         return $right_array[$i]
    #     }
    #     if ($right_array[$i] -eq $address) {
    #         return $left_array[$i]
    #     }
    # }
}


overTheRoad 2 3