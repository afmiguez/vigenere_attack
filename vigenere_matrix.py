# -*- coding: UTF-8 -*-
import string
import sys

alfabet=string.letters[:26]


def get_alfabet_len():
	return len(alfabet)

def get_alfabet():
	return alfabet

def create_matrix(alfabet):
	matrix=[]
	alfabet_len=len(alfabet)
	for i in range(alfabet_len):
		row_list=[]
		for j in range(alfabet_len):
			row_list.append(alfabet[(i+j)%alfabet_len])
		matrix.append(row_list)
	return matrix

matrix=create_matrix(alfabet)

def char_index(c):
	try:
		index=ord(c)-97
		if(index>=0 and index <= (97+25)):
			return index
	#else:
		#return -1	
	except TypeError:
		raise


def index_char(index):
	return matrix[0][index%get_alfabet_len()]

def shift_char(c, shift_n):
	return index_char(char_index(c)+shift_n)

def shift_char_as_e(c):
	return shift_char(c,-4)

def get_vig_matrix():
	return matrix

def main():
	#create vigenere matrix	
	matrix=create_matrix(alfabet)
	if __name__ == "__main__":
		print matrix
	else:
		return matrix

if __name__ == "__main__":
	if(len(sys.argv)==1):
		main()
	else:
		sys.exit(-1)