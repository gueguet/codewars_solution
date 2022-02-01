# https://www.codewars.com/kata/5828713ed04efde70e000346/train/python

from collections import Counter

def count_languages(lst): 
  language_counter = Counter()
  
  for row in lst:
    language_counter[row['language']] += 1
    
  return language_counter
  
  
list1 = [
          { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'C' },
          { 'firstName': 'Anna', 'lastName': 'R.', 'country': 'Liechtenstein', 'continent': 'Europe', 'age': 52, 'language': 'JavaScript' },
          { 'firstName': 'Ramon', 'lastName': 'R.', 'country': 'Paraguay', 'continent': 'Americas', 'age': 29, 'language': 'Ruby' },
          { 'firstName': 'George', 'lastName': 'B.', 'country': 'England', 'continent': 'Europe', 'age': 81, 'language': 'C' },
        ]   


count_languages(list1)


"""
* clever

from collections import Counter
def count_languages(lst): 
    return Counter([d['language'] for d in lst])
"""
