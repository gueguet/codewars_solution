# https://www.codewars.com/kata/551dc350bf4e526099000ae5/train/python*

def song_decoder(song):
    song = song.replace("WUBWUBWUB", " ")
    song = song.replace("WUBWUB", " ")
    song = song.replace("WUB", " ")
    song = song.replace("  ", " ")
    song = song.strip()
    return song

song_decoder("AWUBBWUBC")
song_decoder("AWUBWUBWUBBWUBWUBWUBC")

"""
* clever

return " ".join(song.replace('WUB', ' ').split())

import re
return re.sub('(WUB)+', ' ', song).strip()
"""