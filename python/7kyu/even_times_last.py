# https://www.codewars.com/kata/5a1a9e5032b8b98477000004/train/python


def even_last(numbers): 
    
    if numbers == []:
        return 0

    res = 0
    
    for i in range(0,len(numbers),2):
        res += numbers[i]
    
    res = res * numbers[-1]
    return res

even_last([2, 3, 4, 5])



"""
* clever

def even_last(numbers): 
    return sum(numbers[::2]) * numbers[-1] if numbers else 0

"""
