REG_DW = 0xffffffff
REG_W =0x10000 
REG_H = 0xff00
REG_L = 0x00ff 

flags = { 'C': 0 }

registers = {
        'EAX': 0,
        'ECX': 0x22bf501,
        'EDX': 0x78bfbff,
        'EBX': 0,
        'ESI': 0x22bf590,
        'EDI': 0x22bfe48,
        'EBP': 0x22bf548,
        'ESP': 0x22bf33c
        }


# size 0x200
ebp = []
for i in range(0x200):
    ebp.append(0)

def reg_l(reg_name):
    return registers[reg_name] & REG_L
def reg_h(reg_name):
    return registers[reg_name] & REG_H >> 8
def reg_w(reg_name):
    return registers[reg_name] & REG_W
def reg_dw(reg_name):
    return registers[reg_name] & REG_DW

def change_reg_value(reg_name, size_filter, value):
    reg = registers[reg_name]
    if (size_filter == REG_H):
        ah = (reg & ~REG_H) | (value & REG_L << 8)
        reg = (reg & 0xffff00ff | ah)
    else:
        reg = (reg & ~size_filter) | (value & size_filter)
    registers[reg_name] = reg 

def neg(reg_name, reg_size):
    tmp = registers[reg_name] & reg_size
    if (tmp != 0):
        flags['C'] = 1
    change_reg_value(reg_name, reg_size, -tmp)




change_reg_value('EDX', REG_DW, reg_l('ECX'))
ebp[reg_dw('EDX') - 0x100] = reg_l('EAX')

change_reg_value('EDX', REG_L, reg_l('ECX'))
change_reg_value('EDX', REG_L, reg_l('EDX') & 0x80)
ebp[reg_dw('EAX') - 0x200] = reg_l('ECX')

registers['EAX'] += 1
neg('EDX', REG_L)




