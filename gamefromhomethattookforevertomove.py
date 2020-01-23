import sys
import colorama
from colorama import Fore, Back, Style
import os
import random
import code

class Robot:
    """Robot status"""

    def __init__(self, love, knowledge, kindness, happiness, money=10):
        self.love = love
        self.knowledge = knowledge
        self.kindness = kindness
        self.happiness = happiness
        self.money = money

    #def gain_love(self):
        #self.love +=4
        #return love
    #def gain_knowledge(self):
        #knowledge +=2
        return #knowledge
    #def gain_kindness(self):
        # kindness +=2
        return #kindness
    #def gain_happiness(self):
        #happiness +=2
        return #happiness
#a list with two options to select from
options_two = ["1","2"]
def title_screen_options():
    """gives options for the player to choose from, like whether or not to start or exit the game"""
    option= input("> ")
    #gets rid of any bad or invalid inputs like "potato" or numbers.
    while option.lower() not in ['play','about','quit']:
        option = input("Please enter play/about/quit >  ")
    if option.lower() == ("play"):
        print("placeholder")
        #calls the function that starts the gameplay
        #start_game() #placeholder
    elif option.lower() == ("about"):
        #shows an about screen that gives a short detail about the game
        about_screen()
    elif option.lower() == ("quit"):
        #exits the game
        print("Goodbye (._.)")
        sys.exit()

def title_screen():
    """Gives a title screen format that shows the options for the player to choose from"""
    #clears the current screen
    os.system('cls')
    #all uses of Fore.(Color) are from colorama, it just changes the color of the upcoming text
    print(Fore.CYAN + "####################################")
    print("##########" + Fore.WHITE + "   Hello World   " + Fore.CYAN + "#########")
    print("####################################")
    print(Fore.WHITE + '               -Play-           ')
    print(Fore.WHITE + '               -About-          ')
    print(Fore.WHITE + '               -Quit-           ')
    #calls back the function that gives an ability to choose an option
    title_screen_options()

def about_screen():
    """ The about screen that gives a short summary of the game """
    os.system('cls')
    print(Fore.CYAN + "####################################")
    print("##########" + Fore.WHITE + "   Hello World   " + Fore.CYAN + "#########")
    print("####################################")
    print(Fore.WHITE + "A wholesome adventure with a robot pal!")
    title_screen_options()


def beforeinstructions():
    """first part of story, introduction and intro to rules"""
    os.system('cls')
    response = ""
    print(Fore.CYAN + "####################################" + Style.RESET_ALL)
    print("The sun shines through the windows. You stir awake and wonder why you're laying on the couch in your own apartment.")
    print("You look around the living room and the coffee table is strewn with blueprints and notepads filled with rough sketches.")
    print("Oh, right. Your inventor friend was stopping by on their way to a convention in the big city, and you offered to let them stay over so you could catch up and talk.")
    print("You should probably start the day.")
    print("You have two options.")
    print(Fore.CYAN + "####################################" + Style.RESET_ALL)
    option1 = "1. Get off the couch"
    option2 = "2. Bleh, 5 more minutes"
    print(Fore.YELLOW + option1)
    print(Fore.YELLOW + option2 + Style.RESET_ALL)
    while True:
        response = input("1 or 2? > ")
        if response == "1":
            os.system('cls')
            print(Fore.CYAN + "####################################" + Style.RESET_ALL)
            print("You get off of the couch and take a good stretch. You open up the windows to let some air in, then turn around to look at the clock. Oh. It's 5 am.")
            print("Your friend is definitely still asleep. You look around for things to do.")
            print("There's the" + Fore.YELLOW + " tv," + " bookshelf," + Style.RESET_ALL + " and the" +Fore.YELLOW + " mess" + Style.RESET_ALL + " on the table.")
            print("There's also a piece of paper with your handwriting. A note to yourself.")
            print(Fore.GREEN + "Remember to buy eggs. You can interact with things by typing" + Fore.YELLOW + " -Look- and -Touch- Try looking at the tv!")
            print("Weird..." + "(If you ever get lost, just type in" + Fore.YELLOW + " Help)" + Style.RESET_ALL)
            print(Fore.CYAN + "####################################" + Style.RESET_ALL)
            break
        #skip_morning = False
        elif response == "2":
            print("Thisheckin elif caused me so many problems")
        else:
            print("Just type in numbers 1 or 2.")
        #skip_morning = True

def bookshelffun():
    """Small choice made into a function just to separate parts"""
    options_four = ["1","2","3","4"]
    books = ['1. The Lobster Who Could', '2. 101 Ways to Eat Grass', '3. Alan Brinkley American History 13th Edition', "4. Chunky Chicken's Birthday Party"]
    bookchoice = input("Which one? > ")
    while bookchoice not in options_four:
        bookchoice = input("A number 1-5, please.")
    if bookchoice == "1":
        print("Ah yes, a fine choice.")
        print("You flip through the book and place   >" + (books[0]) + "<   on the couch")
    if bookchoice == "2":
        print("Ah yes, good for future reference.")
        print("You flip through the book and place   >" + (books[1]) + "<   on the couch")
    if bookchoice == "3":
        print("Ah yes, a fine choice.")
        print("You flip through the book and place   >" + (books[2]) + "<   on the couch")
    if bookchoice == "4":
        print("Ah yes, your favorite.")
        print("You flip through the book and place   >" + (books[3]) + "<   on the couch")


    #return skip_morning
def after_instructions():
    """After instructions are given, allows for more free exploration"""
    print(Fore.CYAN + "####################################" + Style.RESET_ALL)
    optionsafterinstructions = ['look at tv', 'touch tv', 'look at bookshelf', 'touch bookshelf', 'look at mess', 'touch mess', 'help']
    response = ""
    books = ['1. The Lobster Who Could', '2. 101 Ways to Eat Grass', '3. Alan Brinkley American History 13th Edition', "4. Chunky Chicken's Birthday Party"]
    print("There's the" + Fore.YELLOW + " tv," + " bookshelf," + Style.RESET_ALL + " and the" +Fore.YELLOW + " mess" + Style.RESET_ALL + " on the table.")
    while True:
        response = input("What now? > ").lower()
        if response == "look at tv":
            print("Yep. That's a tv alright.")
        elif response == "touch tv":
            print("You turn it on and you watch the news about the upcoming convention. It's a day away and supposed to showcase all the newest technological innovations. You'd go but... probably not. You could always change your mind though.")
        elif response == "look at bookshelf":
            print("It's a pretty colorful collection of books. You gaze cheerfully upon the little knickknacks there as well.")
        elif response == "touch bookshelf":
            print("You run your fingers over all the spines of the books, wondering which one to take.")
            print (books)
            print(Fore.CYAN + "####################################" + Style.RESET_ALL)
            bookshelffun()
        elif response == "touch mess":
            print("It's an organized mess, not for you to touch.")
        elif response == "look at mess":
            print("It's a bunch of blueprints of contraptions that you can't understand. Your friend must have left them there after trying to plan a presentation. You don't dare to touch them. By looking at the table, you find that your phone isn't there. Maybe you left it on the" + Fore.YELLOW + " couch?" + Style.RESET_ALL + " Maybe it's in the" + Fore.YELLOW + " kitchen?" + Style.RESET_ALL)
            break
        elif response == "help":
            print(f"Available options: {optionsafterinstructions}")
        else:
            print("You seem confused. Try again")

    #newoptions = ['touch couch', 'look at couch', 'go to kitchen', 'help']
    while True: 
        response = input("What would you like to do? > ").lower()
        if response == "touch couch":
            print("It's so soft. You don't find your phone in between the cushions, but you find some money! Nice!")
        elif response == "look at couch":
            print("It has a very visible indent of you.")
        elif response == "help":
            print("Hm, did you find your phone yet? If so, then maybe it's time to" + Fore.GREEN + " go to" + Fore.WHITE + " the" + Fore.GREEN + " kitchen?" + Style.RESET_ALL)
        elif response == "go to kitchen":
            print("You walk into the kitchen.")
            break
        else: 
            print("You seem confused. Try again?")

def scenetwokitchen():
    """Player just got to the kitchen"""
    response =""
    os.system('cls')
    print(Fore.CYAN + "####################################" + Style.RESET_ALL)
    print("You look around the kitchen, and you find your bag and phone on the countertop. You take them with you. Your phone says it's now 6 am. Hm. Maybe you should make some breakfast?")
    option1 = "1. Yes."
    option2 = "2. Yes YES"
    print(Fore.YELLOW + option1)
    print(Fore.YELLOW + option2 + Style.RESET_ALL)
    response = input("Option 1 or 2? > ")
    while response not in options_two:
        response = input("Number 1, or Number 2? >  ")
    if response in options_two:
        print(Fore.CYAN + "####################################")
        print(Fore.MAGENTA + "-BREAKFAST START-")
        print(Fore.CYAN + "####################################" + Style.RESET_ALL)
        print("It was an intense battle. Batter was flying, pancakes were flipping, but you made the perfect breakfast.")
    print(Fore.CYAN + "####################################" + Style.RESET_ALL)
    print("You look at the clock, it's 7:30 am. Huh. You could've sworn they had to leave at 7. Suddenly, the bedroom door bursts open.")
    print(Back.WHITE + Fore.BLACK + "Hi!! Sorry, I gotta go! I slept in!" + Style.RESET_ALL)
    print("They slide all their papers from the table into their suitcase and head out the door.")
    print(Back.WHITE + Fore.BLACK + "I'll call you later! Thank you!" + Style.RESET_ALL)
    print("Huh. You'll miss them. You head back to the couch with your breakfast and plop down.")

def meetbuddy(): 
    response = ""
    #meetbuddyoptions = ['look under the table', 'touch switch', 'touch robot', 'look robot']
    print(Fore.CYAN + "####################################" + Style.RESET_ALL)
    print(Back.GREEN + "Thump" + Style.RESET_ALL)
    print("Your foot hit something" + Fore.YELLOW + " under the table." + Style.RESET_ALL)
    response = input("What do you do? >  ").lower()
    if response == "look under the table":
        print("Oh, it's a metal box of some sort. You lean down to inspect it. It has rounded edges, and upon closer inspection, there's a small" + Fore.YELLOW + " switch" + Fore.WHITE + " on the side.")
    else:
        response = input("You're very curious to" + Fore.YELLOW + " see" + Style.RESET_ALL + " what is" + Fore.YELLOW + " under the table." + Style.RESET_ALL)
    response = input("That switch looks interesting...what does it do? > ").lower()
    if response == "touch switch":
        print("You hear a small whirring... is the box getting taller?")
    else:
        response = input("You're dying to" + Fore.YELLOW + " touch" + Fore.WHITE + " the switch. >  ").lower()
    print("You watch as it props itself up, and sprouts arms and legs. You crawl up onto the couch as an attempt of self-preservation.")
    print("A small tune starts to play as a display turns on.")
    print("Two words show up on the screen.")
    print(Fore.CYAN + "####################################")
    print("##########" + Fore.WHITE + "   Hello World   " + Fore.CYAN + "#########")
    print("####################################"  + Style.RESET_ALL)
    print("The screen changes to show two round eyes and a smile. It eyes you curiously. What a cute" + Fore.YELLOW + " robot." + Fore.WHITE)
    while True:
        response = input("It feels like you should do something... > ").lower()
        if response == "touch robot":
            print("It takes your hand in response and chirps happily.")
        elif response == "look at robot":
            print("It sings it's little tune happily and looks at you in wonder and... adoration? Don't get attached! It isn't yours.")
            break
        else:
            print("It looks confused at whatever you tried to attempt. Try again.")
    print("Speaking of getting attached... Your inventor friend is probably halfway across town by now! You gotta return it! You hastily shove your belongings into your bag and sweep up the bot. You head out the door together in a rush.")
def buddydevelopment():
    """Phone ability, allows user to check in on robot friend any time they wish"""
    os.system('cls')
    #all uses of Fore.(Color) are from colorama, it just changes the color of the upcoming text
    print(Fore.BLUE + "####################################")
    print("########" + Fore.WHITE + "   Protoype Vers. 1   " + Fore.BLUE + "######")
    print("####################################")
    print(Fore.WHITE + '               -Love-         ')
    print(self.love)
    print(Fore.WHITE + '               -Knowledge-          ')
    print(Fore.WHITE + '               -Kindness-           ')
    print(Fore.WHITE + '               -Happiness-           ')
    print(Fore.WHITE + '               -Money-           ')

def bikeride():
    print(Fore.CYAN + "####################################" + Style.RESET_ALL)
    print("It's still early morning and you look around frantically for the inventor, robot in hand. Ugh. Their car is gone.")
    print("On the curb you spot a few loose" + Fore.YELLOW + " papers" +Fore.WHITE + " and their" + Fore.YELLOW + " phone." + Style.RESET_ALL + " So much for calling them.")
    #optionsbikeride = ['look papers','look phone', 'touch papers','touch phone']
    while True:
        response = input("The inventor's items catch your eye. > ").lower()
        if response == "look at papers" or response == "touch papers":
            print("The papers read: -prototype vers. 1-")
            print("Mission: to learn and observe. A.I changes in correspondance to traits Love, Knowledge, Kindness, Happiness")
        elif response == "look at phone" or response == "touch phone":
            print("It must be because it's close to the robot, but the screen changes to show several traits.")
            print("(Congrats on unlocking the phone! You can use it at any time by typing" + Fore.GREEN + " use phone.)" + Style.RESET_ALL)
            print("It also shows you how much money you have... you won't ask why or how.")
            print("You map out the path to the city in your head. You'd need to go to the marketplace, then take the bus all the way to the piers. Then you'd have to take a ferry. How much did that cost again? Agh less thinking, more doing!")
            print("You take your bike, plop the robot into the basket, and head towards the market.")
            break
def bondingmomentducks():
    print(Fore.CYAN + "####################################" + Style.RESET_ALL)
    print("You can see the colorful tops of the marketplace stands coming into view as you ride your bike over a bridge.")
    print("The robot leans over the basket to peer at the yellow blurbs in the distance, and chirps happily.")
    print("You have two options.")
    option1 = "1. Stop to look at the ducks."
    option2 = "2. Chirp along with the robot."
    print(Fore.YELLOW + option1)
    print(Fore.YELLOW + option2 + Style.RESET_ALL)
    while True:
        response = input("Option 1 or 2? >  ")
        if response == "1":
            print("You tell the robot all that you know about ducks as you watch them waddle.")
            print(" +Love     +Happiness     +Knowledge")

        elif response =="2":
            print("You chirp back and forth like there's no tomorrow.")
            print(" +Love     +Happiness")
#def scenekitchen():
buddydevelopment()
title_screen()
#def start_game():
beforeinstructions()
after_instructions()
scenetwokitchen()
meetbuddy()
bikeride()

#if skip_morning == False:
    #afterinstructions()
    #scenekitchen()
#elif skip_morning == True:
    #print("You wake up hungry an hour later, so you move to the kitchen.")
    #scenekitchen()
