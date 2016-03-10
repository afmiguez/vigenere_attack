import sys
import os
import string
import encrypt
import decrypt
from vigenere_matrix import *

#given a string and an integer n, finds all the repeated substrings with lenght=n
#n = 2 =>bigram; n = 3 => trigram, etc.
def n_repetition(n,str):
	str_len=len(str)
	repetition=[]
	#iterates the entire string
	for i in range(str_len):
		#get the actual substring to be checked
		ngram=str[i:i+n]
		#search for the repetition
		index=str.find(ngram,i+n)
		if(index>0):
			#repetition was found, keep the distance
			repetition.append(index-i)
	return repetition

#given a cipher, generate all n_repetition possibles
#end when a given n does not generate a repetition
def get_distances(cipher):
	#start with a digram
	n=2
	buffer_list=None
	repetition_list=[]
	while(1):
		#test a n_repetition
		buffer_list=n_repetition(n, cipher)
		#no repetition was found, stop the search
		if(len(buffer_list)<1):
			break
		#there was a repetition, merge the lists
		else:
			repetition_list+=buffer_list
		n+=1
	return repetition_list

#factorize all distances between repetitions
def get_factors(distances_list):
	if(len(distances_list)<=0):
		sys.exit(2)
	factors=[]
	for distance in distances_list:
		i=2
		while(i<=distance):
			if(distance%i==0):
				factors.append(i)
			i+=1
	return factors

#return a list of factor after being ordered by their frequencies
def get_ordered_factors(cipher):
	distances_list=get_distances(cipher)
	factors=get_factors(distances_list)
	dict_factors=dict()
	for factor in factors:
		dict_factors[factor]=dict_factors.get(factor,0)+1
	sorted_list=sorted(dict_factors.items(), key=lambda (k,v): v, reverse=True)
	factor_list=[]
	for element in sorted_list:
		factor_list.append(element[0])
	return factor_list

def split_cipher_by_period_n(cipher,start_pos,period):
	cipher_len=len(cipher)
	split_string=""
	while(start_pos<cipher_len):
		split_string+=cipher[start_pos]
		start_pos+=period
	return split_string

def get_frequencies_dict(cipher):
	frequency_dict=dict()
	for c in get_alfabet():
		frequency_dict[c]=0
	for c in cipher:
		frequency_dict[c]=frequency_dict.get(c,0)+1
	return frequency_dict

def order_frequencies_by_value(frequency_dict, cipher_len):
	sorted_freq=list() #creates a list of tuples to sort dictionary by hours
	for k,v in frequency_dict.items():
		sorted_freq.append((v/float(cipher_len),k))
	sorted_freq.sort(reverse=True)
	return sorted_freq
	
def get_partial_crypted(decrypted_msg,cipher,block_position,factor,char_candidate):
	#only test characters different from blank ("_")
	if(char_candidate!="_"):
		cipher_len=len(cipher)
		partial_cipher=split_cipher_by_period_n(cipher,block_position,factor)
		partial_decrypted=decrypt.main(partial_cipher,char_candidate)
		j=0
		#replaces the blanks in the partially decrypted msg
		for x in range(cipher_len):
			if(x%factor==block_position):
				decrypted_msg[x]=partial_decrypted[j]
				j+=1
	return decrypted_msg

def init_decrypted(cipher_len):
	decrypted_msg=[]
	for x in range(cipher_len):
		decrypted_msg.append("_")
	return decrypted_msg

def init_possible_key(factor):
	possible_key=[]
	for i in range(factor):
		possible_key.append("_")
	return possible_key

def main(cipher):
	#cipher="nifonaicumniswtluvetvxshknissxwsstbhuslechsnvytsrocdsoynisgxlnonachvchgnonwyndlhsfrnhnpblryowgfunocacossuouolliuvefissoexgosacpbewuormhlftafcmwakbbbdvcqvekmuvilqbgnhntiriljgigatwnvyuveviorimcpbsbhxvivbuvetvxshkuorimmjbdbpjrutfbuegntgofyuwmxmiodmipdekuuswxlfjeksewfyyssnmzscmmbpgebhuvezysaagusaewmffvbwfgimqpilwbbjeuyfbefvbfrtmtwnzuorigwpbvxhjsnmzpfaguhsnmnpglbjbqrhmttrhhuwekmpfakljjenhbbnhooqewvzdakudvumyucbxyoqufvffewvzonxhjumtlfgefvmwnzuxsizbumagxbbtbkvotxxumpxqswtxl"
	if(cipher==""):
		cipher="XnlzaqfqkejkwhzrcatgqhqhgovsujlocejsxwcliiwkwbuzwelzafxrddygrsiqbeflogyrjlvvegtodswgnvfdgdnmhbvupbadehzhhofwktkktcjapwtdavsjeosotsakebuheefvabkgxsugrsibhtghPvrwxsaxehzvjndagscbihslocdhdnwwhgvzxldajrvstnvwjhcbsikukjvupnFKWrzvronwnsuyjlfwnoslailqpvvQHAushzjwwikFKPLVuojfkpfgnbmlqgkktnalegeriufjaojrcatdatfuihwFOOkrzewhpvrwkudfafrexlalugvfgelsjrlvtilxkfrwiaucohfsXfgfpvvrihwjdoegxtakhwbhaylzwhjrbegfascvtwadhrzvronwnoegjswaphyhctzwugyrjlvhncsdqlqvegtodswaphfwwenwjrfupnvyahzwealudsuviohLdsclzedadcfgeajlhmuheefvocezwelzafmxanwjwpzoxtawooihhpsjosfusefkagkreBmlpvrwpskmisjwwalnqzehgatahwkbsikukjvunikjwburbslglOegihwjawjdaolgbsmlsefuahydiilaobfwhtghBcihmaehhskktrwaooehlnwoCBLFkudfafrexlaluhydilsqzcippnlxkfphprksjrndhifvadvqseflhmulhcgnafvgqyemhhzsaejwosrurhwjoocoprgmjrkktsseahzpt"
	
	#cipher="DPRYEVNTNBUKWIAOXBUKWBT"
	#cipher="DBZMGAOIYSOPVFHOWKBWXZPJLVVRFGNBKIXDVUIMOPFQLVVPUDKPRVWOARLWDVLMWAWINZDAKBWMMRLWQIICGPAKYUCVZKMZARPSDTRVDZWEYGABYYEYMGYFYAFHLCMWLWLCVHLMMGYLDBZIFJNCYLOMIAJJCGMAIBVRLOPVFWOBVLKOPVUJZDVLQXWDGGIQEYFBTZMZDVRMMANZWAZVKFQGWEALZFKNZZZVCKVDVLQBWFXUCIEWWOPRMUJZIYKKWEXAIOIYHZIKYVGMKNWMOIIMKADUQWMWIMILZHLCMTCHCMINWSBRHVOPVSODTCMGHMKCEZASYDJKRNWYIKCFOMIPSGAFZKJUVGMGBZJDZWWNZZVLGTZZFZSGXYUTZBJCFPAVNZZAVWSIJVZGPVUVQNKRHFDVXNZZKZJZZZKYPOIEXXMWDNZZQIMHVKZHYDVKYDGQXYFOOLYKNMJGSYMRMLJBYYFPUSYJJNRFHCISYLN"
	
	cipher=cipher.lower()
	cipher_len=len(cipher)

	#construct the string to test the decryption
	decrypted_msg=init_decrypted(cipher_len)

	#construct a list of most common factor using the distances of ngrams in the string
	list_factor=get_ordered_factors(cipher)	
	print list_factor
	
	while True:
		try:
			factor=int(raw_input("Insert the possible length of the key "))
			break
		except ValueError:
			print "Error"
	#construct the string to test the possible key using the factor choose by the user			
	possible_key=init_possible_key(factor)

	#candidate_strings=analyse_frequencies_by_n(cipher,factor)
	os.system("cls")
	while(1):
		while True:
			try:
				position=int(raw_input("Insert the position of the key to be analysed (0-"+`(factor-1)`+") "))
				if(position>=0 and position<=(factor-1)):
					break
			except ValueError:
				print "Error"	
		
		#get a substring of all chars in the cipher afected by the char in the key
		split_cipher=split_cipher_by_period_n(cipher,position,factor)
		#get the frequencies of chars in the substring
		split_cipher_dict=get_frequencies_dict(split_cipher)
		#get a list of all chars ordered by the ratio of its frequency
		list_freq=order_frequencies_by_value(split_cipher_dict,len(split_cipher))
		print list_freq
		while True:
			possible_char=(raw_input("Insert the possible char for the position "+ `position`+" "))
			if len(possible_char)==1:
				if possible_char in get_alfabet():
					break
		#since the word is in english, the most common char in the cipher could be treated as an 'e', thus, shifting to an 'a' would probably give the char used in the key
		possible_char=shift_char_as_e(possible_char)
		#compose the key using the choosen char in the choosen position
		possible_key[position]=possible_char
		#change the test string with the current possible char
		decrypted_msg=get_partial_crypted(decrypted_msg,cipher,position,factor,possible_char)
		os.system("cls")
		print "possible key:"
		for i in range(factor):
			sys.stdout.write(`i`+"")
		print "\n"+"".join(possible_key)+"\nmessage"
		print "".join(decrypted_msg)

if __name__ == "__main__":
	if(len(sys.argv)==1):
		main("")
	elif len(sys.argv)==2:
		main(sys.argv[1])
	else:
		sys.exit(-1)