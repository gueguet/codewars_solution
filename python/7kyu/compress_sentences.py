# https://www.codewars.com/kata/59de469cfc3c492da80000c5/train/python


def compress(sentence):
    post_list = []
    for word in sentence.split(" "):
        if word.lower() not in post_list:
            post_list.append(word.lower())
            
    res = ""
    
    for word in sentence.split(" "):
        res += str(post_list.index(word.lower()))
            
    return res


compress("The number 0 is such a strange number Strangely it has zero meaning")


"""
* clever

def compress(sentence):
    ref = []
    for i in sentence.lower().split():
        if i not in ref:
            ref.append(i)
    return ''.join([str(ref.index(n)) for n in sentence.lower().split()])
"""
