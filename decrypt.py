# -*- coding: UTF-8 -*-
import sys
import re
from vigenere_matrix import *

def decrypt(cipher,key,matrix):
	message=""
	key_length=len(key)
	cipher_len=len(cipher)
	alfabet_len=get_alfabet_len()
	#iterate all characters of the cipher
	for i in range(cipher_len):
		pos_key=i%key_length
		row_actual=char_index(key[pos_key])
		for j in range(alfabet_len):			
			if(cipher[i]==matrix[row_actual][j]):
				message+=index_char(j)
				break
	if __name__ == "__main__":
		print message
	else:
		return message

def main(cipher, key):
	regex = re.compile('[^a-zA-Z]')
	cipher=regex.sub('',cipher)
	
	#create vigenere matrix
	matrix=get_vig_matrix()

	#decrypt
	message=decrypt(cipher.lower(),key,matrix)
	return message

if __name__ == "__main__":
	if(len(sys.argv)==3):
		main(sys.argv[1],sys.argv[2])
	else:
		sys.exit(2)