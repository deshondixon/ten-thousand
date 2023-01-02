from game_logic import GameLogic


def intro():
    print("Welcome to Ten Thousand")
    print("(y)es to play game or (n)o to decline ")

    y = input("> ")

    if y == "n":
        print("OK, bye")
        exit()


def restart():
    print("(y)es to play game again or (n)o to decline")

    user_input = input("> ")
    if user_input == "y":
        play_dice()

    elif user_input == "n":
        print("OK, bye")
        exit()


def play_dice():
    round_number = 1
    user_wins = 10000
    current_dice = []
    total_score = 0
    turn_score = 0
    dice_left = 6

    print(f"Starting round 1")
    print(f"Rolling {6 - len(current_dice)} dice...")

    while True:

        choice = input("> ")

        if total_score >= user_wins:
            print("You win!")
            restart()
            break

        if choice == "q":
            print("OK, bye")
            exit()
            break

        if choice == "r":
            round_number = round_number + 1
            dice_roll = GameLogic.roll_dice(dice_left)
            roll_score = GameLogic.calculate_score(dice_roll)
            print(f"Total score is {total_score} points")
            print(f"Starting round {round_number}")
            print(f"Rolling {6 - len(current_dice)} dice...")
            print(f"*** {dice_roll} ***")
#           print("Enter dice to keep, or (q)uit:")

        if roll_score == 0:
            turn_score = 0
            print("Farkled!!")
        else:
            turn_score += roll_score
            print(f"You have {turn_score} unbanked points and {dice_left} dice remaining.")
            print(f"(r)oll, (b)ank your points, or (q)uit: ")

        if choice == "b":
            print(f"You banked {turn_score} points in round {round_number}")
            total_score += turn_score
            print(f"Total score is {total_score} points")
            turn_score = 0
            print(f"Starting round {round_number}")


if __name__ == "__main__":
    intro()
    play_dice()
