# Cricket

# Imports:
import random


class Cricket:
    def __init__(self, player_team, opponent_team, overs, wickets):
        self.player_team = player_team,
        self.opponent_team = opponent_team,
        self.overs = overs,
        self.wickets = wickets,

    def toss(self):
        """
        A function that conducts the toss for our cricket game.
        """
        bat_or_bowl = {
            1: "Bat",
            2: "Bowl"
        }

        # Select side on coin:
        coin = int(input("\n"
                         "0 - Head | 1 - Tail: "))

        # Choose a number between 1 & 6 for toss-computational basis:
        coin_computation_player = int(input("Choose a number between [1-6]: "))
        coin_computation_opponent = random.randint(1, 6)

        computation = (coin_computation_player + coin_computation_opponent) % 2

        # If computation = 0, it means Heads and Player Choice is Heads!
        # If computation = 1, it means Tails and Player Choice is Tails!
        if (not computation and not coin) or (computation and coin):
            decision = int(input(F"\n"
                                 F"{self.player_team[0]} won the toss & would like to, 1 - Bat | 2 - Bowl: "))
            batting_side, bowling_side = (self.player_team[0], self.opponent_team[0]) if decision == 1 else (
                self.opponent_team[0], self.player_team[0])

            print(F"{self.player_team[0]} won the toss & choose to {bat_or_bowl.get(decision)} first!")
            return batting_side, bowling_side

        else:
            decision = random.randint(1, 2)
            batting_side, bowling_side = (self.opponent_team[0], self.player_team[0]) if decision == 1 else (
                self.player_team[0], self.opponent_team[0])

            print(F"\n"
                  F"{self.opponent_team[0]} won the toss & choose to {bat_or_bowl.get(decision)} first!")
            return batting_side, bowling_side

    @staticmethod
    def run_rate(z, x, y, tar, rn, tbl, bb):
        """
        Computer chooses options based on CRR of the Player (1st Innings) | RRR of (2nd Innings), to avoid spams.
        """

        # Computer Bats (1st):
        if ((not x) and (not y)) or bb == 0:
            run_options = [r for r in range(1, 7)]
            return run_options

        else:
            rrr = 0
            crr = 0

            if (not x) and y:
                rrr = ((tar - rn) / (tbl - bb)) * 6

            else:
                crr = (rn / bb + 1) * 6

            run_options = []

            if (rrr or crr) >= 36:
                run_options = [6]

            elif 30 <= (rrr or crr) < 36:
                run_options = [r for r in range(5, 7)]

            elif 24 <= (rrr or crr) < 30:
                run_options = [r for r in range(4, 7)]

            elif 18 <= (rrr or crr) < 24:
                run_options = [r for r in range(3, 7)]

            elif 12 <= (rrr or crr) < 18:
                run_options = [r for r in range(2, 7)]

            elif (rrr or crr) < 12:
                run_options = [r for r in range(1, 7)]

            if z not in run_options:
                run_options = [r for r in range(z, 7)]

            return run_options

    def play(self, batting_side, second_innings, innings, target=0):
        """
        A function that codes the gameplay for our cricket game.
        """

        # Stats Initialized:
        balls_bowled = 0
        wickets_taken = 0
        runs = 0

        # Boundaries Initialized:
        fours = 0
        sixes = 0

        # Who is batting ?
        player = False

        if batting_side == self.player_team[0]:
            player = True

        # Possible Runs:
        run_options = [r for r in range(1, 7)]

        # Continue playing until all overs are bowled or all wickets are taken!
        while (balls_bowled != self.overs[0][1]) and (wickets_taken != self.wickets[0][1]):

            while True:

                try:
                    run_player = int(input("\n"
                                           "Choose a run to score [1-6]: "))

                    if run_player not in run_options:
                        print("Choose a valid run to score!")

                    else:
                        break

                except ValueError:
                    print("Choose a valid run to score!")

            # Computer choose its score:
            computer_options = self.run_rate(run_player, player, second_innings, target, runs, self.overs[0][1],
                                             balls_bowled)
            print(computer_options)
            run_opponent = random.choice(computer_options)

            # If value is same, then it means OUT!:
            if run_player == run_opponent:
                balls_bowled += 1
                wickets_taken += 1

            else:

                # Update Variables:
                run = run_player if player else run_opponent

                runs += run
                balls_bowled += 1

                if run == 4:
                    fours += 1

                elif run == 6:
                    sixes += 1

            # Display Result:
            print(F"{self.player_team[0]} chose: {run_player} | {self.opponent_team[0]} chose: {run_opponent}")
            print(F"{teams.get(batting_side)}: {runs}-{wickets_taken} | {balls_bowled // 6}.{balls_bowled % 6}"
                  F" (CRR: {round((runs / balls_bowled) * 6, 2)})")

            if second_innings:
                if (runs >= target) or (self.overs[0][1] == balls_bowled) or (self.wickets[0][1] == wickets_taken):
                    break

                else:
                    print(F"{teams.get(batting_side)} NEED {target - runs} RUNS"
                          F" TO WIN OF {self.overs[0][1] - balls_bowled} BALLS"
                          F" (RRR: {round(((target - runs) / (self.overs[0][1] - balls_bowled)) * 6, 2)})")

        # A dictionary for stats:
        stats = {
            "Team": batting_side,
            "Runs": runs,
            "Over": F"{balls_bowled // 6}.{balls_bowled % 6}",
            "Wicket": wickets_taken,
            "Fours": fours,
            "Sixes": sixes,
            "AVG S/R": round((runs / balls_bowled) * 100, 2)
        }

        # 1st Innings results will be shown!
        if not second_innings:
            target = runs + 1
            innings["First Innings"] = stats

            print("\n"
                  F"Summary of {list(innings.keys())[0]}:")

            for heading, value in innings["First Innings"].items():
                print(F"{heading}: {value}")

            return target, innings

        # Match Results will be shown! (1st Innings & 2nd Innings)
        if second_innings:
            innings["Second Innings"] = stats

            print("\n"
                  F"Summary of {list(innings.keys())[1]}:")

            for heading, value in innings["Second Innings"].items():
                print(F"{heading}: {value}")

            return innings

    def result(self, scorecard):

        # Match Summary:
        first, second = scorecard["First Innings"], scorecard["Second Innings"]

        print("\n"
              "\t Match Summary \t")
        print(F"{(first['Team']).upper()} \t {first['Runs']}-{first['Wicket']} | {first['Over']}")
        print(F"{(second['Team']).upper()} \t {second['Runs']}-{second['Wicket']} | {second['Over']}")

        # Update Winner:
        difference = scorecard["First Innings"]["Runs"] - scorecard["Second Innings"]["Runs"]

        if difference > 0:
            print(F"\n"
                  F"{(scorecard['First Innings']['Team']).upper()} "
                  F"WIN BY {difference} RUNS!")

        elif difference < 0:
            print(F"\n"
                  F"{(scorecard['Second Innings']['Team']).upper()} "
                  F"WIN BY {self.wickets[0][1] - scorecard['Second Innings']['Wicket']} WICKETS!")

        else:
            print("\n"
                  " !MATCH ENDED IN A TIE! ")


# Global Variable, which will later allow the player to replay the game once finished.
replay = False

# Teams:
teams = {
    'Afghanistan': 'AFG',
    'Australia': 'AUS',
    'Bangladesh': 'BAN',
    'England': 'ENG',
    'India': 'IND',
    'New Zealand': 'NZ',
    'Pakistan': 'PAK',
    'South Africa': 'SA',
    'Sri Lanka': 'SL',
    'West Indies': 'WI'
}

# Formats:
formats = {
    1: ["5 Overs", 30],
    2: ["10 Overs", 60],
    3: ["20 Overs", 120],
    4: ["50 Overs", 300]
}

# Wickets:
wicket = {
    1: ["1 Wicket", 1],
    2: ["3 Wickets", 3],
    3: ["5 Wickets", 5],
    4: ["10 Wickets", 10],
}

# Inning Results:
innings_results = {}

# Main:
while not replay:

    # Greetings:
    print("Head & Tail (Childhood's Cricket Game)"
          "\n")

    # Available Teams:
    for index, team in enumerate(list(teams.keys())):
        print(F"{index + 1} - {team}")

    # Player select team:
    selection_player_team = int(input("\n"
                                      "Select your team: ")) - 1

    # Opponent select team:
    while True:
        selection_opponent_team = random.randint(0, 9)

        if selection_player_team == selection_opponent_team:
            continue

        else:
            break

    # Selections:
    print("\n"
          F"You selected: {list(teams.keys())[selection_player_team]}"
          "\n"
          F"Opponent selected: {list(teams.keys())[selection_opponent_team]}"
          "\n")

    # Number Of Overs to be bowled:
    for index, choice in formats.items():
        print(F"{index} - {choice[0]}")

    selection_overs = input("Choose Format: ")

    print("")

    # Number of Wickets available to each team:
    for index, choice in wicket.items():
        print(F"{index} - {choice[0]}")

    selection_wickets = input("Choose Wicket: ")

    # Creating an object, with these 4 values initialized:
    game_on = Cricket(list(teams.keys())[selection_player_team],
                      list(teams.keys())[selection_opponent_team],
                      formats.get(int(selection_overs), "Not Found"),
                      wicket.get(int(selection_wickets), "Not Found"))

    # To do toss & select the batting side.
    bat, bowl = game_on.toss()

    # To start the first innings:
    t, first_innings = game_on.play(bat, False, innings_results)

    # To switch sides:
    bat, bowl = bowl, bat

    # Inter-mission:
    print(F"\n {bat.upper()} WILL NEED {t} RUNS IN {((formats.get(int(selection_overs)))[0]).upper()} TO WIN \n")

    # To start the second innings:
    second_innings = game_on.play(bat, True, first_innings, target=t)

    # Show result:
    game_on.result(second_innings)

    break
