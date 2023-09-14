#!/usr/local/bin/python3.11
# Start of game

# class to edit text when printing
# the variables below are used in text to change the properties of the text
# e.g print("\033[1mThis text is bold.\033[0m")
# I have made it a class so that it is easier to use and i do not have to remember the codes
# also python does not let you use backslashes in f-strings, which i have used througout the game.
import random
import time

class textEdit:
   blue = '\033[94m'
   bold = '\033[1m'
   underline = '\033[4m'
   purple = '\033[95m'
   green = '\033[32m'
   red = '\033[31m'
   end = '\033[0m'

# print the title of the game using ascii art and make it blue using the class above
print(f"""

{textEdit.blue}

████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ██╗         ██╗   ██╗██╗██████╗ ████████╗██╗   ██╗ ██████╗ ███████╗██╗████████╗██╗   ██╗
╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██║         ██║   ██║██║██╔══██╗╚══██╔══╝██║   ██║██╔═══██╗██╔════╝██║╚══██╔══╝╚██╗ ██╔╝
   ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║██║         ██║   ██║██║██████╔╝   ██║   ██║   ██║██║   ██║███████╗██║   ██║    ╚████╔╝ 
   ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║██║         ╚██╗ ██╔╝██║██╔══██╗   ██║   ██║   ██║██║   ██║╚════██║██║   ██║     ╚██╔╝  
   ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║███████╗     ╚████╔╝ ██║██║  ██║   ██║   ╚██████╔╝╚██████╔╝███████║██║   ██║      ██║   
   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝      ╚═══╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚═╝   ╚═╝      ╚═╝   
                                                                                                                                                 
{textEdit.end}

""")

def GuitarChoice():
    guitarchoice = input('> ')
    global guitar
    if guitarchoice.lower().strip() == 'a':
        guitar = ['strat', "Stratocaster"]
    elif guitarchoice.lower().strip() == 'b':
        guitar = ["lespaul", "Les Paul"]
    else:
        print("Sorry, I dont know which guitar you want. Please choose one of the options presented.")
        GuitarChoice()


def GameStats():
    global GuitarMove
    global stamina
    global crowd

    if stamina <= 250 or crowd <= 250:
       time.sleep(0.5)
       gameRestart = input("""\nOh no! Unfortunately the crowd was not too impressed by your guitar playing and quickly got bored as they booed you off the stage.
Would you like to play again or quit? (Type 'r' to restart or any other button to quit. ): """)
       if gameRestart.lower().strip() == "r":
          print("Restarting the game")
          time.sleep(1)
          print("Since you've already had a go at this game you don't need to read")
          yearchoice()
       else:
          print("Quitting the game")
          time.sleep(1)
          exit()

    print(f"""
┌──────────────────────────────────────┐   
│{textEdit.bold} STATS {textEdit.end}                               │
├──────────────────────────────────────┤   
│                                      │
│ {textEdit.underline}Stamina{textEdit.end}:              {textEdit.purple}{stamina}{textEdit.end}            │
│                                      │
│ Stamina is how much energy you have. │
│ This affects how you well you play.  │
│                                      │
│                                      │
│ {textEdit.underline}Crowd Engagement{textEdit.end}:     {textEdit.purple}{crowd}{textEdit.end}            │                                   
│                                      │
│ Crowd engagement is how much the     │
│ crowd is interested in your guitar   │
│ playing and how much they like it.   │
│                                      │
└──────────────────────────────────────┘
""")
    GuitarMove = int(input(f"""{textEdit.bold}{textEdit.underline}Moves{textEdit.end}\n
{textEdit.bold}\tBlues Lick{textEdit.end}
You play an epic blues lick (1)

{textEdit.underline}Stamina{textEdit.end}:\t\t{textEdit.red}- 25{textEdit.end}
{textEdit.underline}Crowd Engagement{textEdit.end}:\t{textEdit.green}+ 75{textEdit.end}

 
{textEdit.bold}\tBehind Your Head{textEdit.end}
Play the guitar behind your head and shock the crowd (2)

{textEdit.underline}Stamina{textEdit.end}:\t\t{textEdit.red}- 50{textEdit.end}
{textEdit.underline}Crowd Engagement{textEdit.end}:\t{textEdit.green}+ 150{textEdit.end}

 
{textEdit.bold}\tTake A Break{textEdit.end}
You take a quick break to recharge your stamina (3)

{textEdit.underline}Stamina{textEdit.end}:\t\t{textEdit.green}+ 100{textEdit.end}
{textEdit.underline}Crowd Engagement{textEdit.end}:\t{textEdit.red}- 150{textEdit.end}

> """))

    if GuitarMove == 1:
        stamina -= 25
        crowd += 75
        GameStats()
    elif GuitarMove == 2:
        stamina -= 50
        crowd += 150
        GameStats()
    elif GuitarMove == 3:
        stamina += 100
        crowd -= 150
        GameStats()

# sixties
def sixties():
    global crowd
    global stamina
    
    print("""
You have chosen to travel back to the 60s! You suddenly see youself fading away as you then open your eyes and yourself at woodstock '69!
You look up and you see your opponent who is ready to challange you to a guitar battle. Your opponent is none other than Jimi Hendrix!
Before you step up on stage, you first need to decide What guitar you will be choosing. Your options are either a Fender Stratocaster (A) or a Gibson Les Paul (B).
The Gibson les paul sounds better, but the Stratocaster is easier to play and lighter, so less fatiguing to use, so choose wisely!""")

    GuitarChoice()

    print((f"""
So {name}, you've decided to go with the {guitar[1]}? Good choice, but lets see how well it does going against Jimi Hendrix!
He picks up his guitar and puts the strap around his shoulder, getting ready to shock the audience!"""))
    
    print(f'Hendrix pics up the mic and says to you "Alright {name}, lets see what you got. You go first. Good luck!"')

    crowdRandom = random.randint(-50,50)

    if guitar[0] == "strat":
        stamina = 700
        crowd = 500 + crowdRandom
    elif guitar[0] == "lespaul":
        stamina = 500
        crowd = 700 + crowdRandom
    print(guitar[0])
        
    GameStats()


# seventies
def seventies():
    global crowd
    global stamina

    print("""
You have chosen to travel back to the 70s! You suddenly see youself fading away as you then open your eyes and yourself at Pink Floyd's performance in pompeii in '72!
You look up and you see your opponent who is ready to challange you to a guitar battle. Your opponent is none other than David Gilmour!
Before you step up on stage, you first need to decide What guitar you will be choosing. Your options are either a Fender Stratocaster (A) or a Gibson Les Paul (B).
The Gibson les paul sounds better, but the Stratocaster is easier to play, so choose wisely!""")

    GuitarChoice()

    print(f"""So {name}, you've decided to go with the {guitar[1]}? Good choice, but lets see how well it does going against David Gilmour!
He picks up his guitar and puts the strap around his shoulder, getting ready to shock the audience!""")

    print(f'Hendrix pics up the mic and says to you "Alright {name}, lets see what you got. You go first. Good luck!"')

    crowdRandom = random.randint(-50,50)

    if guitar[0] == "strat":
        stamina = 700
        crowd = 500 + crowdRandom
    elif guitar[0] == "lespaul":
        stamina = 500
        crowd = 700 + crowdRandom
    print(guitar[0])

    GameStats()

    if stamina >= 250:
       GameStats()

# eighties
def eighties():
    global crowd
    global stamina

    print("""
You have chosen to travel back to the 80s! You suddenly see youself fading away as you then open your eyes and yourself at Eddie Van Halen's 5150 tour!
You look up and you see your opponent who is ready to challange you to a guitar battle. Your opponent is none other than Eddie Van Halen himself!
Before you step up on stage, you first need to decide What guitar you will be choosing. Your options are either a Fender Stratocaster (A) or a Gibson Les Paul (B).
The Gibson les paul sounds better, but the Stratocaster is easier to play, so choose wisely!""")

    GuitarChoice()

    print(f"""So, you've decided to go with the {guitar[1]}? Good choice, but lets see how well it does going against Jimi Hendrix!
He picks up his guitar and puts the strap around his shoulder, getting ready to shock the audience!""")

    print(f'Hendrix pics up the mic and says to you "Alright {name}, lets see what you got. You go first. Good luck!"')

    crowdRandom = random.randint(-50,50)

    if guitar[0] == "strat":
        stamina = 700
        crowd = 500 + crowdRandom
    elif guitar[0] == "lespaul":
        stamina = 500
        crowd = 700 + crowdRandom
    print(guitar[0])

    GameStats()

    if stamina >= 250:
       GameStats()


# Ask for users name and introduces backstory
name = input("Welcome to Terminal Virtuosity! Before we start, what is your name? ")

print(f"""
Well, {name}, I have an exciting quest for you! While looking through an old garage sale you come across a very special guitar. 
You decide to pick it up and strum a chord before you vanish into thin air, being sent to what seems like outer space. 
You look around and you can see all the stars and planets, yet you are able to move around freely and comfortably, despite not being a in a spacesuit.
Out of nowhere, you hear a deep voice, presenting you with three options.
The voice gives you the power to be sent to a certain timeline and be able to play against guitarists of different eras.""")


def yearchoice():
    year = input("The three choices you have been given are to be sent to the 60s, 70s or 80s (Type 60, 70 or 80): ")
    match year: 
        case '60':
            sixties()
        case '70':
            seventies()
        case '80':
            eighties()
        case _:
            print("\nSorry, I don't know what decade you want me to send you back to. Please try again and choose one of the options you are presented with.")
            yearchoice()
yearchoice()
