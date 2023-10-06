# Tic-Tac-Toe (Game):

# Imports:
# random: This module is imported so the computer could make decisions!
import random


class TicTacToe:
    # Default-Board:
    default_board = '''
            1 | 2 | 3
            - - - - -
            4 | 5 | 6
            - - - - -
            7 | 8 | 9
            '''

    # Winning Conditions:
    winning_conditions = [
        [1, 2, 3],  # Horizontal (TOP)
        [4, 5, 6],  # Horizontal (MIDDLE)
        [7, 8, 9],  # Horizontal (BOTTOM)
        [1, 4, 7],  # Vertical (LEFT)
        [2, 5, 8],  # Vertical (MIDDLE)
        [3, 6, 9],  # Vertical (RIGHT)
        [1, 5, 9],  # Diagonal (LEFT to RIGHT)
        [3, 5, 7],  # Diagonal (RIGHT to LEFT)
    ]

    # A list to hold all choices:
    # OR MIGHT EVEN USE EXTEND ON PLAYER.extend(COMPUTER/FRIEND) | BETTER USE X+Y
    all_choices = []

    # First Turn of Player, this variable is put in place to switch turns for each game!
    first_turn = False

    # Incrementation:
    turns = 1
    games = 0

    # Scoring:
    player_1_score = 0
    player_2_score = 0
    drawn = 0

    @staticmethod
    def update_board(board, player_01, player_01_mark, player_02, player_02_mark):

        # Replace Numbers in board against marks!
        for selection_01 in player_01:
            board = board.replace(str(selection_01), player_01_mark)

        for selection_02 in player_02:
            board = board.replace(str(selection_02), player_02_mark)

        # Display updated board:
        print(board)

    def computer_logic(self, difficulty="Easy"):

        # matches: this list will contain choices that gets matched with the current winning conditions! (2 Elements)
        # not_match: this list will contain the element that was not found within the current winning condition!
        matches, not_match = [], []

        # available options are the options that are neither chosen by player nor computer/player!
        available_options = [option for option in range(1, 10) if option not in (player_1[1] + player_2[1])]

        # These 2 lists, player 2[1] & player 1[1], means the current choices they have made,
        # with this Algorithm, computer is supposed to try and win, elif block, else go for a random choice!
        for wb in [player_2[1], player_1[1]]:

            # We iterate over each winning condition:
            for conditions in self.winning_conditions:

                # As discussed above, if in the current winning condition, no matches to make a move list are cleared!
                matches.clear(), not_match.clear()

                # We iterate over each number in the winning condition:
                for condition in conditions:
                    if condition in wb:
                        matches.append(condition)
                    else:
                        not_match.append(condition)

                # If this is the case below, then either go for the WIN or BLOCK!
                if len(matches) == 2 and (not_match[0] in available_options):

                    if difficulty == "Hard":
                        return not_match[0]

                    elif difficulty == "Easy":
                        easy = [not_match[0], random.choice(available_options)]
                        return random.choice(easy)

        # If the code block above is not applicable, then go for a random move!
        return random.choice(available_options)

    def validate_and_score(self, player_choices, others_choices):
        to_win = self.winning_conditions

        # Check if player_choices or others_choices win or not ?
        for conditions_block in to_win:
            matches_p = 0
            matches_o = 0

            for condition in conditions_block:
                if condition in player_choices:
                    matches_p += 1
                elif condition in others_choices:
                    matches_o += 1

            if matches_p == 3:
                return True, "You Win!", conditions_block

            if matches_o == 3:
                return False, F"{player_2[0].split('s')[0][:-1]} Win!", conditions_block

        else:
            return None, None, None


# Main():
print("\n Hey, lets play Tic-Tac-Toe! \n")
set_difficulty = ""

while True:

    # Allows user to choose either to play against a player or a computer!
    try:
        mode = int(input("1 - against Friend | 2 - against Computer: "))

        if mode not in [1, 2]:
            print("Invalid Entry, Choose either 1 or 2!")

        if mode == 2:

            available_difficulties = {"1": "Easy", "2": "Hard"}

            ask_difficulty = input("Select Difficulty (1 - Easy | 2 - Hard): ")

            set_difficulty = available_difficulties.get(ask_difficulty, available_difficulties.get("1"))
            print(F"\nDifficulty: {set_difficulty}")

            break

        else:
            break

    except ValueError:
        print("Invalid Entry, Choose either 1 or 2!")

# Object created so its methods / attributes could be used:
game = TicTacToe()

# Initialize list for the player & (another player or computer):
player_1 = ("Your Turn: ", [], "0")

# 1 - Multiplayer
if mode == 1:
    player_2 = ("Friend's Turn: ", [], "X")

# 2 - Computer
else:
    player_2 = ("Computer's Turn: ", [], "X")

# When game starts either you or (friend | computer) will get the first turn!
if game.games == 0:
    game.first_turn = random.choice([True, False])

# Initiate the game:
while True:

    # Reset Values, if Continued:
    player_1[1].clear()
    player_2[1].clear()
    game.all_choices.clear()
    game.turns = 0

    # Increment Number of Games:
    game.games += 1

    print("\nGame: " + str(game.games))
    print(F"Your Score: {game.player_1_score} | Opponent Score: {game.player_2_score} | Drawn: {game.drawn}"
          "\n")

    if game.games > 1:
        game.first_turn = False if game.first_turn else True

    # Display Default Game Board & Start the Game:
    print(game.default_board)

    while game.turns < 9:

        player = 0
        second = 0

        try:
            # Means player got the first turn:
            if game.first_turn:
                if game.turns % 2 == 1:
                    player = int(input(F"{game.turns + 1} | ({player_1[2]}) {player_1[0]}"))

                else:
                    if mode == 1:
                        second = int(input(F"{game.turns + 1} | ({player_2[2]}) {player_2[0]}"))
                    else:
                        second = game.computer_logic(difficulty=set_difficulty)
                        print(F"{game.turns + 1} | ({player_2[2]}) {player_2[0]} {second}")

            # Means computer or friend got the first turn:
            else:
                if game.turns % 2 == 0:
                    player = int(input(F"{game.turns + 1} | ({player_1[2]}) {player_1[0]}"))

                else:
                    if mode == 1:
                        second = int(input(F"{game.turns + 1} | ({player_2[2]}) {player_2[0]}"))
                    else:
                        second = game.computer_logic(difficulty=set_difficulty)
                        print(F"{game.turns + 1} | ({player_2[2]}) {player_2[0]} {second}")

            # Validate Entry:
            if (player or second) in game.all_choices:
                print("Invalid Input, Already Chosen!")

            elif (player or second) not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                print("Invalid Input, Type the correct number!")

            else:
                if player == 0:
                    game.all_choices.append(second)
                    player_2[1].append(second)
                else:
                    game.all_choices.append(player)
                    player_1[1].append(player)

                # Updating the Turns & Game-Board:
                game.turns += 1
                game.update_board(game.default_board, player_1[1], player_1[2], player_2[1], player_2[2])

                if game.turns >= 5:
                    winner, winner_name, *line = (game.validate_and_score(player_1[1], player_2[1]))

                    if winner is not None:

                        if winner:
                            print(F" Player Wins!"
                                  F" \n {player_1[2]}'s @ {line}")
                            game.player_1_score += 1
                            break

                        else:
                            print(F" Winner is: {winner_name}"
                                  F" \n {player_2[2]}'s @ {line}")
                            game.player_2_score += 1
                            break

        except ValueError:
            print("Invalid Input, Use Numbers only!")

    if game.turns > 8:
        game.drawn += 1
        print("Match Drawn!")

    # Print Score after a game ends.
    print(F"\nYour Score: {game.player_1_score} | Opponent Score: {game.player_2_score} | Drawn: {game.drawn}\n")

    continue_playing = input("Press C to Continue | Press Q to Quit: ")
    print("\n")

    if continue_playing.upper() != "C":
        quit()
