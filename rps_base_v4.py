import random
# For choosing a random option for the computer choice of r/p/s

# All the def functions are below
def user_choice():
    user = input("What's your choice? Rock, Paper or Scissors? \n").lower()
    if user == "r" or user == "rock":
        user = "rock"
        return user
    elif user == "p" or user == "paper":
        user = "paper"
        return user
    elif user == "s" or user == "scissors" or user == "scissor":
        user = "scissors"
        return user
    else:
        print("Please choose paper, scissors or rock")

''' program selects random num between 1&3. 1 is for r, 2 is for
paper and 3 is for scissors '''
def computer_choice():
    computer = random.randint(1, 3)
    if computer == 1:
        computer = "rock"
    elif computer == 2:
        computer = "paper"
    else:
        computer = "scissors"
    return computer

''' lowest the program can accept is 1 and highest
is 10. If it is and integer within those values, it
will be accepted, anything else will be rejected '''
def rounds(question, low, high):
    error = "Please enter a whole number between 1 and 10\n"
    valid = False
    while not valid:
        try:
            response = int(input(question))
            if low < response <= high:
                return response
            else:
                print(error)
        except ValueError:
            print(error)

''' The satement decorater will cover the 'you win/lose/tie'
on top and the side to form a box '''
def statement_generator(statement, decoration):
    sides = decoration * 3
    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)
    print(top_bottom)
    print(statement)
    print(top_bottom)
    return ""

''' this is shown near the end of the game stating
who has won and what the stats are'''
def overall():
    if user_wins > comp_wins:
        print("{} wins the game with {} wins!!! The computer got {} "
              "wins and {} ties".format(name, user_wins, comp_wins, ties))
    elif user_wins == comp_wins:
        print("It's a tie! Both {} and Computer got "
              "the same amount of wins.".format(name))
    else:
        print("Oh noo! Looks like the computer won "
              "against you with {} wins:( You got {} "
              "wins and {} ties. Better luck next "
              "time!".format(comp_wins, user_wins, ties))

''' game history is all the previous choices that
the player has made. To show this, I have used the .append() str '''
def game_history(choices_list):
    question = input("Would you like to see your game history? ").lower()
    if question == "yes" or question == "y" or question == "yeah" or question == "ye":
        print(choices_list)
    else:
        print("Thank you for playing my game!")


''' MAIN '''
# INTRODUCTION TO GAME
name = input("What is your name? ").capitalize()

print()

print("Hi {}! Welcome to my Rock/Paper/Scissors game."
      " Best of luck, hope you win :)".format(name))


print()

# calling the rounds() def for input from user
how_many = rounds("First player to win how many "
                  "games is the winner? ", 0, 10)

print()

# INITIAL STATS ARE ZERO
rounds_played = 0
comp_wins = 0
user_wins = 0
ties = 0

''' this is what the game history will be
shown in (the brackets)
This is an empty list '''
history = []

play = input("Press <enter> to play... ")
while play == "":   # unless play equals to anything but <enter>, the loop will keep going
    rounds_played += 1
    print()
    print("!!! ROUND {} !!!".format(rounds_played))
    computer = computer_choice()   # calling the computer_choice() and user_choice() defs
    user_option = user_choice()
    if user_option == "rock":    # if user chooses rock
        if computer == "rock":
            print("You chose rock. The computer chose rock.")
            player = "Tied"
            deco = "-"
            ties += 1
        elif computer == "paper":
            print("You chose rock. The computer chose paper.")
            comp_wins += 1
            player = "Lose"
            deco = "|"
        else:
            print("You chose rock. The computer chose scissors.")
            user_wins += 1
            player = "Win"
            deco = "!"
    elif user_option == "paper":   # if user chooses paper
        if computer == "rock":
            print("You chose paper. The computer chose rock. You win.")
            user_wins += 1
            player = "Win"
            deco = "!"
        elif computer == "paper":
            print("You chose paper. The computer chose paper. You tied.")
            ties += 1
            player = "Tied"
            deco = "-"
        else:
            print("You chose paper. The computer chose scissors. You lose.")
            comp_wins += 1
            player = "Lose"
            deco = "|"
    elif user_option == "scissors":  # if user chooses scissors
        if computer == "rock":
            print("You chose scissors. The computer chose rock. You lose.")
            comp_wins += 1
            player = "Lose"
            deco = "|"
        elif computer == "paper":
            print("You chose scissors. The computer chose paper. You win.")
            user_wins += 1
            player = "Win"
            deco = "!"
        else:
            print("You chose scissors. The computer chose scissors. You tied.")
            ties += 1
            player = "Tied"
            deco = "-"
    else:   # if user inputs something else instead, it will take user to start of the while loop and calls the user choice functoin again
        # play = ""
        redo = user_option
        rounds_played -= 1

    if user_option == "paper" or user_option == "scissors" or user_option == "rock":
        history.append(user_option)  # makes a list of all the choices that user has made
        outcome = "You {}".format(player)
        statement_generator(outcome, deco)
        print()      # Displaying the stats after every round
        print("{}'s score: {}".format(name, user_wins))
        print("Computer's score: {}".format(comp_wins))
        print("Ties: {}".format(ties))
        print()
        if user_wins == how_many:  # if the amount of wins is how many the user chose, it will end the game
            play = "xxx"
            print("You have played {} rounds".format(rounds_played))
            print()
            end = overall()
        elif comp_wins == how_many:
            play = "xxx"
            print("You have played {} rounds".format(rounds_played))
            print()
            end = overall()
        else:
            play = input("Press <enter> to continue playing or 'xxx' to quit ")
    else:
        redo = user_option



player_choices = ("You chose: {}".format(history))
player_history = game_history(player_choices)

print("")
print("Thank you for playing my game!")
