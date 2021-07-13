# https://www.codewars.com/kata/5300901726d12b80e8000498/train/python

def fizzbuzz(n):
  
  my_list = [i for i in range(1,n+1)]

  for i in range(len(my_list)):

    if (my_list[i] % 3 == 0 and my_list[i] % 5 == 0):
      my_list[i] = "FizzBuzz"
      continue

    if (my_list[i] % 3 == 0):
      my_list[i] = "Fizz"
      continue

    if (my_list[i] % 5 == 0):
      my_list[i] = "Buzz"
      continue
  
  return my_list

fizzbuzz(10)


"""
* clever

def fizzify(n):
    if n % 15 == 0: return "FizzBuzz"
    if n % 5 == 0: return "Buzz"
    if n % 3 == 0: return "Fizz"
    return n

def fizzbuzz(n):
    return map(fizzify, range(1,n+1))


-------------------------------------


def fizzbuzz(n):
    return ['Fizz'*(not i%3) + 'Buzz'*(not i%5) or i for i in range(1, n+1)]
"""
