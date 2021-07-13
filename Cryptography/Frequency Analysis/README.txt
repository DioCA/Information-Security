########################################################################
			Frequency Analysis Lab
########################################################################

This lab is to use frequency analysis to find the key and decode the ciphertext.
You can use the frequency.py to find the frequency of each encrypted letter inside the ciphertext file. Then, use the letter_frequency.png as reference to guess the corresponding letter in plaintext. Try decrypted each letter one at a time until you can read the text.


Example:
./frequency.py plain.txt
plain.txt
{'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 
'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 
'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0, 'j': 24, 
'p': 26, 'u': 26, 'n': 28, 'g': 30, '7': 31, 'w': 46, 'm': 47, 'e': 105, 
'b': 128, 'a': 153, '5': 438, '9': 545, 'c': 579, 'r': 3685, 'l': 4568, 
'o': 6646, 'z': 7240, 'x': 8312, 'k': 9363, 'q': 9777, '3': 11119, 
'h': 11555, '0': 12151, '8': 13605, '4': 17634, 'y': 19065, 'd': 25709, 
'i': 27942, 'v': 29589, '6': 29702, 't': 31241, 's': 34867, '1': 36147, 
'2': 40546, 'f': 54973}

# f is the most frequently appearing letter in ciphertext. 
# we believe that the plaintext is english, we suspect that f->E
# So we replace f with E in plain.txt

ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
    f





















########################################################################
			File Description
########################################################################

cipher.txt:	
	
	This file contains the encrypted ciphertext produced from the plain.txt using encrpt.py. 


plain.txt:

	This file contain the plaintext 


key.txt:

	The derived key we found by using the frequency analysis method
	
	
letter_frequency.png:

	The picture showing the frequency of each English letter
	
encrypt.py:

	The python program we used to encrypt to text
	
	
frequency.py:

	The python program we used to analysis the frequency of letters in a file
	
