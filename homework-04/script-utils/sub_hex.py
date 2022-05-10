def hex_to_dec(n:str):
    return int(n, 16)

def dec_to_hex(n:int):
    s = hex(n)
    return s[2:]

def sub_hexs(hex1:str, hex2:str):
    n1_int = hex_to_dec(hex1)
    n2_int = hex_to_dec(hex2)
    sum_int = n1_int - n2_int
    return dec_to_hex(sum_int)

if __name__ == '__main__':
    import sys
    n1 = sys.argv[1]
    n2 = sys.argv[2]
    
    print(sub_hexs(n1,n2))
