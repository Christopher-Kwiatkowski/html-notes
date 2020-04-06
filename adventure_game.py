import time
import random


items = []
quest_item = random.choice(["toilet paper", "food", "water", "dog food"])


def print_pause(message):
    print(message)
    time.sleep(2)


def intro():
    print_pause("Welcome to the city of Denver!")
    print_pause("Recently, a horrible plague has broken out.")
    print_pause("The denizens are all quarantined in their houses.")
    print_pause(
        f"You have run out of {quest_item} and are tasked with finding "
        "more and bringing it home.")
    print_pause(
        f"There are rumors that someone on your street has been hoarding "
        "{quest_item}...")
    print_pause(
        "but you never know who might also have the plague. Good luck, "
        "friend and stay safe.")
    time.sleep(2)
    your_house()


def your_house():
    print_pause("You find yourself in your house.")
    if quest_item in items:
        print_pause(
            "Congratulations, a winner is YOU! Because of your valient "
            "efforts,")
        print_pause(
            f" you now have an abundance of {quest_item} and are safely "
            "home.")
        print_pause(
            "According to the groundhog, only 12 more weeks of plague...")
        play_again()
    else:
        print_pause(
            f"Well? What are you waiting for, go find some {quest_item}!")
        inside_outside_choice()


def inside_outside_choice():
    activity = input("Do you want to search inside or go outside?\n")
    if 'search' in activity or 'inside' in activity:
        time.sleep(2)
        if 'keys' in items:
            print_pause("There really isn't much left to do here.")
            your_house()
        else:
            inside_key_choice()
    elif 'go' in activity or 'outside' in activity:
        your_street()
    else:
        print_pause("Decide inside or outside please.")
        inside_outside_choice()


def inside_key_choice():
    choice = input(
        "You see your car keys hanging on the wall. Do you want to take "
        "them?\nY/N\n").lower()
    if 'y' in choice:
        print_pause(
            "Good idea, take the keys in case you need to drive to the "
            "store.")
        items.append('keys')
        your_house()
    elif 'n' in choice:
        print_pause("You probably shouldn't be driving anyways right now.")
        your_house()
    else:
        print_pause("Make a yes or no descision here please.")
        inside_key_choice()


def your_street():
    print_pause("Outside it is nice and sunny.")
    print_pause(
        "You can see your house, your car, and your neighbors white,"
        " red and blue houses.")
    outside_choice()


def outside_choice():
    choice = input("Do you want to go to your car, in your house, "
                   "or knock "
                   "on one of your neighbors? White house, blue house,"
                   " or red house?\n").lower()
    if "your house" in choice or "my house" in choice:
        print_pause("You head inside your house.")
        your_house()
    elif "car" in choice:
        if "keys" in items:
            print_pause(
                "Good thing you grabbed your keys! You get in and "
                "start your car.")
            drive_to_store()
        else:
            print_pause("Car is locked, need to find your keys to "
                        "unlock it.")
            your_street()
    elif "white" in choice:
        white_house()
    elif "blue" in choice:
        blue_house()
    elif "red" in choice:
        red_house()
    else:
        print_pause(f"You are under quarantine, you cant go to {choice}.")
        outside_choice()


def drive_to_store():
    drive = input("Do you want to drive to the Grocery "
                  "Store?\nY/N\n").lower()
    if "y" in drive:
        print_pause(
            "The streets are almost deserted as you make your way "
            "to the store parking lot.")
        store()
    elif "n" in drive:
        print_pause("You turn off the car and get back outside.")
        outside_choice()
    else:
        print_pause(
            "This car only takes you to the store and home. "
            "Please answer yes or no.")
        drive_to_store()


def store():
    print_pause(
        "There weren't many cars in the parking lot and you "
        "can see why!")
    print_pause(
        "Looks like the store was picked clean. You do manage to "
        "find some food,")
    print_pause(
        "hopefully you can put your cooking skills to the test "
        "with pork sausage ")
    print_pause("and the last box of pasta!")
    items.append("food")
    print_pause(
        "After checking out, you head back to your car, throw "
        "the food in the trunk")
    print_pause("and drive back to your house.")
    your_street()


def white_house():
    print_pause(
        "You knock on the white house door and your neighbor "
        "Donald greets you and invites you in.")
    print_pause(
        'Donald: "HELLO! It\'s great to see you again, how are '
        'you doing?"')
    print_pause(
        "Before waiting for a reply, Donald starts talking to you "
        "about how he is")
    print_pause(
        "handling the situation and how great of a job he is doing "
        "in this crises.")
    print_pause(
        f'Donald: "And wouldn\'t you know it? but I have a HUGE '
        'stockpile of {quest_item}"')
    print_pause("because I knew it would be scarce!")
    ask_donald()


def ask_donald():
    ask = input(
        f"Do you want to ask Donald for some "
        "{quest_item}?\nY/N\n").lower()
    if 'y' in ask:
        print_pause(
            f"You ask Donald and he agrees, bringing you a big "
            "bag of {quest_item}.")
        print_pause(
            'Donald: "I am always happy to help make the neighborhood '
            'great again!"')
        items.append(quest_item)
        print_pause("After thanking him, you head back outside.")
        your_street()
    elif 'n' in ask:
        print_pause(
            f"You tell him thanks but no thanks (you figure maybe "
            "{quest_item} isn't thaaat important)")
        print_pause("and head back outside.")
        your_street()
    else:
        print_pause(
            f'You mumble something about "{ask}" but Donald doesn\'t '
            'seem to understand you')
        ask_donald()


def red_house():
    print_pause(
        "You head over to your neighbor Nomie's red house and knock on "
        "the door.")
    time.sleep(5)
    print_pause(
        "After about a minute of waiting, you hear her dog, Eco whining "
        "quietly inside.")
    print_pause(
        "Eco is a very happy and friendly dog but you haven't seen her "
        "outside much")
    print_pause(
        "since the start of the plague. You also notice the door is "
        "unlocked and there")
    print_pause("is some dog food in kitchen you can see from the window.")
    red_choice()


def red_choice():
    choice = input("Do you go inside Nomie's house or leave?\n").lower()
    if "inside" in choice:
        print_pause("You slowly open the door and Eco slinks over to you.")
        print_pause("She looks like she hasn't been fed in awhile.")
        print_pause(
            "Her food is next to her bowl in the kitchen but you also "
            "hear a tv upstairs.")
        if "dog food" in items:
            print_pause("Eco barks wildly at you and foams at the mouth!")
            print_pause(
                "You decide now isn't the time to be here anymore and "
                "slam the door")
            your_street()
        else:
            search_red()
    elif "leave" in choice:
        print_pause("It doesn't seem right to break into a neighbors house.")
        your_street()
    else:
        print_pause(
            f"Pick either inside or leave, you can't {choice} right now.")
        red_choice()


def search_red():
    choice = input(
        "Do you take the dog food and leave or check upstairs?\n").lower()
    if 'take' in choice or 'leave' in choice:
        print_pause(
            "You put some food in Eco's bowl and poor half in a bag. "
            "Leaving a note for Nomie,")
        print_pause(
            "you promise to pay her back and take care of Eco whenever "
            "she needs!")
        items.append("dog food")
        print_pause("You head back outside.")
        your_street()
    elif 'check' in choice or 'upstairs' in choice:
        print_pause(
            "You head upstairs, calling out for Nomie as Eco runs ahead.")
        print_pause(
            "Eco cries out in the room where you see the tv lights "
            "flickering")
        print_pause(
            "and you hear what sounds like her collapsing to the floor.")
        print_pause("By the time you make it into the room, it is too late.")
        print_pause(
            "Laying on the floor in front of you lies Eco, Nomie, both "
            "dead of the plague")
        print_pause("Realization washes over you. You also have the plaque.")
        print_pause("GAME OVER")
        play_again()
    else:
        print_pause(
            f"Take the food and leave, or check upstairs. No {choice} "
            "this time.")
        search_red()


def blue_house():
    print_pause(
        "You decide your neighbor Maureen's blue house might be a good idea.")
    print_pause(
        "She loves conspiracy stories and always seems well prepared "
        "for this sort of thing.")
    print_pause(
        "Ringing the doorbell, you don't have to wait long to hear her "
        "little dog yapping at the door")
    if "water" in items:
        print_pause("She yells to you through the door:")
        print_pause('Maureen: "I am sorry, but we are worried about the '
                    'plague and can\'t allow visitors!"')
        print_pause('"It looks like you already have everything you need, '
                    'please go away!"')
        print_pause('"Everything is going to be so good soon. Believe it. '
                    'Speak it. Trust it. Affirm it."')
        print_pause(
            f"Realizing maybe she isn't the person to ask for "
            "{quest_item}, you leave")
        your_street()
    else:
        print_pause(
            "She open's the door a crack and after a breif hello, she "
            "hands you some water")
        items.append("water")
        print_pause(
            "She then starts repeating something you have a hard time "
            "understanding:")
        print_pause('Maureen: "Have no fear. If there is a darkness '
                    'growing in the world, there must')
        print_pause('be an equally growing light. Such are the laws '
                    'of balance and nature"')
        print_pause("You decide now might be the time to head back.")
        your_street()


def play_again():
    again = input("Would you like to play again?\nY/N\n").lower()
    if 'y' in again:
        print_pause("And aaawaaaaaaay we GOOOOOOO!")
        intro()
    elif 'n' in again:
        print_pause("Thanks for playing!")
    else:
        print_pause(
            "What did you even type!? I asked a simple yes or no question...")
        time.sleep(2)
        play_again()


intro()
