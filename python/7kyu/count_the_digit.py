# https://www.codewars.com/kata/566fc12495810954b1000030/train/python

def nb_dig(n, d):
  all_square = [i*i for i in range (0,n+1)]

  digit_counter = 0

  for num in all_square:
    for char in str(num):
      if char == str(d):
        digit_counter +=1

  print(all_square)
  print(digit_counter)

  return digit_counter



if __name__ == "__main__":
  nb_dig(25, 1)