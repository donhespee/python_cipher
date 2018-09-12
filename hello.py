print('''This program is written by ADEYI SEGUN
	Email address: adeyi1759@gmail.com
	Phone number: 08066576271''')

#cipher	

alphabet = "abcdefghijklmnopqrstuvwxyz "
key = "xznlwebgjhqdyvtkfuompciasr" 
secret_message = input("Enter your message:" )
secret_message = secret_message.lower() 
for y in secret_message: 
  if y.isalpha(): 
      print(key[alphabet.index(y)], end = '') 
  else:
      print(y, end = '')


#Decipher

alphabet = "abcdefghijklmnopqrstuvwxyz "
key = "xznlwebgjhqdyvtkfuompciasr" 
secret_message = input("Enter your message:" )
secret_message = secret_message.lower() 
for y in secret_message: 
  if y.isalpha(): 
      print(alphabet[key.index(y)], end = '') 
  else:
      print(y, end = '')


