# https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991/train/python

def revrot(strng, sz):
    if (strng == "" or sz > len(strng) or sz == 0):
        return ""

    char_left = len(strng)
    res = ""

    while (char_left >= sz):

        substring = strng[0:sz]
        sum_cube_digit = sum([int(x)**3 for x in substring]) 

        print(sum_cube_digit)

        if (sum_cube_digit % 2 == 0):
            res += substring[::-1]
        else:
            res += substring[1:] + substring[0]

        char_left = char_left - sz
        strng = strng[sz:]

    return(res)


s = "987653"
print(revrot(s, 6))

# 330479108928157


"""
* more elegant

def revrot(s, n, res=""):
    if not s or n < 1 or n > len(s):
        return ""
    
    while len(s) >= n:
        group = s[:n]
        if sum([int(d)**3 for d in group]) % 2 == 0:
            res += group[::-1]
        else:
            res += group[1:] + group[0]
        s = s[n:]
    
    return res


* clever - lambda functions

def revrot(strng, sz):
    func = lambda x : x[1:] + x[0] if sum(int(i) for i in x) % 2 else x[::-1]
    return "" if sz <= 0 or sz > len(strng) else "".join(func(strng[i:i+sz]) for i in xrange(0, len(strng) - sz + 1, sz))

"""