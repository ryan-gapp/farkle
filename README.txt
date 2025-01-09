Farkle Dice Python Terminal Program

Overview
This is a Python-based implementation of the popular dice game Farkle, designed to run in the terminal. Farkle is a fun and engaging dice game where players roll six dice to score points based on specific combinations. The objective is to reach a target score of 10,000 before your opponents.

Features
Fully playable in the terminal.
    Supports single-player and multiplayer modes.
    The players score their own turns.
    Displays running totals and turn-by-turn gameplay.
    Allows players to "bank" points or risk rolling again.

Requirements
    Python 3.7 or higher.

How to Play
    Run the program:
    python farkle.py
    Follow the on-screen instructions to:
        Choose the number of players.
        Enter Player Names
        Enter ‘r’ to Roll the dice.
        Enter the numbers of the dice to keep them.
        Enter ‘turn’ to end your turn and enter your points. 
        Avoid rolling a Farkle (no scoring dice) to keep your turn alive.

Scoring Rules
The scoring is based on standard Farkle rules:
    Single die scores:
        1 = 100 points
        5 = 50 points
    Three of a kind:
        Three 1's = 1,000 points
        Three 2's = 200 points
        Three 3's = 300 points
        Three 4's = 400 points
        Three 5's = 500 points
        Three 6's = 600 points
    Other combinations:
        A straight (1, 2, 3, 4, 5, 6) = 1,500 points
        Three pairs = 1,500 points
        Four of a kind = Double the score of three of a kind
        Five of a kind = Triple the score of three of a kind
        Six of a kind = Quadruple the score of three of a kind

Game Flow
    Rolling Dice: On your turn, roll six dice.
    Scoring: Select dice that score points and set them aside.
    Re-Rolling: Re-roll the remaining dice to try to score more points.
    Banking Points: End your turn and bank your accumulated points.
    Farkle: If no scoring dice appear on a roll, you lose all unbanked points for the turn.
    Winning: The first player to reach the target score (e.g., 10,000) triggers the final round. The player with the highest score at the end wins.

Example Gameplay
    Player 1 rolls: 1, 5, 5, 2, 3, 6
        Scores 200 points (100 for the 1 and 50+50 for two 5's).
        Re-rolls the remaining three dice.
    Player 2 rolls: 2, 3, 4, 5, 5, 5
        Scores 500 points (three 5's).
        Banks points and ends turn.

Contributing
    Contributions are welcome! Please follow these steps:
        Fork the repository.
        Create a new branch for your feature or bugfix:
        git checkout -b feature-name
    Commit your changes and push the branch:
        git commit -m "Add new feature"
        git push origin feature-name
        Open a pull request.
License
    This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgments
    Inspired by the traditional Farkle dice game.
    Developed as a Python learning project.

Enjoy playing Farkle in your terminal!

