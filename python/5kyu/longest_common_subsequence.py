# https://www.codewars.com/kata/52756e5ad454534f220001ef

import itertools


def get_list_subseq(str):
    res = []
    combs = []
    for l in range(1, len(str)+1):
        combs.append(list(itertools.combinations(str, l)))

    for c in combs:
        for t in c:
            combi = (''.join(t))
            res.append(combi)
    return res


def lcs(x, y):
    all_combi_x = get_list_subseq(x)
    all_combi_y = get_list_subseq(y)

    lcs = ""
    for combi_x in all_combi_x:
        for combi_y in all_combi_y:
            if (combi_x == combi_y):
                if len(combi_x) > len(lcs):
                    lcs = combi_x
    return lcs


lcs("a", "b")
