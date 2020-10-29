from colorama import Fore
import sys
from time import sleep
import os
# Dictionary representing the morse code chart 

MORSE_CODE_DICT = { 'a':'.-', 'b':'-...', 

                    'c':'-.-.', 'd':'-..', 'e':'.', 

                    'f':'..-.', 'g':'--.', 'h':'....', 

                    'i':'..', 'j':'.---', 'k':'-.-', 

                    'l':'.-..', 'm':'--', 'n':'-.', 

                    'o':'---', 'p':'.--.', 'q':'--.-', 

                    'r':'.-.', 's':'...', 't':'-', 

                    'u':'..-', 'v':'...-', 'w':'.--', 

                    'x':'-..-', 'y':'-.--', 'z':'--..', 

                    '1':'.----', '2':'..---', '3':'...--', 

                    '4':'....-', '5':'.....', '6':'-....', 

                    '7':'--...', '8':'---..', '9':'----.', 

                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 

                    '?':'..--..', '/':'-..-.', '-':'-....-', 

                    '(':'-.--.', ')':'-.--.-'} 

  
# Function to encrypt the string 

def encrypt(message): 

    cipher = '' 

    for letter in message: 

        if letter != ' ': 
            
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:

            cipher += ' '

    return cipher 

  
# Function to decrypt the string 

def decrypt(message): 

    message += ' '

    decipher = '' 

    citext = '' 

    for letter in message:

        if (letter != ' '):  

            i = 0

            citext += letter 

        else: 
        
            i += 1
            
            if i == 2 :
                
                decipher += ' '

            else: 
            
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT 

                .values()).index(citext)] 

                citext = '' 

    return decipher 

  
#================== Menu ====================

while True:
	
	os.system('clear')
	
	try:
		
		print(Fore.CYAN+"The Morser")
		
		sleep(0.2)
		
		print(Fore.GREEN+"[1] English to Morse Code")
		sleep(0.2)
		
		print(Fore.GREEN+"[2] Morse Code to English")
		
		sleep(0.2)
		
		print(Fore.RED+"[3] Exit")
		
		sleep(0.2)
		
		print(Fore.YELLOW+"[4] About")
		
		sleep(0.2)
		
		menu = int(input(f"{Fore.RED}[root{Fore.GREEN}@home] "))
		
		if menu == 1:
			
			os.system('clear')
			
			print(Fore.CYAN+"The Morse")
			
			sleep(0.2)
			
			print(Fore.YELLOW+"please print your text\n")
			sleep(0.2)
			
			message = input(f'{Fore.RED}[root{Fore.GREEN}@home/text] ')
			
			result = encrypt(message) 

			print (result)
			
			input(Fore.BLUE+"Enter for back")
			
		elif menu == 2:
		
			os.system('clear')
	
			print(Fore.CYAN+"The Morse")
			
			sleep(0.2)
		
			print(Fore.YELLOW+"please print your Morse Code\n")
		
			sleep(0.2)
			
			message = input(f'{Fore.RED}[root{Fore.GREEN}@home/morse-code] ')

			result = decrypt(message) 

			print (result)
			
			input(Fore.BLUE+"Enter for back")
			
		elif menu == 3:
			
			print(Fore.LIGHTMAGENTA_EX+"Thanks for use,\n Bye!")
			
			break
			
			sys.exit()
			
		elif menu == 4:
			
			print(f"{Fore.CYAN}\nThe Morse\n{Fore.GREEN}Powered By Guardiran Security Team\n{Fore.YELLOW}Writer: SHIWPTS13\n{Fore.RED}Website: https://Guardiran.org\n")
			input(Fore.BLUE+"Enter for back")
		
		
		
		else:
			print(Fore.YELLOW+"please wait...")
			sleep(5)
			
			print(Fore.RED+"Bye!")
			
			break
			
			sys.exit()
			
	except:
			print(Fore.YELLOW+"please wait...")
			sleep(5)
			print(Fore.RED+'Bye!')
			break
			sys.exit()
			
