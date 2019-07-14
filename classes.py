from threading import Timer
import random

import sys, select


class Game(object):

    def __init__(self, teams, deck):
        self.teams = teams
        self.deck = deck

        self.level_tracker = 1  # keeps track of current level in game
        self.team_tracker = 0  # aids the team_currently_playing keep track of teams
        self.team_currently_playing = self.teams[self.team_tracker]  # keeps track of which team is currently playing
        self.words_left_in_level = []  # gets filled with the whole deck before every level
        self.clock_ticking = False
        self.timer_five = Timer(5, self.end_turn)
        self.timer_ten = Timer(10, self.end_turn)

        self.run_game()

    def run_game(self):
        if self.level_tracker <= 3:
            self.new_level()
        elif self.level_tracker == 4:
            print(self.team_currently_playing.score)
            print("End of game!")

    def new_level(self):
        print("\nLevel %s" % self.level_tracker)
        self.words_left_in_level = list(self.deck)
        if not self.words_left_in_level:
            print("SOMETHING IS WRONG, NO WORDS LEFT AFTER FILLING THE LIST!")
            exit()
        self.start_turn()

    def start_turn(self):
        self.team_currently_playing = self.teams[self.team_tracker]
        print("\nTeam %s is up next!" % self.team_currently_playing.name)
        secs = 5 if self.level_tracker == 1 else 10
        ready = input("\nAre you ready to start the turn? Press 's' \n")
        print("\nYou pressed '%s' to start the turn" % ready)
        if ready == "s":
            self.clock_ticking = False
            self.do_turn()

    def do_turn(self):
        #self.timer_five.start()
        #self.clock_ticking = True
        while True:
            print("Say somethin!")
            i, o, e = select.select([sys.stdin], [], [], 10)
            if i:
                print("You said", sys.stdin.readline().strip())
            else:
                print("You said nothing!")
                break
    """            if self.words_left_in_level:
                current_word = random.choice(self.words_left_in_level)
                presentation = "\nThe word is: " + current_word + "\n"
                answer = input(presentation) if self.clock_ticking else None
                print("You pressed '%s' after word: '%s'" % (answer, current_word))
                if answer == "y":
                    # I think the problem is here.
                    # The timer above doesn't actually stop the loop,
                    # so the input question is still hanging there after end_turn is called.
                    # How can i make the input irrelevant when a specific event happens?
                    self.handle_correct_guess(current_word)
                else:
                    print("\nAnswer wasn't 'y'")
            else:
                self.timer_five.cancel()
                self.end_level()
    """

    def end_turn(self):
        self.clock_ticking = False
        print("\nTime's up.")
        if (self.team_tracker + 1) == len(self.teams):
            self.team_tracker = 0
        else:
            self.team_tracker += 1
        if self.words_left_in_level:
            self.start_turn()
        else:
            self.end_level()

    def handle_correct_guess(self, word):
        self.team_currently_playing.give_point()
        try:
            self.words_left_in_level.remove(word)
        except ValueError:
            print("FAILING TO REMOVE LAST WORD")
            pass

    def end_level(self):
        self.clock_ticking = False
        print("\nNo words left in this level.\nNext level coming up!")
        self.level_tracker += 1
        self.run_game()


class Team(object):
    def __init__(self, name):
        self.name = name
        self.score = 0

    def give_point(self):
        self.score += 1
