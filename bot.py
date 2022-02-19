import json
from datetime import date
import random
from colorama import *
init()

today = date.today()
d1 = today.strftime("%m/%d/%Y")

"""

Word Example: 

Current word: Means
MNCRD


"""

print(Fore.CYAN+
      
    """
    
░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░██╗░░░░░███████╗  ░██████╗░██╗░░░██╗███████╗░██████╗░██████╗██████╗░
░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗██║░░░░░██╔════╝  ██╔════╝░██║░░░██║██╔════╝██╔════╝██╔════╝██╔══██╗
░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║██║░░░░░█████╗░░  ██║░░██╗░██║░░░██║█████╗░░╚█████╗░╚█████╗░██████╔╝
░░████╔═████║░██║░░██║██╔══██╗██║░░██║██║░░░░░██╔══╝░░  ██║░░╚██╗██║░░░██║██╔══╝░░░╚═══██╗░╚═══██╗██╔══██╗
░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝███████╗███████╗  ╚██████╔╝╚██████╔╝███████╗██████╔╝██████╔╝██║░░██║
░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚══════╝  ░╚═════╝░░╚═════╝░╚══════╝╚═════╝░╚═════╝░╚═╝░░╚═╝
"""
      
)

print(Fore.RESET+f'\nWelcome to Wordle on {d1}!')

print('\n--- COMMANDS ---\n(1) Start the guessing program\n(2) Generate random word\n')
ask = input('>> ')

new_list = []
real_list = []

def random_word():
    a_file = open(f"all_words.json", "r")
    json_object = json.load(a_file)
    a_file.close()

    randomword = random.choice(json_object).title()

    print(f'\nYour random word is: '+Fore.CYAN+randomword)

    print(Fore.RESET+'\nDo you want to pick another random word? (enter "y" if yes)')
    ask = input('>> ')
    ask = ask.lower()
    if ask == 'y':
        random_word()

def start():
    print('\nWhat is your current word in wordle?')
    current_word = input('>> ')
    if len(current_word) != 5:
        print('This word is not 5 characters! Make sure to enter a 5 letter word.\nI will be restarting the process now.\n\n')
        return start()

    #print(str(len(new_list)))

    print('\nWhat are the bad letters in this word? (Example: ABC)')
    bad_letters = input('>> ')
    bad_letters = bad_letters.lower()
    
    a_file = open(f"all_words.json", "r")
    json_object = json.load(a_file)
    a_file.close()
    
    sumofwords = 0

    for i in json_object:
        if any((c in bad_letters) for c in i):
            pass # There are bad letters here
        else:
            new_list.append(i)
            print('added word')
    
    # Currently, new_list only includes the words that does not have the bad letters.

    #print(str(len(new_list)))
    print(Fore.GREEN+'\nHow much perfect letters (green) are in this word? (Enter a number)')
    ask = int(input('>> ')) # Here, we ask for how much perfect letters are in the word.

    if ask != 0: # If the answer is not 0 green words.
        for i in range(ask):
            print(Fore.GREEN+'\nWhat is this perfect letter? (Example: A)')
            perfect_letter = input('>> ')
    
            print('\nWhat spot from 1-5 is this letter in? (Enter a number 1-5)')
            perfect_letter_spot = int(input('>> '))
            for x in new_list:
                if str(x)[perfect_letter_spot - 1] ==  perfect_letter.lower():
                    pass # Word is good. 
                    real_list.append(x) # We append this to a new list with only the words we need.
                    
                else:
                    new_list.remove(str(x)) # We now removed the word in our list that doesn't have our perfect letter.
        
    #print(str(len(real_list)))

    print(Fore.YELLOW+'\nHow much good letters (yellow) are in this word? (Enter a number)')
    ask = int(input('>> '))

    for i in range(ask):
        print('\nWhat is this good letter? (Example: A)')
        good_letter = input('>> ')

        print('\nWhat spot from 1-5 is this letter in? (Enter a number 1-5)')
        good_letter_spot = int(input('>> '))

        for i in real_list:
            if str(i)[good_letter_spot - 1] ==  good_letter.lower(): # If good letter is in bad spot
                real_list.remove(i)
            else:
                pass

    if sumofwords == 0:
        for i in new_list:
            real_list.append(i)

    sumofwords = len(real_list)

    print(Fore.RESET+f'\nFound {sumofwords} possible words with this combo. Do you want to continue?\n(1) Yes\n(2) No')
    ask = input('>> ')
    
    if ask == '1':
        f= open(f'words.txt', 'w')

        string = ''
        for i in real_list:
            string += f'{i}\n'

        f.write(string)
        f.close()

        sumofwords = len(real_list)
        print(f'\nThere are currently {sumofwords} possible words. I have added every one of those words into a file in this directory titled "words.txt", use one of them on Wordle to continue.')
        
        print('')

        print('Now, we are going to start again with the guessing process. Make sure to enter every bad/perfect/good letter.')
        start()
        
    
if ask == '1':
    start()
elif ask == '2':
    random_word()
else:
    print(Fore.RED+'\nUnknown command!')
