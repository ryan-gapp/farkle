import random

# Function to roll a single die
def roll_die():
    return random.randint(1, 6)

# Function to initialize six dice
def initialize_dice():
    return [roll_die() for _ in range(6)]

# Function to determine the first player
def determine_first_player(players):
    print("\nDetermining who goes first...")
    while True:
        rolls = {player: roll_die() for player in players}
        for player, roll in rolls.items():
            print(f"{player} rolled a {roll}")
        max_roll = max(rolls.values())
        tied_players = [player for player, roll in rolls.items() if roll == max_roll]
        
        if len(tied_players) == 1:
            print(f"{tied_players[0]} goes first!")
            return tied_players[0]
        else:
            print("It's a tie! Re-rolling for tied players...\n")
            players = tied_players

# Function to display the current game state
def display_state(first_list, second_list):
    print(f"[Kept] {first_list} [Rollable] {second_list}")

# Function to reset all dice to the second list
def reset_dice(first_list, second_list):
    second_list.extend(first_list)
    first_list.clear()

# Parse dice numbers entered by the player
def parse_input(input_string):
    input_string = input_string.replace(",", "").replace(" ", "")
    return [int(char) for char in input_string if char.isdigit()]

# Main game logic
def start_game():
    # Setup players
    num_players = int(input("Enter the number of players: "))
    players = [input(f"Enter the name of player {i + 1}: ") for i in range(num_players)]
    
    # Determine who goes first
    first_player = determine_first_player(players)
    current_player_index = players.index(first_player)

    # Initialize scores
    player_points = {player: 0 for player in players}
    
    # Main game loop
    while True:
        current_player = players[current_player_index]
        print(f"\n{current_player}'s turn!")
        
        # At the beginning of each turn, reset the dice
        first_list = []
        second_list = initialize_dice()
        display_state(first_list, second_list)
        
        while True:
            command = input("Enter 'r' to roll, numbers to move dice, 'turn' to end turn, or 'reset': ").strip()
            
            if command == "r":
                # Roll all dice in the second list
                second_list = [roll_die() for _ in second_list]
                print("------ROLLED------")
            elif command == "reset":
                # Reset all dice to the second list
                reset_dice(first_list, second_list)
            elif command == "turn":
                # End the current turn
                turn_points = int(input(f"Enter turn points for {current_player}: "))
                if player_points[current_player] == 0 and turn_points < 500:
                    print(f"{current_player} must score at least 500 points to get on the board.")
                else:
                    player_points[current_player] += turn_points
                    print(f"{current_player} now has {player_points[current_player]} points.\n")
                print("Game scores:")
                for player, points in player_points.items():
                    print(f"{player}: {points} points")
                break
            else:
                # Attempt to move dice from second to first
                try:
                    numbers = parse_input(command)
                    for num in numbers:
                        if num in second_list:
                            second_list.remove(num)
                            first_list.append(num)
                except ValueError:
                    print("Invalid input. Please enter 'r', numbers, 'turn', or 'reset'.")
            
            # Check if all six dice are in the first list
            if len(first_list) == 6:
                print("All six dice are in the first list. Moving them back to the second list.")
                reset_dice(first_list, second_list)
            
            # Display the updated game state
            display_state(first_list, second_list)
        
        # Check for winner
        winner = None
        for player, points in player_points.items():
            if points >= 10000:
                winner = player
                break
        
        # If someone has won, initiate final round
        if winner:
            print(f"\n{winner} has reached 10,000 points! Final round begins.")
            print(f"Other players have one turn to try to beat {winner}'s score.")
            
            # Final round for other players
            for player in players:
                if player != winner:
                    first_list = []
                    second_list = initialize_dice()
                    print(f"\n{player}'s turn in the final round!")
                    while True:
                        command = input("Enter 'r' to roll, numbers to move dice, 'turn' to end turn, or 'reset': ").strip()
                        
                        if command == "r":
                            second_list = [roll_die() for _ in second_list]
                            print("------ROLLED------")
                        elif command == "reset":
                            reset_dice(first_list, second_list)
                        elif command == "turn":
                            turn_points = int(input(f"Enter points for {player}: "))
                            player_points[player] += turn_points
                            print(f"{player} now has {player_points[player]} points.\n")
                            break
                        else:
                            try:
                                numbers = parse_input(command)
                                for num in numbers:
                                    if num in second_list:
                                        second_list.remove(num)
                                        first_list.append(num)
                            except ValueError:
                                print("Invalid input. Please enter 'r', numbers, 'turn', or 'reset'.")
                        
                        # Check if all six dice are in the first list
                        if len(first_list) == 6:
                            print("All six dice are in the first list. Moving them back to the second list.")
                            reset_dice(first_list, second_list)
                        
                        # Display the updated game state
                        display_state(first_list, second_list)
            
            # Determine the final winner
            final_winner = max(player_points, key=player_points.get)
            print(f"\nThe final winner is {final_winner} with {player_points[final_winner]} points!")
            break
        
        # Move to the next player
        current_player_index = (current_player_index + 1) % num_players

# Start the game
if __name__ == "__main__":
    start_game()
