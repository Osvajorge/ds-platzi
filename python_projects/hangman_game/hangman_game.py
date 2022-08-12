import os
import variables
import random

#hangman game
def hangman_game():
    title()
    os.system ("echo '{}' | lolcat".format(variables.SUBMENU))
    #open data file
    with open('./data.py', 'r', encoding="utf-8") as f:
        dt = f.read() #read file
    
    #
    while True:
        wordtoguess = random.choice(dt.split('\n')) #random word from data file
        print(wordtoguess)

        



def title():
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system ("echo '{}' | lolcat".format(variables.HANGMAN_TITLE)) #print title and pass it trough the terminal using lolcat

def menu():
    while True:
        title()
        os.system ("echo '{}' | lolcat".format("1. Play"))
        os.system ("echo '{}' | lolcat".format("2. Exit"))
        choice = input("Enter your choice: ")
        if choice == "1":
            title()
            print("1. English")
            print("2. Spanish")
            os.system ("echo '{}' | lolcat".format("Press any other key to exit"))
            print("\n")
            language = input("Enter the language in which you want to guess: ")
            if language == "1":
                hangman_game()
            elif language == "2":
                hangman_game()
            break   
        elif choice == "2":
            break
        else:
            print("Invalid choice")
            continue

def run ():
    menu()

if __name__ == '__main__':
    run()
