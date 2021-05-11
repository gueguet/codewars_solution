# https://www.codewars.com/kata/52ea928a1ef5cfec800003ee/train/python

def ip_to_int32(ip):
    octets_list = ip.split(".")
    bin_decomp = []

    for octect in octets_list:
        bin_decomp.append(bin(int(octect))[2:].zfill(8))

    final_bit_num = int("".join(bin_decomp),2)
    return final_bit_num

ip_to_int32("128.32.10.1")