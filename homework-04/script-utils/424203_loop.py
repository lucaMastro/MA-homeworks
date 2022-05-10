dword_keeper = 0xffffffff
word_keeper = 0xffff
byte_keeper = 0xff

_19fcae = [0xf0, 0x03, 0x19,0x17, 0x84,0x84,0x48,0x5e,0x42]

_19fc7d_output = []

ecx = 0x883f
eax = 0x5e48
for i in range(8):
    cl = ecx & byte_keeper 
    al = cl

    ecx = (ecx * 0x1f0d) & dword_keeper
    cx = ecx & word_keeper
    cl = ecx & byte_keeper 
    
    bl = 0x51
    eax = bl * al
    al = eax & byte_keeper
    al = al ^ _19fcae[i] 
    _19fc7d_output.append(al)
    ecx = cx 

print('[', end =' ')
for i in _19fc7d_output:
    print(hex(i), end=' ')
print(']')
