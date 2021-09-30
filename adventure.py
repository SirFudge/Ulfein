import random


def river_east1():
    print("\nLooks like you have to turn back, you cannot cross the river")
    print("Or are you brave enough to try?")
    print("(1. Go back.) (2. Try to swim across.)")
    print("================================")

def forest_edge_north1():

    print("\nYou walk east and find yourself at the edge of a forest.")
    print("Do you enter the forest or turn back?")
    print("================================")

def pod_west1():
    chance = random.randint(1, 100)
    if chance <= 20:
        print("You didn't manage to grab the ledge!")
        game_over("Fell into the Void!")
    else:
        print("\nYou managed to grab the ledge and pull yourself up.")
        print("You quickly return to the field!")
        print("================================")
        start()

def void():
    print("You have reached the edge of the world.")
    print("The ground fall's away from the ground underneath you!")
    print("You fall off the edge into a dark pit!")
    print("================================")

def game_over(reason):
    print("Game Over!")
    print("\n" + reason)
    print("\nRestarting the game!")
    print("================================")
    start()

def start():

    print("\nYou are in a big field")
    print("There are multiple ways to travel.")
    print("The only thing you have is a compass, you look at it to figure out where to go.")
    print("Do you go north, east, south or west?")
    print("================================")

    answer = input(">").lower()

    if "north" in answer:
        forest_edge_north1()
    elif "east" in answer:
        river_east1()
    elif "west" in answer:
        pod_west1()
    else:
        game_over("Your option was invalid.")

def main():
    print("\nWelcome to A simple Text Adventure")
    print("Do you want to start playing?")
    print("================================")

    answer = input(">").lower()
    if "y"  in answer:
        start()
    else:
        sys.exit()

main()
