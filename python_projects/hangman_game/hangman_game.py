import os
import variables
import random
import data

def get_word(language):
    if language == 'es':
        get_word.word = data.ES_WORDS[random.randint(0, len(data.ES_WORDS)-1)]
    if language == 'en':
        get_word.word = data.EN_WORDS[random.randint(0, len(data.EN_WORDS)-1)]
    return get_word.word

def game_screen(word):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n")
        print("The word is: ")
        print(word)
        print("\n")
        print("You have {} tries left".format(variables.TRIES))
        print("\n")
        print("The letters you have guessed: ")
        print(variables.GUESSED)
        print("\n")
        guess = input("Enter a letter: ")
        if guess in variables.GUESSED:
            print("You have already guessed that letter")
            continue
        elif guess in word:
            variables.GUESSED.append(guess)
            print("\n")
            print("Correct")
            print("\n")
        else:
            variables.TRIES -= 1
            print("\n")
            print("Incorrect")
            print("\n")
        if variables.TRIES == 0:
            print("You lost")
            break
        if "*" not in variables.GUESSED:
            print("You won")
            break
        if variables.TRIES > 0:
            continue
        else:
            break
    
        
    

#hangman game
def hangman_game():
    title()
    os.system ("echo '{}' | lolcat".format(variables.SUBMENU))
    get_word(menu.chosen_l)
    game_screen(get_word)
    

    






                
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
            print("1. Spanish")
            print("2. English")
            os.system ("echo '{}' | lolcat".format("Press any other key to exit"))
            print("\n")
            language = input("Enter the language in which you want to guess: ")
            if language == "1":
                menu.chosen_l='es'
                hangman_game()
            elif language == "2":
                menu.chosen_l='en'
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
