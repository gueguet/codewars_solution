# https://www.codewars.com/kata/5efae11e2d12df00331f91a6/train/powershell

# ! first solutio not working because I created md5 and utf8 object in the loop... timeout!


# function md5Hash($pin) {
#     $md5 = new-object -TypeName System.Security.Cryptography.MD5CryptoServiceProvider
#     $utf8 = new-object -TypeName System.Text.UTF8Encoding
#     $hash = [System.BitConverter]::ToString($md5.ComputeHash($utf8.GetBytes($pin)))
#     return $hash.ToLower() -replace '-', ''
#     # ([System.BitConverter]::ToString((New-Object -TypeName System.Security.Cryptography.MD5CryptoServiceProvider).ComputeHash((New-Object -TypeName System.Text.UTF8Encoding).GetBytes($pin)))).Replace("-","")
# }

# function crack($hash) {
#     for ($i = 0; $i -lt 99999; $i++) {    
#         $pin = "{0:00000}" -f $i
#         $calculatedHash = md5Hash($pin).ToLower()
#         if ($calculatedHash -eq $hash) {
#             return $pin
#         }
#     }
# }


# ! good solution


function crack($hash) {

    $md5 = new-object -TypeName System.Security.Cryptography.MD5CryptoServiceProvider
    $utf8 = new-object -TypeName System.Text.UTF8Encoding
    
    for ($i = 0; $i -lt 99999; $i++) {    
        $pin = "{0:00000}" -f $i
        $calculatedHash = [System.BitConverter]::ToString($md5.ComputeHash($utf8.GetBytes($pin))).ToLower() -replace '-', ''
        if ($calculatedHash -eq $hash) {
            return $pin
        }
    }
}



# crack("86aa400b65433b608a9db30070ec60cd")
# crack("827ccb0eea8a706c4c34a16891f84e7b")
crack("3b4212acba5516490217ce1ba7ea5f8c")
