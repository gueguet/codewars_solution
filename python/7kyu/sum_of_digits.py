def sum_of_digits(digits): 
  
  res_num = 0
  res_str = ""

  if (isinstance(digits,str)):
    for digit in digits[:-1]:
      res_str += digit + " + "
      res_num += int(digit)
    res_num += int(digits[-1])
    res_str += digits[-1] + " = " + str(res_num)
    return res_str

  if (isinstance(digits,int)):
    digits = str(digits)
    for digit in digits[:-1]:
      res_str += digit + " + "
      res_num += int(digit)
    res_num += int(digits[-1])
    res_str += digits[-1] + " = " + str(res_num)
    return res_str

  return ""


"""
* clever -- wow I relleay like this one

def sum_of_digits(digits): 
    d = str(digits)
    return "" if digits is None else f'{" + ".join(x for x in d)} = {sum(map(int, d))}'
"""
