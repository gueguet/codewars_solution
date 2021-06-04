# https://www.codewars.com/kata/5282b48bb70058e4c4000fa7/train/python


hex_dict = dict(zip(['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'],[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))

def hex_string_to_RGB(hex_string): 

  hex_string = hex_string[1:].upper()
  red_val = (hex_dict[hex_string[0]] * 16) + hex_dict[hex_string[1]]
  green_val = (hex_dict[hex_string[2]] * 16) + hex_dict[hex_string[3]]
  blue_val = (hex_dict[hex_string[4]] * 16) + hex_dict[hex_string[5]]
  

  return {
    'r': red_val,
    'g': green_val,
    'b': blue_val
  }



hex_string_to_RGB("DA70D6")


"""

* clever

def hex_string_to_RGB(hex_string): 
    # your code here
    r = int(hex_string[1:3], 16)
    g = int(hex_string[3:5], 16)
    b = int(hex_string[5:7], 16)
    
    return {'r': r, 'g': g, 'b': b}

"""

