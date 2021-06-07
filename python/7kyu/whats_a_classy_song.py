# https://www.codewars.com/kata/6089c7992df556001253ba7d/train/python

class Song():
  def __init__(self,title,artist):
    self.title = title
    self.artist = artist
    self.people_listen = []


  def how_many(self,people_array):
    counter = 0 
    for people in people_array:
      if people.lower() not in self.people_listen:
        self.people_listen.append(people.lower())
        counter += 1
    return counter


mount_moose = Song('Mount Moose', 'The Snazzy Moose')

print(mount_moose.title)
print(mount_moose.artist)
print(mount_moose.how_many(['John', 'Fred', 'Bob', 'Carl', 'RyAn']))


"""
* clever --> use set and map function

class Song:
    def __init__(self, a, b):
        self.title = a
        self.artist = b
        self.s = set()
    
    def how_many(self, a):
        return sum(x not in self.s and (self.s.add(x) or 1) for x in map(str.lower, a))
"""
