# https://www.codewars.com/kata/5a2fd38b55519ed98f0000ce/train/python

def multi_table(number):
    
    res = ""
    
    for i in range(1,11):
        res += "{} * {} = {}\n".format(i,number,i*number)
      
    print(res)
    print(res[:-1])


    return res[:-1]

multi_table(5)