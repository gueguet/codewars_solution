# https://www.codewars.com/kata/581c06b95cfa838603000435/train/python

from bs4 import BeautifulSoup
import requests

URL = 'https://www.codewars.com/users/leaderboard'

from collections.abc import MutableSequence

"""
# ! ALL THIS PART BECAUSE YOU CANNOT SHIFT AN ARRAY IN PYTHON...
# you also need all the method to deifne correctly the class
# the only thing we really need is the custom __getitem__ method...
# can maybe do better...
class MyList(MutableSequence):
    """A container for manipulating lists of hosts"""
    def __init__(self, data=None):
        """Initialize the class"""
        super(MyList, self).__init__()
        if (data is not None):
            self._list = list(data)
        else:
            self._list = list()

    def __repr__(self):
        return "<{0} {1}>".format(self.__class__.__name__, self._list)

    def __len__(self):
        """List length"""
        return len(self._list)

    def __getitem__(self, ii):
        """Get a list item"""
        return self._list[ii-1]

    def __delitem__(self, ii):
        """Delete an item"""
        del self._list[ii]

    def __setitem__(self, ii, val):
        # optional: self._acl_check(val)
        self._list[ii] = val

    def __str__(self):
        return str(self._list)

    def insert(self, ii, val):
        # optional: self._acl_check(val)
        self._list.insert(ii, val)

    def append(self, val):
        self.insert(len(self._list), val)


class Leaderboard():
    def __init__(self):
        self.position = MyList()
        

class User():
    def __init__(self, name, clan, honor):
        self.name = name
        self.clan = clan
        self.honor = honor

def solution():

    leaderboard = Leaderboard()

    r = requests.get(URL)
    soup = BeautifulSoup(r.content, features="html.parser")

    for tr_tag in soup.find_all('tr')[1:]:
        username = tr_tag.attrs['data-username']
        tr_children = tr_tag.findChildren()
        honor = int(str(tr_children[-1].contents[0]).replace(',',''))
        try:
            clan = tr_children[-2].contents[0]
        except:
            clan = "" 

        user = User(username, clan, honor)
        leaderboard.position.append(user)

    return leaderboard

solution()
"""


"""
* other solutions !!

from collections import namedtuple

URL = 'https://www.codewars.com/users/leaderboard'
    
def solution():
    Table = namedtuple('Table', ['position'])
    Table_Element = namedtuple('Table_Element', ['name', 'clan', 'honor'])
    
    leaderboard = Table({})
    soup = BeautifulSoup(requests.get(URL).text, 'html.parser')
    table = soup.find('table')
    for c, row in enumerate(table.find_all('tr', attrs={'data-username': True}), 1):
        cells = row.find_all('td')
        leaderboard.position[c] = Table_Element(row.attrs['data-username'], cells[2].text, int(cells[3].text.replace(',', '')))
    return leaderboard





# * or just use dict... (I tried it, but I think I used str instead of int to solve it... I try again that at the bottom)

from bs4 import BeautifulSoup
import requests

URL = 'https://www.codewars.com/users/leaderboard'

def solution():    
    soup = BeautifulSoup(requests.get(URL).text)    
    leader_board = leaderboard()
    
    for n, link in enumerate(soup.find_all('tr')[1:]):
        c = link.findChildren('td')
        leader_board.add_user(n + 1, link['data-username'], c[2].string or '', int(c[3].string.replace(',', '')))
    return leader_board
  
class leaderboard:
    def __init__(self):
        self.position = {}
        
    def add_user(self, pos, name, clan, honor):
        self.position[pos] = self.user(name, clan, honor)
        
    class user:
        def __init__(self, name, clan, honor):
            self.name = name
            self.clan = clan
            self.honor = honor
"""

# ! best solution

class Leaderboard():
    def __init__(self):
        self.position = {}
        

class User():
    def __init__(self, name, clan, honor):
        self.name = name
        self.clan = clan
        self.honor = honor

def solution():

    leaderboard = Leaderboard()

    r = requests.get(URL)
    soup = BeautifulSoup(r.content, features="html.parser")

    i = 1

    for tr_tag in soup.find_all('tr')[1:]:
        username = tr_tag.attrs['data-username']
        tr_children = tr_tag.findChildren()
        honor = int(str(tr_children[-1].contents[0]).replace(',',''))
        try:
            clan = tr_children[-2].contents[0]
        except:
            clan = "" 

        user = User(username, clan, honor)
        leaderboard.position[i] = user

        i += 1

    return leaderboard

solution()