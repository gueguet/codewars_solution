# https://www.codewars.com/kata/5848565e273af816fb000449/train/python

def encrypt_this(text):
    if text == "":
        return ""
    res = ""
    
    for word in text.split(" "):
        if (len(word) == 1):
            res += str(ord(word[0])) + " "
        elif (len(word) == 2):
            res += str(ord(word[0])) + word[-1] + word[2:-1] + " "
        else:
            res += str(ord(word[0])) + word[-1] + word[2:-1] + word[1] + " "
            
    return res[:-1]
    

print(encrypt_this("A wise old owl lived in an oak"))


"""
* clever

def swapper(w):
    return w if len(w)<2 else w[-1] + w[1:-1] + w[0]

def encrypt_this(s):
    return ' '.join(w if not w else str(ord(w[0])) + swapper(w[1:]) for w in s.split())
    

-----------------------------------------------------------------------------

def encrypt_this(text):
    result = []
    
    for word in text.split():
        # turn word into a list
        word = list(word)
        
        # replace first letter with ascii code
        word[0] = str(ord(word[0]))
        
        # switch 2nd and last letters
        if len(word) > 2:
            word[1], word[-1] = word[-1], word[1]
        
        # add to results
        result.append(''.join(word))
    
    return ' '.join(result)


"""
