# Programmer: 
# Description: A simulation of a game using the Player class

from player import Player

# Here are two example objects that you can for testing
player1 = Player("Mario")
print(player1)
player2 = Player("Luigi", 50, 2, 10)
print(player2)
print()

# A little game simulation
round = 1
while player1.is_alive() and player2.is_alive():
    print(f"ROUND {round}")
    player1.attack(player2)
    print(player1)
    print(player2)
    print()
    round += 1
