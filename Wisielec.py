'''Klasyczna gra w wisielca. Komputer losowo wybiera słowo, a gracz
próbuje odgadnąć jego poszczególne litery. Jeśli gracz nie odgadnie w
porę całego słowa, mały ludzik zostanie powieszony.'''

import random

#stałe
HANGMAN=('''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''')

MAX_WRONG=len(HANGMAN)-1
WORDS=('MAGNEZ', 'KONTUSZ', 'SĘDZIA', 'KARAWELA', 'ŚWIECA')

word=random.choice(WORDS)  #słowo do odgadnięcia
so_far='-'*len(word)  #kreska zastępuje nieodgadniętą literę
wrong=0  #liczba nietrafionych liter
used=[]  #litery już użyte w zgadywaniu

print('Witaj w grze "Wisielec". Powodzenia!')

while wrong<MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print('Wykorzystałeś już następujące litery:\n', used)
    print('\nNa razie zagadkowe słowo wygląda tak:\n', so_far)

    guess= input('\nWprowadź literę:')
    guess= guess.upper()

    while guess in used:
        print('Już wykorzystałeś literę', guess)
        guess= input('Wprowadź literę:')
        guess= guess.upper()
    used.append(guess)

    if guess in word:
        print('\nTak! ', guess, ' znajduje się w zagadkowym słowie!')

        #nowa wersja zmiennej so_far, zawierająca odgadniętą literę
        new=""
        for i in range(len(word)):
            if guess==word[i]:
                new+=guess
            else:
                new+=so_far[i]
        so_far=new
    else:
        print('\nNiestety, ', guess, ' nie znajduje się w zagadkowym słowie.')
        wrong+=1
if wrong==MAX_WRONG:
    print(HANGMAN[wrong])
    print('\nZostałeś powieszony!')
else:
    print('Odgadłeś!')
print('Zagadkowe słowo to: ', word)