l = [0x3f, 0x88,0xf0, 0x03,0x19,0x17,0x84,0x84,0,0]
ecx = 0x50b
word_keeper = 0xffff

for i in l:
    cx = ecx & word_keeper
    dx = (cx + i) & word_keeper
    dx = dx * 0x1e0b
    ecx = dx & word_keeper
    print(hex(ecx))

print(hex(ecx))

