from hashlib import md5

def get_hex_array(s):
    r = md5(s)
    l = []
    for i in range(16):
        digest = r.digest()
        l.append(hex(digest[i]))
    return l

def get_hex_string(r):
    l = ""
    digest = r.digest()
    for i in range(16):
        l += hex(digest[i])
    return [r, l]

def get_md5_obj(s):
    return md5(s)
    

def find(output):
    for i in range(256):
        for j in range(256):
            for k in range(256):
                s = (i).to_bytes(1, byteorder='big') + (j).to_bytes(1, byteorder='big') + (k).to_bytes(1, byteorder='big')
                digest = get_hex_string(s)
                if (digest) == output:
                    return [i,j,k]
    return []


def find_string(output):
    for i in range(256):
        for j in range(256):
            for k in range(256):
                s = (i).to_bytes(1, byteorder='big') + (j).to_bytes(1, byteorder='big') + (k).to_bytes(1, byteorder='big')
                r = get_md5_obj(s)
                digest = r.hexdigest()
                if digest == output:
                    return [i,j,k]
    return []

