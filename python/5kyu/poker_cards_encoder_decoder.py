# https://www.codewars.com/kata/52ebe4608567ade7d700044a/train/python

# dict to encode
symbol_values = {
    "c":0,
    "d":1,
    "h":2,
    "s":3
}
val = "A 2 3 4 5 6 7 8 9 T J Q K"
value_dict = dict(zip(val.split(" "),[x for x in range(0,13)]))

# dict to decode
inv_symbol_values = {v: k for k, v in symbol_values.items()}
inv_value_dict = {v: k for k, v in value_dict.items()}


print(value_dict)


def encode(cards):
    res = []
    for card in cards:
        res.append(value_dict[card[0]] + 13*symbol_values[card[1]])
    res.sort()
    return res

def decode(cards):
    res = []
    cards.sort()
    for num in cards:
        sym = num // 13
        val = num % 13
        string_res = "{}{}".format(inv_value_dict[val],inv_symbol_values[sym])
        res.append(string_res)
    return res



# encode(['Ac', 'Ks', '5h', 'Td', '3c'])
# decode([0, 51, 30, 22, 2])


"""
* you can do much better...

str = "A23456789TJQK"
card = "cdhs"

def encode(cards):
    return sorted([card.index(x[1]) * 13 + str.index(x[0]) for x in cards])

def decode(cards):
    return [f"{str[x % 13]}{card[x // 13]}" for x in sorted(cards)]
"""