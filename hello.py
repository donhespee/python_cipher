'''print(This program is written by ADEYI SEGUN
	Email address: adeyi1759@gmail.com
	Phone number: 08066576271)
	
alphabet = "abcdefghijklmnopqrstuvwxyz "
key = "xznlwebgjhqdyvtkfuompciasr" 
secret_message = input("Enter your message:" )
secret_message = secret_message.lower() 
for y in secret_message: 
  if y.isalpha(): 
      print(key[alphabet.index(y)], end = '') 
  else:
      print(y, end = '')'''



temp = eval(input('Enter a temperature in Celsius: '))
f_temp = 9/5*temp+32
print('In Fahrenheit, that is, f_temp') 
if f_temp > 212: 
   print('That temperature is above the boiling point.') 
if f_temp < 32: 
   print('That temperature is below the freezing point.')