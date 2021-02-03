# https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python

def pig_it(text):

  word_list = text.split(" ")
  res = ""

  for word in word_list:
    if (word in ["?","!"]):
      res += " " + word
    else:
      res += " " + word[1::] + word[0] + "ay"

  return(res[1::])








pig_it('Pig latin is cool')
# igPay atinlay siay oolcay