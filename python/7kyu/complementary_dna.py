# https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python

def DNA_strand(dna):
    dna_dict = {
        "A":"T",
        "T":"A",
        "C":"G",
        "G":"C"
    }

    res = ""
    for char in dna:
        res += dna_dict[char]

    return res
    print(res)


DNA_strand("ATTGC")


"""
one line solution
    return dna.translate(string.maketrans("ATCG","TAGC"))

or with dict but with join function
    return ''.join([pairs[x] for x in dna])
"""
