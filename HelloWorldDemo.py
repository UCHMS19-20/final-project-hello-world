import sys
#allows the ability to quit the program
import colorama
from colorama import Fore, Back, Style
#Colorama allows text to change color
import os
#Can use operating system commands, like clearing the screen (which is used)

#lists with two options to select from
options_two = ["1","2"]
#yes or no list
yes_no = ["yes","no"]

class Robot:
    """Robot status, shows statistics of traits"""

    def __init__(self, love, knowledge, kindness, happiness, money=10):
        """Several traits of the robot pal; values can change throughout the story"""
        self.love = love
        self.knowledge = knowledge
        self.kindness = kindness
        self.happiness = happiness
        self.money = money

    def add_stat(self, stat, amount):
        """adds a value to the stat of the robot's trait"""
        if stat == "love":
            self.love += amount
        elif stat == "knowledge":
            self.knowledge += amount
        elif stat == "kindness":
            self.kindness += amount
        elif stat == "happiness":
            self.happiness += amount
        elif stat == "money":
            self.money += amount

    def set_stat(self, stat, amount):
        """sets the status to a specific amount"""
        if stat == "love":
            self.love == amount
        elif stat == "knowledge":
            self.knowledge == amount
        elif stat == "kindness":
            self.kindness == amount
        elif stat == "happiness":
            self.happiness == amount
        elif stat == "money":
            self.money == amount

bot = Robot(0, 0, 0, 0)
#the stats of the robot

def title_screen_options():
    """gives options for the player to choose from, like whether or not to start or exit the game"""
    #gives ability to put an input
    option= input("> ")
    #gets rid of any bad or invalid inputs like "potato" or numbers.
    while option.lower() not in ['play','about','quit']:
        #if input not in list of inputs, then ability to input again is given until valid input is typed
        option = input("Please enter play/about/quit >  ")
    if option.lower() == ("play"):
        print("Yay!")
        #if input is equal to play, moves code along to start gameplay
    elif option.lower() == ("about"):
        #shows an about screen that gives a short detail about the game
        about_screen()
    elif option.lower() == ("quit"):
        #exits the game, says goodbye, and exits the system
        print("Goodbye (._.)")
        sys.exit()

def title_screen():
    """Displays a title screen format that shows the options for the player to choose from"""
    #clears the current screen
    os.system('cls')
    #all uses of Fore.(Color) are from colorama, it changes the color of the upcoming text
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
    #clears screen to avoid crowding
    os.system('cls')
    print(Fore.CYAN + "####################################")
    print("##########" + Fore.WHITE + "   Hello World   " + Fore.CYAN + "#########")
    print("####################################")
    print(Fore.WHITE + "A wholesome adventure with a robot pal!")
    title_screen_options()


def beforeinstructions():
    """first part of story, introduction and intro to rules"""
    os.system('cls')
    #adds a border to separate main text from commands
    print(Fore.CYAN + "####################################" + Style.RESET_ALL)
    print("The sun shines through the windows. You stir awake and wonder why you're laying on the couch in your own apartment.")
    print("You look around the living room and the coffee table is strewn with blueprints and notepads filled with rough sketches.")
    print("Oh, right. Your inventor friend was stopping by on their way to a convention in the big city, and you offered to let them stay over so you could catch up and talk.")
    print("You should probably start the day.")
    print("You have two options.")
    print(Fore.CYAN + "####################################" + Style.RESET_ALL)
    #sets two valid choices to names option1 and option2
    option1 = "1. Get off the couch"
    option2 = "2. Bleh, 5 more minutes"
    #displays options in colored text
    print(Fore.YELLOW + option1)
    print(Fore.YELLOW + option2 + Style.RESET_ALL)
    #Creates a loop in which the user is confronted with a repeating input that branches off into different scenarios
    #If response is not 1 or 2, then asks user to retry
    while True:
        response = input("1 or 2? > ")
        if response == "1":
            os.system('cls')
            print(Fore.CYAN + "####################################" + Style.RESET_ALL)
            print("You get off of the couch and take a good stretch. You open up the windows to let some air in, then turn around to look at the clock. Oh. It's 5 am.")
            print("Your friend is definitely still asleep. You look around for things to do.")
            #text styles change in text to help indicate what to do
            print("There's the" + Fore.YELLOW + " tv," + " bookshelf," + Style.RESET_ALL + " and the" +Fore.YELLOW + " mess" + Style.RESET_ALL + " on the table.")
            print("There's also a piece of paper with your handwriting. A note to yourself.")
            print(Fore.GREEN + "Remember to buy eggs. You can interact with things by typing" + Fore.YELLOW + " -Look- and -Touch- Try looking at the tv!")
            print("Weird..." + "(If you ever get lost, just type in" + Fore.YELLOW + " Help)" + Style.RESET_ALL)
            print(Fore.CYAN + "####################################" + Style.RESET_ALL)
            break
        elif response == "2":
            print("You fell asleep again.")
            print("You wake up groggily a bit later.")
            print("You should probably start the day.")
            print("You have two options.")
            print(Fore.YELLOW + option1)
            print(Fore.YELLOW + option2 + Style.RESET_ALL)
        else:
            response = input("Just type in numbers 1 or 2. >  ")

def bookshelffun():
    """Allows user to choose a specific book"""
    #list of options
    options_four = ["1","2","3","4"]
    #idea for full game: make a part that elaborates on the stories
    books = ['1. The Lobster Who Could', '2. 101 Ways to Eat Grass', '3. Alan Brinkley American History 13th Edition', "4. Chunky Chicken's Birthday Party"]
    #asks for input
    bookchoice = input("Which one? > ")
    #gets rid of invalid input
    while bookchoice not in options_four:
        bookchoice = input("A number 1-5, please.")
    if bookchoice == "1":
        print("Ah yes, a fine choice. Chapter 47 falls a bit flat, in your opinion.")
        print("You flip through the book and place   >" + (books[0]) + "<   on the couch")
    elif bookchoice == "2":
        print("Ah yes, good for future reference.")
        print("You flip through the book and place   >" + (books[1]) + "<   on the couch")
    elif bookchoice == "3":
        print("Whatever floats your boat.")
        print("You flip through the book and place   >" + (books[2]) + "<   on the couch")
    elif bookchoice == "4":
        print("Ah yes, your favorite. You love how it follows the classic Hero's Journey plotline.")
        print("You flip through the book and place   >" + (books[3]) + "<   on the couch")


    #return skip_morning
def after_instructions():
    """After instructions are given, allows for more free exploration of the living room"""
    print(Fore.CYAN + "####################################" + Style.RESET_ALL)
    optionsafterinstructions = ['look at tv', 'touch tv', 'look at bookshelf', 'touch bookshelf', 'look at mess', 'touch mess', 'help']
    response = ""
    books = ['1. The Lobster Who Could', '2. 101 Ways to Eat Grass', '3. Alan Brinkley American History 13th Edition', "4. Chunky Chicken's Birthday Party"]
    print("There's the" + Fore.YELLOW + " tv," + " bookshelf," + Style.RESET_ALL + " and the" +Fore.YELLOW + " mess" + Style.RESET_ALL + " on the table.")
    while True:
        #all input has .lower() at the end to prevent errors with capitaization
        response = input("What now? > ").lower()
        #each response path has two options, in case the user adds an extra word.
        if response == "look at tv" or response == "look tv":
            print("Yep. That's a tv alright.")
        elif response == "touch tv" or response == "touch the tv":
            print("You turn it on and you watch the news about the upcoming convention. It's a day away and supposed to showcase all the newest technological innovations. You'd go but... probably not. You could always change your mind though.")
        elif response == "look at bookshelf" or response == "look bookshelf":
            print("It's a pretty colorful collection of books. You gaze cheerfully upon the little knickknacks there as well.")
        elif response == "touch bookshelf" or response == "touch the bookshelf":
            print("You run your fingers over all the spines of the books, wondering which one to take.")
            print (books)
            print(Fore.CYAN + "####################################" + Style.RESET_ALL)
            bookshelffun()
        elif response == "touch mess" or response == "touch the mess":
            print("It's an organized mess, not for you to touch.")
        #option to forward story
        elif response == "look at mess" or response == "look mess":
            print("It's a bunch of blueprints of contraptions that you can't understand. Your friend must have left them there after trying to plan a presentation. You don't dare to touch them. By looking at the table, you find that your phone isn't there. Maybe you left it on the" + Fore.YELLOW + " couch?" + Style.RESET_ALL + " Maybe it's in the" + Fore.YELLOW + " kitchen?" + Style.RESET_ALL)
            break
        elif response == "help":
            #gives user available options to use if stuck
            print(f"Available options: {optionsafterinstructions}")
        else:
            print("You seem confused. Try again")
    #after "look at mess" option to forward story
    # options to choose from: ['touch couch', 'look at couch', 'go to kitchen', 'help']
    while True: 
        response = input("What would you like to do? > ").lower()
        if response == "touch couch" or response == "touch the couch":
            print("It's so soft. You don't find your phone in between the cushions, but you find some money! Nice!")
            print(" + 10 Money")
            bot.set_stat("money", 20)
        elif response == "look at couch" or response == "look couch":
            print("It has a very visible indent of you.")
        elif response == "help":
            print("Hm, did you find your phone yet? If so, then maybe it's time to" + Fore.GREEN + " go to" + Fore.WHITE + " the" + Fore.GREEN + " kitchen?" + Style.RESET_ALL)
        elif response == "go to kitchen" or response == "go to the kitchen":
            print("You walk into the kitchen.")
            break
        else: 
            print("You seem confused. Try again?")

def scenetwokitchen():
    """Player just got to the kitchen"""
    os.system('cls')
    print(Fore.CYAN + "####################################" + Style.RESET_ALL)
    print("You look around the kitchen, and you find your bag and phone on the countertop. You take them with you. Your phone says it's now 6 am. Hm. Maybe you should make some breakfast?")
    #choice is an illusion
    #same system as first two-option choice
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
    """Time to meet the robot friend"""
    #meetbuddyoptions = ['look under the table', 'touch switch', 'touch robot', 'look robot']
    print(Fore.CYAN + "####################################" + Style.RESET_ALL)
    print(Back.YELLOW + Fore.BLACK + "Thump" + Style.RESET_ALL)
    #hint at keywords of what to do next
    print("Your foot hit something" + Fore.YELLOW + " under the table." + Style.RESET_ALL)
    while True:
        response = input("What do you do? >  ").lower()
        if response == "look under the table" or response == "look under table":
            print("Oh, it's a metal box of some sort. You lean down to inspect it. It has rounded edges, and upon closer inspection, there's a small" + Fore.YELLOW + " switch" + Fore.WHITE + " on the side.")
            break
    #if they don't get it, then give a more forward hint
        else:
            print("You're very curious to" + Fore.YELLOW + " see" + Style.RESET_ALL + " what is" + Fore.YELLOW + " under the table." + Style.RESET_ALL)
    #Next part to forward story
    while True:
        response = input("That switch looks interesting...what does it do? > ").lower()
        if response == "touch switch" or response == "touch the switch":
            print("You hear a small whirring... is the box getting taller?")
            break
    #extra hint
        else:
            print("You're dying to" + Fore.YELLOW + " touch" + Fore.WHITE + " the switch. >  ")
    os.system('cls')
    print("You watch as it props itself up, and sprouts arms and legs. You crawl up onto the couch as an attempt of self-preservation.")
    print("A small tune starts to play as a display turns on.")
    print("Two words show up on the screen.")
    print(Fore.CYAN + "####################################")
    print("##########" + Fore.WHITE + "   Hello World   " + Fore.CYAN + "#########")
    print("####################################"  + Style.RESET_ALL)
    print("The screen changes to show two round eyes and a smile. It eyes you curiously. What a cute" + Fore.YELLOW + " robot." + Fore.WHITE)
    while True:
        response = input("It feels like you should do something... > ").lower()
        if response == "touch robot" or response == "touch the robot":
            print("It takes your hand in response and chirps happily.")
        #choice that forwards story
        elif response == "look at robot" or response == "look robot":
            print(Fore.CYAN + "####################################" + Style.RESET_ALL)
            print("It sings it's little tune happily and looks at you in wonder and... adoration? Don't get attached! It isn't yours.")
            break
        else:
            print("It looks confused at whatever you tried to attempt. Try again.")
    #this text shows once the "look at robot" choice is made
    print("Speaking of getting attached... Your inventor friend is probably halfway across town by now! You gotta return it! You hastily shove your belongings into your bag and sweep up the bot. You head out the door together in a rush.")
    
def phone():
    """Phone ability, allows user to check in on robot friend any time they wish"""
    os.system('cls')
    #all uses of Fore.(Color) are from colorama, it just changes the color of the upcoming text
    print(Fore.BLUE + "####################################")
    print("########" + Fore.WHITE + "   Protoype Vers. 1   " + Fore.BLUE + "######")
    print("####################################" + Fore.WHITE)
    print(f"                  -Love {bot.love}/40-      ")
    print(f"                  -Knowledge {bot.knowledge}/20-       ")
    print(f"                  -Kindness {bot.kindness}/20-       ")
    print(f"                  -Happiness {bot.happiness}/20-       ")
    print(f"                  -Money {bot.money}-       ")

def bikeride():
    """Transitions into biking scene"""
    print(Fore.CYAN + "####################################" + Style.RESET_ALL)
    print("It's still early morning and you look around frantically for the inventor, robot in hand. Ugh. Their car is gone.")
    print("On the curb you spot a few loose" + Fore.YELLOW + " papers" +Fore.WHITE + " and their" + Fore.YELLOW + " phone." + Style.RESET_ALL + " So much for calling them.")
    #options for the user to use
    bikeride_options = ['look at papers', 'look papers', 'touch papers',' touch the papers']
    #options for second stage
    bikeride_options2 = ['look at phone', 'touch phone','look phone','touch the phone']
    while True:
        #user input
        response = input("The inventor's items catch your eye. > ").lower()
        if response in bikeride_options:
            print("The papers read: -prototype vers. 1-")
            print("Mission: to learn and observe. A.I changes in correspondance to traits Love, Knowledge, Kindness, Happiness")
        elif response in bikeride_options2:
            print(Fore.CYAN + "####################################" + Style.RESET_ALL)
            print("It must be because it's close to the robot, but the screen changes to show several traits.")
            #introduces the Use Phone ability
            print("(Congrats on unlocking the phone! You can use it at any time by typing" + Fore.GREEN + " use phone.)" + Style.RESET_ALL)
            print("It also shows you how much money you have... you won't ask why or how.")
            print("You map out the path to the city in your head. You'd need to go to the marketplace, then take the bus all the way to the piers. Then you'd have to take a ferry. How much did that cost again? Agh less thinking, more doing!")
            print("You take your bike, plop the robot into the basket, and head towards the market.")
            break

def bondingmomentducks():
    "Bonding moment one"
    print(Fore.CYAN + "####################################" + Style.RESET_ALL)
    print("You can see the colorful tops of the marketplace stands coming into view as you ride your bike over a bridge.")
    print("The robot leans over the basket to peer at the yellow blurbs in the distance, and chirps happily.")
    print("You have two options.")
    #two option choice again
    option1 = "1. Stop to look at the ducks."
    option2 = "2. Chirp along with the robot."
    print(Fore.YELLOW + option1)
    print(Fore.YELLOW + option2 + Style.RESET_ALL)
    while True:
        response = input("Option 1 or 2? >  ")
        if response == "1":
            print("You tell the robot all that you know about ducks as you watch them waddle.")
            #changes stats of robot to show that you're bonding 
            print(" +4 Love     +2 Happiness     + 2 Knowledge")
            #love, happiness, and knowledge are added
            bot.set_stat("love", 4)
            bot.set_stat("happiness", 2)
            bot.set_stat("knowledge", 2)
            break
        elif response == "2":
            print("You chirp back and forth like there's no tomorrow.")
            #change robot stats differently because of different choice
            print(" +4 Love     +3 Happiness")
            #only love and happiness is added
            bot.set_stat("love", 4)
            bot.set_stat("happiness", 3)
            break
        else:
            print("Number 1 or 2, please. > ")

def marketplace():
    """The marketplace is full of decisions and choices to make"""
    print(Fore.CYAN + "####################################" + Style.RESET_ALL)
    print("The marketplace is bustling with vendors and customers, and the streets are filled with the smell of baked goods and fresh flowers.")
    print("Your little robot pal seems to carry the same energy as the crowd.")
    print("You chain your bike to a stand. The bus stop is on the other side of the market, but there's no harm in staying a little to enjoy, right?")
    while True:
        helpoptions = ['look clothes stand', 'look toy stand', 'look photo booth', 'look food vendor', 'look musician', 'go to bus stop', 'use phone']
        #options that will give different answers: touch clothes stand, touch toy stand, touch photo booth, touch food vendor, touch musician, touch bus stop
        weirdoptions = ['touch clothes stand','touch toy stand']
        pleasedont = ['touch food vendor', 'touch musician']
        #exposition
        print("There are several vendors nearby that look interesting. To your left there is a" + Fore.YELLOW + " clothes stand" + Fore.WHITE + " and a" + Fore.YELLOW + " toy stand.")
        print(Fore.WHITE + "To your right, there's a" + Fore.YELLOW + " photo booth" + Fore.WHITE + " and a" + Fore.YELLOW + " food vendor." + Fore.WHITE)
        print("You also spot a" + Fore.YELLOW + " musician" + Fore.WHITE + " performing in the corner. You can go to the" + Fore.YELLOW + " bus stop" + Fore.WHITE + " when you're done.")
        print("You can always" + Fore.GREEN + " use" + Fore.WHITE + " your" + Fore.GREEN + " phone" + Style.RESET_ALL + " whenever.")
        print(Fore.CYAN + "####################################" + Style.RESET_ALL)
        #start input loop
        response = input("What do you want to do? >  ").lower()
        if response in weirdoptions:
            print("That would make you look like a thief.")
        elif response == "help":
            print(helpoptions)
        elif response == "use phone":
            phone()
        #brings user to phone option where stats can be seen
        elif response in pleasedont:
            print("That would be considered assault.")
        #tells user to not be weird
        elif response == "look clothes stand":
            print("The clothes stand has small shirts, sweaters, and socks for children. They look like they would fit your robot friend. ")
            #allows the user to interact more with the clothes stand
            answer = input("Look closer at the wares? [yes/no] > ").lower()
            #if yes, goes to a function where you could buy wares.
            if answer == "yes":
                marketclothes()
            if answer == "no":
            #returns to input
                print("You look around again for something to do")
            elif answer not in yes_no:
                answer = input("Yes or no? >  ").lower()
        elif response == "look toy stand" or response == "look at toy stand":
            toystand()
        #brings user to toy stand function with more decisions
        elif response == "look photo booth" or response == "look at photo booth":
            phototime()
        #brings user to photo booth with more decisions
        elif response == "look musician" or response == "look at musician":
            musician()
        #brings user to musician area with more decisions
        elif response == "look food vendor" or response == "look at food vendor":
            foodvendor()
        #brings user to area to make more money
        elif response == "go to bus stop" or response == "go bus stop" or response == "look bus stop":
            bus_stop()
            break
        #brings user to bus stop where game ends
        else:
            print("You don't think you can do that. Try again.")

def foodvendor():
    """Food vendor is where the player can make more money for the marketplace and the upcoming journey."""
    print("You arrive at the food vendor and see a help wanted sign. For each hour you get $5.")
    job = input("Work for the vendor? [yes/no] > ").lower()
    if job == "yes":
        print("You spend the hour chopping fruit")
        print("You got $5!")
        bot.add_stat("money", 5)
    #if user accepts the job, they earn $5
    elif job == "no":
        print("You don't feel like working right now, and return to the market center.")
    #if user does not accept, they return back
    elif job not in yes_no:
        job = input("Yes or no? >  ").lower()

def toystand():
    """choices for the toy stand"""
    #clears the current screen
    os.system('cls')
    print(Fore.CYAN + "####################################" + Style.RESET_ALL)
    print("The toy stand has a bunch of stuffed animals and plushies. There's only one your buddy seems to like. It's a duck plushie that quacks softly when you squeeze it. It's $5.")
    answer = input("Buy the duck plushie? [yes/no] > ").lower()
    if answer == "yes":
        if bot.money >= 5:
        #checks to see if user has enough money
            print("You buy the plushie, and the robot hugs it tightly.")
            #takes away money
            print(" -$5")
            bot.add_stat("money", -5)
        elif bot.money < 5:
            print("Sorry, looks like you don't have enough money.")
            #tells the player they're broke 
    elif answer == "no":
        print("You pat the robot on the head and lead them away from the stand.")
        print("You look around again for something to do")
        #returns user to marketplace
    elif answer not in yes_no:
        answer = input("Yes or no? >  ").lower()

def musician():
    """Choices for the cool musician on the street"""
    #clears the current screen
    os.system('cls')
    print(Fore.CYAN + "####################################" + Style.RESET_ALL)
    print("They're playing the pennywhistle solo of 'My Heart Will Go On'. It's not very good.")
    answer = input("Donate? [yes/no] > ").lower()
    if answer == "yes":
        if bot.money >= 1:
        #if user decides to donate, checks to see if they have enough money.
        #if enough money, success
            print("You donate a dollar since they tried. The robot looks at you in surprise.")
            print(" -$1")
            print(" +kindness")
            bot.add_stat("money", -1)
            bot.add_stat("kindness", 4)
        elif bot.money < 1:
        #not enough money, soz
            print("Sorry, looks like you don't have enough money.")
    if answer == "no":
        print("You look around again for something to do.")
        #returns user to marketplace
    elif answer not in yes_no:
        answer = input("Yes or no? >  ").lower()

def marketclothes():
    """Shows items and prices at the market store for clothes. Purchase goods here."""
    print("You find a few options that would fit your friend.")
    shoppingitems = {'1': {'Item':'Tiny duck shirt', 'Price': 10},
    '2': {'Item':'Tiny panda onesie','Price': 15},
    '3': {'Item':'"I love you a bot" hoodie','Price': 10}}
    print(shoppingitems['1'])
    print(shoppingitems['2'])
    print(shoppingitems['3'])
    while True:
        purchase = input("Which one would you like to buy? [1/2/3] or [leave] > ")
        if purchase == "1":
            if bot.money >= 10:
                print("You got a tiny duck shirt. It's very cute, and your friend puts it on instantly.")
                print(" -$10")
                bot.add_stat("money", -10)
            elif bot.money < 10:
                print("You don't have enough money.")
        elif purchase == "2":
                    if bot.money >= 15:
                        print("You got a tiny panda onesie. It's very cute, and your friend puts it on instantly.")
                        print(" -$15")
                        bot.add_stat("money", -15)
                    elif bot.money < 15:
                        print("You don't have enough money.")
        elif purchase == "3":
                    if bot.money >= 10:
                        print("You got a punny hoodie. It's very cute, and your friend puts it on instantly.")
                        print(" -$10")
                        bot.add_stat("money", -10)
                    elif bot.money < 10:
                        print("You don't have enough money.")
        elif purchase == "use phone":
            phone()
        elif purchase == "leave":
            print("You look around again for something to do.")
            break

def phototime():
    """Choices for photo booth"""
    #clears the current screen
    os.system('cls')
    print(Fore.CYAN + "####################################" + Style.RESET_ALL)
    print("It looks like it's free, and you could take a picture of you and your new friend. It's not every day you can take a photo with a robot.")
    answer = input("take a photo? [yes/no] >  ").lower()
    if answer == "yes":
        print("You spend a couple minutes in the photo booth. The robot looks very pleased with the strip of film.")
        print("+love +happiness")
        #because it was a touching moment, your robot gains stats
        bot.add_stat("love", 4)
        bot.add_stat("happiness", 4)
    if answer == "no":
        print("You look around again for something to do")
        #back to the market
    elif answer not in yes_no:
        answer = input("Yes or no? >  ").lower()

def bus_stop():
    #clears the current screen
    os.system('cls')
    print(Fore.CYAN + "####################################" + Style.RESET_ALL)
    print("You decided it's time to move on. You make your way through the crowd and head towards the bus stop.")
    print("You sit down on a bench and help your buddy onto the seat.")
    print("You wonder how the city is going to be like, and what else is in store for you both.")
    #end of options, nice closing for now
    print(Fore.CYAN + "####################################" + Style.RESET_ALL)

def demo_end():
    """Tells player they have reached the end of the demo"""
    print("You've reached the end of Hello World: A Wholesome Adventure, but don't worry! More content is planned.")
    print("I hope you enjoyed! If you're reading this, feel free to let me know if you have any suggestions for the future.")
    #shows phone which is updated with stats
    print("Have a nice day!")
    finalstats = input("Want to see your final stats? Saying no will end the game without it. [yes/no] > ").lower()
    if finalstats == "yes":
        phone()
    elif finalstats == "no":
        sys.exit()
    elif finalstats not in yes_no:
        finalstats =input("You completed a whole chunk of an adventure game and you still don't get this concept? Humanity is an amazing thing. A blessing and a curse. Two sides of the same coin that is man. What an enigma. You don't deserve to see your final stats.").lower()
    #:(

title_screen()
#shows the title screen and allows user to pick a choice
beforeinstructions()
#introduction and setting before instructions are given
after_instructions()
#more complex choices from here on out
scenetwokitchen()
#second scene, kitchen
meetbuddy()
#meet the robot
bikeride()
#bike ride to marketplace
bondingmomentducks()
#bond with the robot (duck edition)
marketplace()
#large market with tons of choices
demo_end()
#end of demo :(