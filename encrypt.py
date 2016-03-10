# -*- coding: UTF-8 -*-
import sys
import re
from vigenere_matrix import *

def encrypt(mesage,key,matrix):
	count=len(mesage)
	key_length=len(key)
	cipher=""
	#iterate all characters from the message
	for i in range(count):
		#get the row in the vigenere matrix associated to the actual character
		row=char_index(mesage[i])
		#get the column in the vigenere matrix that is the index of the current key character 
		col=char_index(key[i%key_length])
		#concatenate in the cypher the character associated to that row and column in the matrix
		cipher+=matrix[row][col]
	if __name__ == "__main__":
		print cipher
	else:
		return cipher

def main(message,key):
	regex = re.compile('[^a-zA-Z]')
	message=regex.sub('',message)

	#making the encryption pad
	#str=put_padding_str(str,group)

	matrix=get_vig_matrix()

	#encrypt
	cipher=encrypt(message.lower(),key,matrix)
	return cipher


if __name__ == "__main__":
	#print len(sys.argv)
	if(len(sys.argv)==3):
		main(sys.argv[1],sys.argv[2])
	else:
		sys.exit(2)
