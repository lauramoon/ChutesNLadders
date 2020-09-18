"""
Simulate thousands of Chutes and Ladders (aka, snakes and ladders or snakes and arrows) games, analyze the results.
Uses the American standard Milton Bradley set of chutes and ladders, the roll of a single six-sided die,
and the rule that a player must land exactly on square 100 to win.
(If a role would take the player past 100, the player doesn't move.)
Note: there is a variation in one chute; in some editions the one that ends at space 26
starts at space 47, and in some it starts at space 48.
"""
import random
import statistics
import matplotlib.pyplot as plt
from collections import defaultdict
from game import Game


def load_cnl():
    """
    returns a dictionary with all the chutes and ladders (cnl). Key is the starting location,
    value is the result of traveling the chute or ladder.
    :return: dictionary of start (key) and end (value) positions of chutes and ladders
    """
    cnl = {1: 38, 4: 14, 9: 31, 16: 6, 21: 42, 28: 84, 36: 44, 47: 26, 49: 11, 51: 67,
           56: 53, 62: 19, 64: 60, 71: 91, 80: 100, 87: 24, 93: 73, 95: 75, 98: 78}

    return cnl


def turn_count_sim(n):
    """
    simple count of total turns to finish a game. no data about the game is retained.
    :param n: the number of single-player games to simulate
    :return: list of turn counts for n single-player simulations
    """
    turns = []

    # do n simulations
    for i in range(0, n):

        # initialize number of turns and the space the player is on
        turn_count = 0
        space = 0

        cnl = load_cnl()

        # keep taking turns until the player is on space 100
        while space != 100:
            # current turn number
            turn_count += 1

            # roll the die
            roll = random.randint(1, 6)

            # see where the player lands
            land = space + roll

            # if on a chute or ladder, traverse it
            if land in cnl:
                space = cnl[land]
            # if overshoots 100, stay put
            elif land > 100:
                space = space
            # if lands on 100, done!
            elif land == 100:
                break
            # if nothing interesting, stay on land
            else:
                space = land

            if turn_count > 2000:
                print("Over 2000 turns!")
                break

        turns.append(turn_count)

    return turns


def turns_hist(turns):
    """
    prints histogram of turns for a single player to reach the end
    :param turns: list of turns from simulation
    """
    plt.hist(turns, 300, (1, 300))
    plt.title(f"Turns to Win in Chutes and Ladders: {len(turns)} simulations")
    plt.xlabel("Turns to Land on Final Space")
    plt.ylabel("Number of Games")
    plt.show()


def sets_of_sims(n, count):
    """
    simulates given numbers of simulations given number of times, calculates mean, median, mode, and
    standard deviation for each set of simulations, plots box plot for each stat
    :param n: number of simulation sets
    :param count: number of simulations in each set
    """
    # Lists of stats for n simulations of count games
    mean = []
    median = []
    mode = []
    stdev = []

    for i in range(0, n):
        turns = turn_count_sim(count)
        mean.append(statistics.mean(turns))
        median.append(statistics.median(turns))
        mode.append(statistics.mode(turns))
        stdev.append(statistics.pstdev(turns))

    fig, axs = plt.subplots(2, 2)
    axs[0, 0].boxplot(mean)
    axs[0, 0].set_title('Mean')
    axs[0, 1].boxplot(median)
    axs[0, 1].set_title('Median')
    axs[1, 0].boxplot(mode)
    axs[1, 0].set_title('Mode')
    axs[1, 1].boxplot(stdev)
    axs[1, 1].set_title('Standard Deviation')
    fig.suptitle(f"{n} Sets of {count} Simulations")
    plt.show()


def full_sim(n):
    """
    simulates n games, creates object Game for each game, returns list of n Games
    :param n: number of simulations
    :return: list of Games
    """
    # list of Games
    games = []

    for i in range(n):
        # initialize game, number of turns, and the space the player is on
        game = Game()
        turn_count = 0
        space = 0

        cnl = load_cnl()

        # keep taking turns until the player is on space 100
        while space != 100:
            # current turn number
            turn_count += 1

            # roll the die
            roll = random.randint(1, 6)

            # see where the player lands
            land = space + roll

            # if on a chute or ladder, traverse it, update map of chutes/ladders used
            if land in cnl:
                space = cnl[land]
                game.cnl_map[land] += 1

            # if overshoots 100, stay put
            elif land > 100:
                space = space

            # if lands on 100, done!
            elif land == 100:
                break

            # if nothing interesting, stay on land
            else:
                space = land

            # update lists of spaces and dictionary of spaces
            game.moves.append(space)
            game.space_map[space] += 1

            # in case something goes wrong
            if turn_count > 2000:
                print("Over 2000 turns!")
                break

        game.turns = turn_count
        games.append(game)

    return games


def longest_slide(n):
    """
    Exploration of the longest chute in the game: space 87 to 24. Produces 2 plots, one shows the average
    length of a game for a given number of times the chute was traversed, the other shows in how many games the
    chute was traversed a given number of times. Could easily be modified for any other chute or ladder of interest.
    :param n: number of simulations to run
    """
    games = full_sim(n)

    long_slide = []

    # get list of number of times longest slide traversed and total turns
    for i in range(0, n):
        long_slide.append([games[i].cnl_map[87], games[i].turns])

    # max times the long slide was traversed
    max_long = max([x[0] for x in long_slide])
    avg_turns = []

    for i in range(0, max_long + 1):
        turns_i = [x[1] for x in long_slide if x[0] == i]
        if turns_i:
            mean_turns = statistics.mean(turns_i)
        else:
            mean_turns = 0
        avg_turns.append([i, mean_turns, len(turns_i)])

    plt.bar([x[0] for x in avg_turns], [x[1] for x in avg_turns])
    plt.xlabel("Number of times down the longest chute")
    plt.ylabel("Average number of turns")
    plt.title(f"{n} Simulations: When You Keep Landing on Space 87")
    plt.show()

    plt.bar([x[0] for x in avg_turns], [x[2] for x in avg_turns], log=True)
    plt.xlabel("Number of times down the longest chute")
    plt.ylabel("Number of games with this number of times")
    plt.title(f"{n} Simulations: How Likely Are You to Land on Space 87?")
    plt.show()


def compare_cnl(n):
    """
    Compare the frequency of traversing the 18 different chutes and ladders, produces bar chart of
    the average number of times each chute and ladder is traversed per game.
    :param n: number of simulations to run
    """
    games = full_sim(n)
    cnl = load_cnl()

    # total number of times each chute or ladder was traversed
    cnl_counts = defaultdict(int)

    for i in range(n):
        for key, value in games[i].cnl_map.items():
            cnl_counts[key] += value

    # lists of info for plot
    start_squares = [key for key in cnl_counts]
    start_squares.sort()
    start_strings = []
    color = []
    avg_times = []

    for square in start_squares:
        if cnl[square] < square:
            color.append('red')
        else:
            color.append('blue')
        start_strings.append(str(square))
        avg_times.append(cnl_counts[square]/n)

    plt.bar(start_strings, avg_times, color=color)
    plt.title(f"{n} Simulations: How Frequently Chutes and Ladders Traversed")
    plt.xlabel("Starting square of each chute and ladder")
    plt.ylabel("Average number of times per game traversed")
    plt.show()


def main():

    compare_cnl(100000)


main()
