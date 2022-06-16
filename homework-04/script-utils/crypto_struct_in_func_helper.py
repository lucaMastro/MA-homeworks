base = 0x22bf6b0       
size = 836
end = base + size                  
ebp = 0x22bfca0
def check(input_):
    if (input_ < end and input_ >= base):
        print("offset: {}".format(input_ - base))
        return True                
    else:
        return False

def get_end():
    print(hex(end))

def get_base():
    print(hex(base))

def get_size():
    print(hex(size))


def prova():
    ecx = 0 
    edx = 0
    output = {}
    base_key = 0x483218
    for edx in range(0x100):
        for j in range(8):
            edi = (ecx & 1) - 1
            edi = ~edi
            edi = edi & 0xedb88320
            ecx = ecx >> 1 
            ecx = ecx ^ edi
        output[hex(base_key)] = ecx
        base_key += 4 
        edx += 1
        ecx = edx

    keys = list(output.keys())
    print(len(keys))
    for i in range(0,len(keys),2):

        print(keys[i], ' | ', hex(output[keys[i]]), ' ', hex(output[keys[i+1]]), end=' ')
        print()
             

prova()
