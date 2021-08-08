def decrypt(ciphertext,key):

	result = ""



	# traverse text

	for i in range(len(ciphertext)):

		char = ciphertext[i]



		# Encrypt uppercase characters

		if (char.isupper()):

			result += chr((ord(char) - key-65) % 26 + 65)



		# Encrypt lowercase characters

		else:

			result += chr((ord(char) - key - 97) % 26 + 97)



	return result



#check the above function

ciphertext=input("cipher: ")

key =int(input("shift: "))

print ("Text : " + ciphertext)

print ("Shift : " + str(key))

print ("Cipher: " + decrypt(ciphertext,key))