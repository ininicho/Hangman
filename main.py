##HANGMAN
country = 'INDONESIA'
country_list = ['I','N','D','O','N','E','S','I','A']
display = '*********'
hint = 'NUSA'
i = 0

print('Welcome to Hangman!')
choice  = input('''
To read Instructions, enter I
To show Hint, enter H
To directly play, press [ENTER]
''')

if choice == 'I':
  print(open('instructions.txt').read())
elif choice == 'H':
  print('Hint: ' + hint)

while i<5:
    print('==================')
    print('HANGMAN!\n')
    print(display + '\n')
    guess = input('Your Guess :')

    if guess == country:
        print('\nCorrect!')
        print('==================')
        break

    elif (guess in country_list):
        for n in range(len(country)):
            if guess == country_list[n]:
                display = display[0:n] + guess + display[n+1:]
        print('\n'+ display)
        print('Letter correct!')
        if display == country:
            input('Puzzle Solved! The secret word is ' + country)
            break
    else:
        i+=1
        print('\nWrong! Life remaining: ' + str(5-i))

if display != country and guess != country:
    input('You Lose! Puzzle not solved')