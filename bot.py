import json
from datetime import date

today = date.today()
d1 = today.strftime("%m/%d/%Y")

print(
    """
    
░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░██╗░░░░░███████╗  ░██████╗░██╗░░░██╗███████╗░██████╗░██████╗██████╗░
░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗██║░░░░░██╔════╝  ██╔════╝░██║░░░██║██╔════╝██╔════╝██╔════╝██╔══██╗
░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║██║░░░░░█████╗░░  ██║░░██╗░██║░░░██║█████╗░░╚█████╗░╚█████╗░██████╔╝
░░████╔═████║░██║░░██║██╔══██╗██║░░██║██║░░░░░██╔══╝░░  ██║░░╚██╗██║░░░██║██╔══╝░░░╚═══██╗░╚═══██╗██╔══██╗
░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝███████╗███████╗  ╚██████╔╝╚██████╔╝███████╗██████╔╝██████╔╝██║░░██║
░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚══════╝  ░╚═════╝░░╚═════╝░╚══════╝╚═════╝░╚═════╝░╚═╝░░╚═╝
"""
)

print(f'\nWelcome to Wordle on {d1}!')

new_list = []

def continue_process():
    f= open(f'words.txt', 'w')

    string = ''
    for i in new_list:
        string += f'{i}\n'

    f.write(string)
    f.close()

    sumofwords = len(new_list)
    print(f'\nThere are currently {sumofwords} possible words. I have added every one of those words into a file in this folder titled "words.txt", use one of them on Wordle to continue.')
    
    print('')

    ask = input('Enter your chosen word: ')


def start():
    print('\nWhat is your current word in wordle?')
    current_word = input('>> ')
    if len(current_word) != 5:
        print('This word is not 5 characters! Make sure to enter a 5 letter word.\nI will be restarting the process now.\n\n')
        return start()

    print('\nWhat are the bad letters in this word? (Example: ABC)')
    bad_letters = input('>> ')
    
    a_file = open(f"all_words.json", "r")
    json_object = json.load(a_file)
    a_file.close()
    
    sumofwords = 0

    for i in json_object:
        if any(ext in bad_letters for ext in i):
            pass
        else:
            new_list.append(i.lower())
            #sumofwords += 1
            #print(f'Found possible word: {i}')
    
    print('\nHow much good letters (green) in this word? (Enter a number)')
    ask = int(input('>> '))

    good_letters = ''
    for i in range(ask):
        print('\nWhat is this good letter? (Example: A)')
        good_letter = input('>> ')

        print('\nWhat spot from 1-5 is this letter in? (Enter a number 1-5)')
        good_letter_spot = int(input('>> '))
        for i in new_list:
            if good_letter in i[0:good_letter_spot]:
                pass # Word is good. 
            else:
                new_list.remove(i)

        good_letters += good_letter.lower()
        
    for i in new_list:
        if any(ext in good_letters for ext in i):
            pass #Word is good
        else:
            if i in new_list:
                new_list.remove(i)

    sumofwords = len(new_list)

    print(f'\nFound {sumofwords} possible words with this combo. Do you want to continue?\n(1) Yes\n(2) No')
    ask = input('>> ')

    if ask == '1':
        continue_process()
        
    
start()
