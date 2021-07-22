def read(file):

	data = b""

	f = open(file,  mode='rb')

	while True:
		line = f.readline()
		if not line: break
		data+=bytes(line)

	f.close()

	return data
