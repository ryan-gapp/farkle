import random

# Scoring rules
def calculate_score(dice):
    counts = {i: dice.count(i) for i in range(1, 7)}
    score = 0

    # Scoring for ones and fives
    score += counts[1] * 100 if counts[1] < 3 else (counts[1] - 3) * 100 + 1000
    score += counts[5] * 50 if counts[5] < 3 else (counts[5] - 3) * 50 + 500

    # Scoring for triples of 2, 3, 4, and 6
    for num in range(2, 7):
        if counts[num] >= 3:
            score += num * 100

    return score

# Function to roll dice
def roll_dice(num_dice, used_dice):
    dice = [random.randint(1, 6) for _ in range(num_dice)]
    while any(die in used_dice for die in dice):  # Re-roll any used dice
        dice = [random.randint(1, 6) for _ in range(num_dice)]
    return dice

# Function to validate chosen dice
def validate_kept_dice(kept_dice, rolled_dice):
    rolled_copy = rolled_dice[:]
    for die in kept_dice:
        if die in rolled_copy:
            rolled_copy.remove(die)
        else:
            return False
    return True

def farkle():
    print("Welcome to Farkle!")
    total_score = 0

    while True:
        print(f"\nYour total score: {total_score}")
        dice_to_roll = 6
        turn_score = 0
        used_dice = []  # Keep track of used dice
        first_roll = True  # Track if it's the first roll of the turn

        while dice_to_roll > 0:
            rolled_dice = roll_dice(dice_to_roll, used_dice)
            print(f"You rolled: {rolled_dice}")

            # Calculate score for this roll
            roll_score = calculate_score(rolled_dice)

            # If it's the first roll, the player must score 500 or more to start scoring
            if first_roll and roll_score < 500:
                print("You must score at least 500 points on your first roll to start scoring.")
                print("Farkle! You lose all points for this turn.")
                turn_score = 0
                break

            # If it's not the first roll or the player has scored enough on the first roll, continue
            if roll_score == 0:
                print("Farkle! You lose all points for this turn.")
                turn_score = 0
                break

            # Let the player choose dice to keep
            while True:
                try:
                    kept_input = input("Enter the dice you want to keep (comma-separated, e.g., 1,1,5): ")
                    kept_dice = [int(die) for die in kept_input.split(",")]

                    if validate_kept_dice(kept_dice, rolled_dice):
                        break
                    else:
                        print("Invalid selection. Please choose dice from the rolled dice.")
                except ValueError:
                    print("Invalid input. Please enter numbers separated by commas.")

            turn_score += calculate_score(kept_dice)
            print(f"Points this turn: {turn_score}")

            # Update the used dice list
            used_dice.extend(kept_dice)
            dice_to_roll -= len(kept_dice)

            if dice_to_roll == 0:
                print("You used all dice. Rolling 6 dice again!")
                dice_to_roll = 6
                used_dice = []  # Reset the used dice for a new round
            else:
                choice = input("Do you want to keep rolling the remaining dice? (y/n): ").lower()
                if choice != 'y':
                    break

            # Mark the first roll as completed
            first_roll = False

        total_score += turn_score

        # Ask the player if they want to continue playing
        keep_playing = input("Do you want to play another turn? (y/n): ").lower()
        if keep_playing != 'y':
            print(f"Game over! Your final score is {total_score}.")
            break

if __name__ == "__main__":
    farkle()
