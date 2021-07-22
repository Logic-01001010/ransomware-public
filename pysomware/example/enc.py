from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


data = b"hello world!"
key = b'qwertyuiop123456'

#key = get_random_bytes(16)

print(len(key))


cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)

file_out = open("enc.txt", "wb")
[ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
file_out.close()
