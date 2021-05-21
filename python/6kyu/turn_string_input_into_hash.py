# https://www.codewars.com/kata/52180ce6f626d55cf8000071/train/python

def str_to_hash(st): 

  list_string = st.split(", ")
  res_hash = {}

  if st == "":
    return {}

  for el in list_string:

    key,val = el.split("=")

    if (key not in res_hash):
      res_hash[key] = int(val)
    else:
      pass

  return res_hash

str_to_hash("a=1, b=2, c=3, d=4")