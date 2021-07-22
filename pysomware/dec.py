from Crypto.Cipher import AES


key = b"qwertyuiop123456"

def decrypt(path):

	file_in = open(path, "rb")
	nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]


	# let's assume that the key is somehow available again
	cipher = AES.new(key, AES.MODE_EAX, nonce)
	data = cipher.decrypt_and_verify(ciphertext, tag)

	path = path.replace('.crypt', '')

	file_out = open(path, 'wb')

	file_out.write(data)

	file_out.close()
