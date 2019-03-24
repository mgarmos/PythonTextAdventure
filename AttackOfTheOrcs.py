import random

occupants = ['enemy', 'friend', 'unoccupied']

#While the user wishes to keep playing the game
keepPlaying = 'y'
while (keepPlaying == 'y'):

    # Create a huts list and populate
    huts = []
    while len(huts) < 5:
        huts.append(random.choice(occupants))

    # Prompt the player to select a hut number
    userChoice = int(input('Choose a hut number [1-5]: '))

    # Result of combat
    if huts[userChoice-1] == 'enemy':
        print('you loose')
    else:
       print('you win')

    print(huts)
    keepPlaying = input('Continue playing? [y/n]: ')
    

