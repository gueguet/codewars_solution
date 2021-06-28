# https://www.codewars.com/kata/5816b76988ca9613cc00024f

def sort_sequence(sequence):
  
  splited_arrays = []

  sub_array = []
  for num in sequence:
    if (num != 0):
      sub_array.append(num)
    else:
      sub_array = sorted(sub_array)
      sub_array.append(num)
      splited_arrays.append(sub_array)
      sub_array = []

  final_list = [] 
  
  for sub_list in sorted(splited_arrays,key=sum):
    for el in sub_list:
      final_list.append(el)

  return final_list


a = [3, 2, 1, 0, 5, 6, 4, 0, 1, 5, 3, 0, 4, 2, 8, 0]
sort_sequence(a)


"""
* clever

from itertools import groupby
def sort_sequence(sequence):
    return sum(sorted([sorted(y)+[0] for x,y in groupby(sequence, lambda x: x==0) if not x],key=sum),[])
"""
