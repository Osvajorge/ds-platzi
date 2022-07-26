import random
import string

print('\033[1m'+"Hello, this is a password generator.\n"+'\033[0m')

def menu():
    try:
        menu.ln = int(input("How many characters would you like your password to be? "))
    except:
        print("\033[91m"+"Please enter a number."+'\033[0m')
        menu()   
    if menu.ln < 8 or menu.ln > 16:
        print('\033[93m'+"Password length must be between 8 and 16 characters."+'\033[0m')
        menu()            
    else:
        n = [0,1,2,3,4,5,6,7,8,9]
        p = list('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
        lmayus = list(string.ascii_uppercase)
        lminus = list(string.ascii_lowercase)
        menu.characters = n + p + lmayus + lminus
              
# Generates a random password
def pwd_generator():
    print('\033[96m'+"Generating password..."+'\033[0m')
    pwd = ""
    for i in range(menu.ln):
        pwd += str(random.choice(menu.characters))
    return ('\033[92m'+pwd+'\033[0m')
       
def run():
    menu()
    print("Your password is: " + pwd_generator())

if __name__ == '__main__':
    run()