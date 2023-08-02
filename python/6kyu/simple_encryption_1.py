# https://www.codewars.com/kata/57814d79a56c88e3e0000786/train/python

def encrypt(text, n):
    if (text == None):
        return None
    
    for _ in range(n):
        even_values = [val for idx,val in enumerate(text) if idx % 2 == 0]
        odd_values = [val for idx,val in enumerate(text) if idx % 2 != 0]
        text = odd_values + even_values
    return "".join(text)

def decrypt(encrypted_text, n):
    if (encrypted_text == None):
        return None

    text_lenght = len(encrypted_text)
    half = len(encrypted_text) // 2
    for _ in range(n):
        odd_values = [val for val in encrypted_text[0:half]]
        even_values = [val for val in encrypted_text[half::]]
        encrypted_text = []
        for o,e in zip(odd_values, even_values): # ! I would like to tell zip command go at the "end" of each list, whatever the cases
            encrypted_text.append(e)
            encrypted_text.append(o)
        if (text_lenght % 2 == 1): # ! ugly
            encrypted_text.append(even_values[-1])
    return "".join(encrypted_text)

# print(encrypt("This is a test!", 1))
print(decrypt("hskt svr neetn!Ti aai eyitrsig", 1))



"""
* Clever

def decrypt(text, n):
    if text in ("", None):
        return text
    
    ndx = len(text) // 2

    for i in range(n):
        a = text[:ndx]
        b = text[ndx:]
        text = "".join(b[i:i+1] + a[i:i+1] for i in range(ndx + 1))
    return text
    
    
def encrypt(text, n):
    for i in range(n):
        text = text[1::2] + text[::2] # * 
    return text

"""