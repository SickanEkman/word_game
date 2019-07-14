import data_set
from classes import Game, Team


def prepare_game():
    teams = create_teams()
    deck = present_the_game_options()
    return teams, deck


def create_teams():
    team_list = []
    for i in range(int(input("How many teams will be playing?\n"))):  # TODO Handle errors!
        name = input("What's the name of team %s?\n" % (len(team_list) + 1))
        name = Team(name)
        team_list.append(name)
    return team_list


def present_the_game_options():
    print("What game would you like?")
    for k, v in data_set.mapping_int_to_presentation.items():
        print(k, v)
    return choose_game()


def choose_game():
    # TODO If else or except is executed, there return value of function is None
    try:
        answer = int(input(
            "* * * Answer with the corresponding number, or 666 if you want to see list of games again. * * * \n"
            "Number: "))
        if answer == 666:
            present_the_game_options()
        elif answer in data_set.mapping_int_to_var.keys():
            return data_set.mapping_int_to_var[answer]
        else:
            print("That number is not in the list. Come on...\n")
            choose_game()
    except ValueError:
        print("That's not gonna work.\n")
        choose_game()


if __name__ == "__main__":
    #playing_teams, game_deck = prepare_game()
    my_game = Game([Team("sara"), Team("x")], data_set.programming_basic_concepts)
