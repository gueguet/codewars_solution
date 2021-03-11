# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python

def find_short(s):
    word_list = s.split(" ")
    word_list = sorted(word_list, key=str.__len__)
    l = len(word_list[0])
    return l  # l: shortest word length

find_short("bitcoin take over the world maybe who knows perhaps")
