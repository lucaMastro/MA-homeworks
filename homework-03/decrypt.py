
def decrypt_byte(hex1, hex2):
    tmp = int(hex1, 16) ^ int(hex2,16)
    return chr(tmp)

if __name__ == '__main__':
    hex_key = ['3f', '28', '2f', 'a5', '5d', '47', 
            '3d', '4f', '3f']
            
    expected_outputs = ['0c', '5a', '61', 'c0', '2e',
            '13', '0d', '70', '1e']
    s = ''
    for k_i,y_i in zip(hex_key, expected_outputs):
        s += decrypt_byte(k_i, y_i)
    print('The password is:', s)
