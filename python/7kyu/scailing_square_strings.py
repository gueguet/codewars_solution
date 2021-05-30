# https://www.codewars.com/kata/56ed20a2c4e5d69155000301/train/python

def scale(strng, k, n):

  if (strng == ""):
    return ""

  splited_string = strng.split("\n")

  list_res = []
  for string in splited_string:
    tmp_res = ""
    for char in string:
      tmp_res += char * k
    list_res.append(tmp_res)

  list_final_res = []
  for el in list_res:
    for i in range(0,n):
      list_final_res.append(el)

  return "\n".join(list_final_res)

a = "abcd\nefgh\nijkl\nmnop"
r = "aabbccdd\naabbccdd\naabbccdd\neeffgghh\neeffgghh\neeffgghh\niijjkkll\niijjkkll\niijjkkll\nmmnnoopp\nmmnnoopp\nmmnnoopp"
scale(a, 2, 3)


"""

* clever

def scale(strng, k, n):
    words = strng.split()
    words_h = ("".join(char * k for char in word) for word in words) 
    return "\n".join("\n".join(word for _ in range(n)) for word in words_h)
"""
