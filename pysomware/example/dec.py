from Crypto.Cipher import AES

file_in = open("enc.txt", "rb")
nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]

key = b"qwertyuiop123456"

# let's assume that the key is somehow available again
cipher = AES.new(key, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(ciphertext, tag)


print(data)
