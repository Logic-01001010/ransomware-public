import enc
import dec
import os


def findFile(path):

	filenames = os.listdir(path)

	for file in filenames:

		if not os.path.isdir(path+'/'+file):

			print('found file: {}'.format(file))

			if '.crypt' in file:

				try:
					dec.decrypt(path+'/'+file)
					os.remove(path+'/'+file)
                    
				except Exception as e:
					print('warning dec.decrypt() error. {}'.format(e))

def scanDir(path):

	print("current path: {}".format(path))

	findFile(path)


	filenames = os.listdir(path)

	for file in filenames:

		if os.path.isdir(path+'/'+file):

			print("found folder: {}".format(file))

			scanDir(path+'/'+file)


path = os.getcwd() # current dir path

scanDir('./target') # path

