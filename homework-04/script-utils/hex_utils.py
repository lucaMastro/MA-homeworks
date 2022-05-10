def hex_to_dec(n:str):
    return int(n, 16)

def dec_to_hex(n:int):
    s = hex(n)
    return s[2:]

def add_hexs(hex1:str, hex2:str):
    n1_int = hex_to_dec(hex1)
    n2_int = hex_to_dec(hex2)
    sum_int = n1_int + n2_int
    return dec_to_hex(sum_int)


def sub_hexs(hex1:str, hex2:str):
    n1_int = hex_to_dec(hex1)
    n2_int = hex_to_dec(hex2)
    sum_int = n1_int - n2_int
    return dec_to_hex(sum_int)

def signed_hex_value(hex_str:str):
    bin_value = bin(hex_to_dec(hex_str))[2:]
    reversed_ = bin_value[::-1]
    sum_ = 0
    size = len(reversed_)
    for i in range(size - 1):
        sum_ += pow(2, i) * int(reversed_[i])

    return sum_ - pow(2, len(reversed_) - 1)

# def two_complement(n):
    # if type(n) != str and type(n) != int:
        # print("error: type must be int or str")
    # else:
        # n_bin = n 
        # if type(n) == int:
            # n_bin = bin(n)
            # n_bin = n_bin[n_bin.find('b') + 1:]
        # return bin_two_complement(n_bin)

# def bin_two_complement(n_bin:str):
    # negated = ''
    # for bit in n_bin:
        # if bit == '1':
            # negated += '0'
        # else:
            # negated += '1'
    # int_neg = int(negated, 2)
    # int_neg += 1 
    # return int_neg

def two_complement(n:int):
    return ~n + 1

