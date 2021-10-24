import random
import json
import datetime

secret = random.randint(1, 30)
wg = []


with open("score_list.json", "r") as score_file:
    score_list = json.loads(score_file.read())
    highsc_list = sorted(score_list, key=lambda d: d["attempts"]) #sorts the dictionaries in the list according to the "attempts" key

# functions
def show_score_list():
    for score_dict in score_list:
        print("Player: " + score_dict["name"], "| Attempts: " + str(score_dict["attempts"]), "| Secret number: "+ str(score_dict["secret"]), "| Date: " + score_dict["date"], "| Wrong guesses: " + str(score_dict["wrong_guesses"]))
def show_top3():
    for score_dict in highsc_list[:3]:
        print("Player: " + score_dict["name"], "| Attempts: " + str(score_dict["attempts"]), "| Secret number: "+ str(score_dict["secret"]), "| Date: " + score_dict["date"], "| Wrong guesses: " + str(score_dict["wrong_guesses"]))

def play_game(level):
    name = input("Enter player's name? ")
    attempts = 0
    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1
        with open("score_list.json", "r") as score_file:
            score_list = json.loads(score_file.read())

        if guess == secret:
            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            score_list.append({"name": name, "attempts": attempts, "date": str(datetime.datetime.now()), "secret": secret, "wrong_guesses": wg})
            with open("score_list.json", "w") as score_file:
                score_list = score_file.write(json.dumps(score_list))
            break
        elif guess > secret:
            wg.append(guess)
            if level == "easy":
                print("Your guess is not correct... try something smaller")
            else:
                print("Wrong! Try again.")
        elif guess < secret:
            wg.append(guess)
            if level == "easy":
                print("Your guess is not correct... try something bigger")
            else:
                print("Wrong! Try again.")

# use of functions
while True:
    print("------------------------------------------------------------------------------------------------------------")
    selection = input("Enter\n- A for score list,\n- B for top 3 highscores, \n- C to play the game,\n- Q for quitting the game.\nEnter selection: ")
    if selection == "A":
        show_score_list()
    elif selection == "B":
        show_top3()
    elif selection == "C":
        level = input("Do you want to play easy or hard?: ")
        play_game(level.lower())
    elif selection == "Q":
        print("Thnks for playing! Goodbye!")
        break
    else:
        print("Ooops! There was a typo in your selection!")