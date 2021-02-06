# https: // www.codewars.com/kata/53368a47e38700bd8300030d/train/python

def namelist(names):

    if (len(names) == 0):
        return ''

    if (len(names) == 1):
        return names[0]['name']

    else:
        res = names[0]['name']
        for name_dict in names[1:-1]:
            print(name_dict)
            res += ', ' + name_dict['name']
        res += ' & ' + names[-1]['name']

    print(res)
    return res





namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}])
# returns 'Bart, Lisa & Maggie'
