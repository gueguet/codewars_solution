# https://www.codewars.com/kata/5d2d0d34bceae80027bffddb/train/python

vowels = "aeiouAEIOU"

def num_of_contiguous(my_string):
  count = 0
  max_count = 0
  for char in my_string:
    if char in vowels:
      count += 1
      if (count >= max_count):
        max_count = count
    else:
      count = 0
  return max_count

def sort_strings_by_vowels(seq):
  seq.sort(key=num_of_contiguous, reverse=True)
  return seq



sort_strings_by_vowels(["high","day","boot"])


"""
* clever 

def sort_strings_by_vowels(seq): 
    return sorted(seq, reverse=True, key=lambda x: max((len(i) for i in re.findall(r'[aeiouAEIOU]+', x)), default=0))
"""