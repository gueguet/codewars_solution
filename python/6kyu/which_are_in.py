# https://www.codewars.com/kata/550554fd08b86f84fe000a58/train/python

def in_array(array1, array2):

  substring_arr = []

  for el_arr1 in array1:
    for el_arr2 in array2:
      if el_arr1 in el_arr2:
        substring_arr.append(el_arr1)

  return sorted(list(set(substring_arr)))


a1 = ["arp", "mice", "bull"] 
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

in_array(a1,a2)


"""
* clever

def in_array(a1, a2):
    return sorted({sub for sub in a1 if any(sub in s for s in a2)})

could also have define a set at the very beginning instead of a list
"""