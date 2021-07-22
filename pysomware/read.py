def read(file):

	data = b""

	f = open(file, 'r')

	while True:
		line = f.readline()
		if not line: break
		data+=bytes(line, encoding='utf-8')

	f.close()

	return data
