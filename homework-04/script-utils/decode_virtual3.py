from sub_hex import *
prev_enc = 'f2136d07'
enc = "67525fac"
xor_const = '954132ac'

enc_minus_6 = sub_hexs(enc, '6')
xor = dec_to_hex(hex_to_dec(enc_minus_6) ^ hex_to_dec(xor_const))
print(sub_hexs(xor, prev_enc))
