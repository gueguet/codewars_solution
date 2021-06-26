# https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b/train/python

def human_years_cat_years_dog_years(human_years):

  if (human_years == 1):
    return [1,15,15]

  if (human_years == 2):
    return [2,24,24]

  return [human_years,15+9+((human_years-2)*4),15+9+((human_years-2)*5)]

