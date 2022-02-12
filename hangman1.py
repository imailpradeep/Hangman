import random, hangman_art, hangman_words

from hangman_words import word_list
from hangman_art import stages, logo

chosen_word = random.choice(word_list)

blanks = []
for letter in chosen_word:
  blanks += '_'
print(blanks)

hangman = 'hangman'
hangman_count = 0

print(logo)

while '_' in blanks:
  
  guess = input("Guess a letter: ").lower()
  
  for i in range(len(chosen_word)):
    if chosen_word[i] == guess:
      blanks[i] = guess
    
  if guess not in chosen_word:
    #print(hangman[hangman_count])
    print(stages[hangman_count])
    hangman_count += 1

  if hangman_count == 7:
    print('try again')
    print(logo)
    break

  print(blanks)
  print('\n')

if (hangman_count < 7):
  print('you have successfully completed it')
  print(logo)
