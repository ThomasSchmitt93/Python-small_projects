word = 'funny'
guess = ''
list_guessed_word = list(guess.ljust(len(word),'_'))
guessed_word = ''.join(list_guessed_word)
guessed_word_previous = ''.join(list_guessed_word)
index = 0

guess_count = 0
guess_limit = 10
out_of_guesses = False

for i in range(len(word)):
    print('_', end = '')
print('')
print('')

while guessed_word != word and not(out_of_guesses):
    
    if guess_count < guess_limit:
        print('')
        guess = input('guess a letter! ')
        for letter in word:
            if letter == guess:
                list_guessed_word[index] = guess
                index = index + 1 
            else:
                index = index + 1
        index = 0
        print('')
        guessed_word = ''.join(list_guessed_word)

        if guessed_word == guessed_word_previous:
            guess_count = guess_count + 1
        else:
            guessed_word_previous = guessed_word

        if guess_count == 0:
            print( '')
            print( '')
            print( '')
            print( '')
            print( '')
            print( '')
            print( '')
        elif guess_count == 1:
            print( '')
            print( '')
            print( '')
            print( '')
            print( '')
            print( '')
            print( '/')
        elif guess_count == 2:
            print( '')
            print( '')
            print( '')
            print( '')
            print( '')
            print( '')
            print( '/\\')
        elif guess_count == 3:
            print( '')
            print( '|  ')
            print( '|  ')
            print( '|  ')
            print( '|  ')
            print( '|  ')
            print( '/\\')
        elif guess_count == 4:
            print( '-----')
            print( '|   ')
            print( '|   ')
            print( '|   ')
            print( '|   ')
            print( '|   ')
            print( '/\\')
        elif guess_count == 5:
            print( '-----')
            print( '|   |')
            print( '|    ')
            print( '|    ')
            print( '|    ')
            print( '|    ')
            print( '/\\')
        elif guess_count == 6:
            print( '-----')
            print( '|   |')
            print( '|   o')
            print( '|    ')
            print( '|    ')
            print( '|    ')
            print( '/\\')
        elif guess_count == 7:
            print( '-----')
            print( '|   |')
            print( '|   o')
            print( '|   |')
            print( '|   |')
            print( '|    ')
            print( '/\\')
        elif guess_count == 8:
            print( '-----')
            print( '|   |')
            print( '|   o')
            print( '|  \\|/')
            print( '|   |')
            print( '|    ')
            print( '/\\')
        elif guess_count == 9:
            print( '-----')
            print( '|   |')
            print( '|   o')
            print( '|  \\|/')
            print( '|   |')
            print( '|   /')
            print( '/\\')
        print( '')
        print(guessed_word)

    else:
        out_of_guesses = True

if out_of_guesses:
    print( '')
    print('You loose!')
    print( '-----')
    print( '|   |')
    print( '|   o')
    print( '|  \\|/')
    print( '|   |')
    print( '|   /\\')
    print( '/\\')
else:
    print( '')
    print('You win!')