import rsa
from base64 import b64encode


bytes_to_crypt = bytes.fromhex("e778c2bee472ebea59e33913ee0ee322")

rsa_key = "06 02 00 00 00 A4 00 00 52 53 41 31 00 08 00 00 01 00 01 00 A7 49 CD 90 52 BE 0D EB 8E 77 79 79 6B 56 79 2F 1D E5 CA ED 76 46 66 51 40 2A 7E 1D 57 25 09 FA D1 70 3D D5 13 4E E0 D6 B8 2E FE 9F 6A 3E 4E A8 6D 44 F4 E5 A0 AE 61 B9 37 4F 71 BF 35 AE 88 5A E7 78 4A 6A 8F F7 15 23 D4 71 20 20 36 EC 10 34 C9 AC F5 CF 51 40 05 14 83 6A B1 A9 B2 01 EF 74 0C 74 02 46 CC 80 A6 1B BD 0A 4E FF 14 52 37 87 5D 3F 41 75 F2 9E 5D 60 DA 50 8C B2 8A A6 09 AD 44 E4 80 63 F0 F6 37 2D 52 2B 8E 48 A1 95 05 7B 3F B6 B8 CF 77 EA EC 72 A0 8D 3B 0A C7 37 61 E9 C3 98 49 11 D1 D0 BE 4A 32 4B 66 72 79 70 E5 46 E3 4D 9B AB 69 FC 71 32 B1 F3 DF 0B F6 A6 EE 5D 07 68 6F CF 99 FD 58 5C 13 A2 12 95 A2 B0 C7 B1 A5 BA B4 F7 E7 A8 31 53 F4 A8 92 03 33 CE 48 54 5D E7 1F 4F D5 85 9E 98 8E 84 5A EF 0B 7B E8 D7 E4 6A 44 BF CB 67 BD C5 51 A7 38 F3 4F B0 42 BD".replace(" ", '')[2 * 20:]


def print_encoded():
    bytes_rsa_key = bytes.fromhex(rsa_key)
    print(b64encode(bytes_rsa_key))

if __name__ == '__main__':
    with open('tmp.pem', mode='rb') as privatefile:
        keydata = privatefile.read()

    key = rsa.PrivateKey.load_pkcs1(keydata)
    c = rsa.encrypt(bytes_to_crypt, key)
    print(c)


