import random
import textwrap

width = 75
dottedLine = '-' * width
occupants = ['enemy', 'friend', 'unoccupied','perro']


def revealOccupants(userChoice, huts):
    ''' Reveal the ocupants of the hut'''
     # Print the occupant info
    print("Revealing the occupants...")

    # Leo el contenido de cada cabaña y si coincide con el seleccionado la pongo en negrita
    message = ""
    for i in range(len(huts)):
        ocupantInfo = "<%d:%s>"%(i+1,huts[i])
        # Marco en negrita la cabaña selecionada
        if userChoice == i+1:
           ocupantInfo = "\033[31m" + ocupantInfo + "\033[0m"
        message += ocupantInfo + " "
    print("\t" + message)
    print(dottedLine)

    #Muestro la cabaña seleccionada y dejo preparado para que se añada el resultado (end=' ')
    print("\033[1m" + "Entering hut %d ..." % (userChoice) +"\033[0m", end= ' ')

def showGameMission(dottedLine, width):
    # Presentacion
    print(dottedLine)
    print("\033[1m" + "Attack of the Orcs v.0.0.1: " +"\033[0m")


    initMessage = (
        'The war between humans and their arch enemies, the Orcs, was in the offing. A '
        'huge army of Orcs was heading toward the human establishments. They were '
        'virtually destroying everything in their way. The great kings of the human race '
        'joined hands to defeat their worst enemy for the great battle of their time. Men were '
        'summoned to join the rest of the army. Sir Foo, one of the brave knights guarding '
        'the southern plains, began a long journey toward the east, through an unknown '
        'dense forest. For two days and two nights, he moved cautiously through the thick '
        'woods. On his way, he spotted a small isolated settlement. Tired and hoping to '
        'replenish his food stock, he decided to take a detour. As he approached the village, he '
        'saw five huts. There was no one to be seen around. Hesitantly, he decided to enter a '
        'hut...'
    )
    print(textwrap.fill(initMessage,width= width))
    print("\033[1m" + "Mision: " +"\033[0m")
    print("\tChoose a hut where Sir Foo can rest...")
    print("\033[1m" + "TIP: " +"\033[0m")
    print("\tBe careful as there are enemies lurking around!")
    print(dottedLine)

def ocupyHuts():
    # Create a huts list and populate
    huts = []
    while len(huts) < 5:
        huts.append(random.choice(occupants))
    return huts



def getUserChoice():
    # Prompt the player to select a hut number
    userChoice = int(input("\033[1m" + "Choose a hut number [1-5]: " + "\033[0m"))
    return userChoice

def resultCombat(huts, userChoice):
    # Result of combat
    if huts[userChoice-1] == 'enemy':   
        print("\033[1m" + "You loose. Better luck next time" +"\033[0m")
    else:
       print("\033[1m" + "Congratulations: You win!!. " +"\033[0m")
    
    print(dottedLine)

    

showGameMission(dottedLine,width)

#While the user wishes to keep playing the game
keepPlaying = 'y'
while (keepPlaying == 'y'):

    huts = ocupyHuts()
    userChoice = getUserChoice()
    revealOccupants(userChoice,huts)
    resultCombat(huts,userChoice)

    keepPlaying = input('Continue playing? [y/n]: ')





    

