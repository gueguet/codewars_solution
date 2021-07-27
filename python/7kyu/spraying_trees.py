# https://www.codewars.com/kata/5981a139f5471fd1b2000071/train/python

def task(w,n,c):
  name_dict = {
    "Monday": "James",
    "Tuesday": "John",
    "Wednesday": "Robert",
    "Thursday": "Michael",
    "Friday": "William"
  }
  return 'It is {} today, {}, you have to work, you must spray {} trees and you need {} dollars to buy liquid'.format(w,name_dict[w],n,n*c)
