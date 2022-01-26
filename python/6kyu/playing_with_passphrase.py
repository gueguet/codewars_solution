# https://www.codewars.com/kata/559536379512a64472000053/train/python


from itertools import cycle

def play_pass(s, n):
    res = ""
    for char in s:
        
        if char.isalnum():
            if char.isnumeric():
                res += str(9 - int(char))
                
            else:
                if (char.islower()):
                    shift_char = chr((ord(char.upper())+n - 65) % 26 + 65).lower()
                else:
                    shift_char = chr((ord(char.upper())+n - 65) % 26 + 65).upper()
                
                res += shift_char.lower()
                    
        else:
            res += char

    final_res = ""
    for i in range(0,len(res)):
        if (i%2 == 0):
            final_res += res[i].upper()
        else:
            final_res += res[i].lower()

    return final_res[::-1]

        
        
play_pass("my GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2)


"""
* clever

def play_pass(s, n):

    # Step 1, 2, 3
    shiftText = ""
    for char in s:
        if char.isdigit():
            shiftText += str(9 - int(char))
        elif char.isalpha():
            shifted = ord(char.lower()) + n
            shiftText += chr(shifted) if shifted <= ord('z') else chr(shifted - 26)
        else:
            shiftText += char

    # Step 4
    caseText = ""
    for i in range(len(shiftText)):
        caseText += shiftText[i].upper() if i % 2 == 0 else shiftText[i].lower()

    # Step 5
    return caseText[::-1]
"""
