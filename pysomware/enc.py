from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import read




key = b'qwertyuiop123456'
extenstion = '.crypt'

def encrypt(path):

	data = read.read(path)
	data = base64.b64encode(data)

	cipher = AES.new(key, AES.MODE_EAX)
	ciphertext, tag = cipher.encrypt_and_digest(data)


	file_out = open(path+extenstion, "wb")
	[ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
	file_out.close()
