import binascii

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad


def decrypt_DES(ciphertext: bytes, key: bytes) -> bytes:
    cipher = DES.new(key, DES.MODE_ECB)
    # If used in 2DES, this could be X, not P
    p = unpad(cipher.decrypt(ciphertext), DES.block_size)
    return p



def generate_keys(key: bytes) -> list[bytes]:
    keys = []
    for i in range(256):
        for j in range(256):
            for k in range(256):
                # To make the bytes editable, we convert
                # it to a list explicitly
                l = list(key)
                l[0] = i
                l[1] = j
                l[2] = k
                # Convert the list back to bytes
                keys.append(bytes(l))

    return keys

K1 = b"aaaxkrmd"
K2 = b"cccxkrmd"


x_cats_bck = {}
for key in generate_keys(K2):  # We know the final xkrmd
    try:
        x = decrypt_DES(ciphertext, key)
        x_cats_bck[x] = key
    except ValueError:
        continue  # Bad padding, let's skip this key
