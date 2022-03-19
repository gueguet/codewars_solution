# https://www.codewars.com/kata/583203e6eb35d7980400002a/train/python

def count_smileys(arr):

    count_smiley = 0

    for smiley in arr:
        
        if len(smiley) == 2:
            if (smiley[0] in [";",":"]) and smiley[1] in ["D",")"]:
                count_smiley += 1
        
        elif len(smiley) == 3:
            if (smiley[0] in [";",":"]) and smiley[-1] in ["D",")"]:
                if (smiley[1] in ["-","~"]):
                    count_smiley += 1
                    
    return count_smiley
    
    

# * clever

from re import findall
def count_smileys(arr):
    return len(findall(r"[:;][-~]?[)D]", " ".join(arr)))



count_smileys([':D',':~)',';~D',':)'])
