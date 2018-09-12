print('''This program is written by ADEYI SEGUN
	Email address: adeyi1759@gmail.com
	Phone number: 08066576271''')
	
alphabet = "abcdefghijklmnopqrstuvwxyz "
key = "xznlwebgjhqdyvtkfuompciasr" 
secret_message = input("Enter your message:" )
secret_message = secret_message.lower() 
for y in secret_message: 
  if y.isalpha(): 
      print(key[alphabet.index(y)], end = '') 
  else:
      print(y, end = '')