import random

player_1_position = 0
player_2_position = 0

player_1_trapped = False
player_2_trapped = False

LAP_DISTANCE = 20
LAP_AMOUNT = 3
GOAL = LAP_DISTANCE * LAP_AMOUNT

while player_1_position < GOAL and player_2_position < GOAL:
    # player 1 turn
    print("Player 1, it is your turn. Press enter to roll the dice!")
    input()

    roll_1 = random.randint(1, 6)
    roll_2 = random.randint(1, 6)

    player_1_move = roll_1 + roll_2

    print("Player 1, you rolled a " + str(roll_1) + " and a " + str(roll_2) + ".")

    if not player_1_trapped:
        player_1_position += player_1_move
        print("You move " + str(player_1_move) + " spaces. You are now at space " + str(player_1_position % 20) + " on lap " + str(player_1_position // 20 + 1) + ".")
        
        # check for early player 1 win
        if player_1_position > GOAL:
            print("Player 1, you have won the game!")
            break

        # check if trapped
        if player_1_position % 5 == 0 and player_1_position % 20 != 0:
            print("You are now trapped!")
            player_1_trapped = True
    else:
        if roll_1 == roll_2:
            print("You have escaped from the trap! You can move again next turn.")
            player_1_trapped = False
        else:
            print("You are still stuck in the trap!")

    print()

    # player 2 turn
    print("Player 2, it is your turn. Press enter to roll the dice!")
    input()

    roll_1 = random.randint(1, 6)
    roll_2 = random.randint(1, 6)

    player_2_move = roll_1 + roll_2

    print("Player 2, you rolled a " + str(roll_1) + " and a " + str(roll_2) + ".")

    if not player_2_trapped:
        player_2_position += player_2_move
        print("You move " + str(player_2_move) + " spaces. You are now at space " + str(player_2_position % 20) + " on lap " + str(player_2_position // 20 + 1) + ".")
        
        # check for early player 2 win
        if player_2_position > GOAL:
            print("Player 2, you have won the game!")
            break

        # check if trapped
        if player_2_position % 5 == 0 and player_2_position % 20 != 0:
            print("You are now trapped!")
            player_2_trapped = True
    else:
        if roll_1 == roll_2:
            print("You have escaped from the trap! You can move again next turn.")
            player_2_trapped = False
        else:
            print("You are still stuck in the trap!")

    print()