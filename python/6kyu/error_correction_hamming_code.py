# https://www.codewars.com/kata/5ef9ca8b76be6d001d5e1c3e/train/python

get_bin = lambda x: format(x, 'b').zfill(8)

def encode(string):
  
  encoded_res = []
  
  ascii_res = [ord(i) for i in string]
  bin_res = [get_bin(ascii_val) for ascii_val in ascii_res] 

  print(bin_res)

  # triple
  for str_bin in bin_res:
    for s in str_bin:
      encoded_res.append(s*3)

  encoded_res = "".join(encoded_res)
  return encoded_res


def decode(bits):
  splited_array = [bits[i:i+3] for i in range(0,len(bits),3)]
  corrected_bits = []

  for sample_bit in splited_array:
    if (sample_bit.count("1") > sample_bit.count("0")):
      corrected_bits.append("1")
    else:
      corrected_bits.append("0")

  
  ascii_res = ["".join(corrected_bits[i:i+8]) for i in range(0,len(corrected_bits),8)] 
  print(ascii_res)

  string_res = [chr(int(ascii_val,2)) for ascii_val in ascii_res]
  return "".join(string_res)
