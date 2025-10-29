import pygame
import sys
import re
import threading

# board and sizing constants
SCREEN_SIZE = 800
OFFSET = 100
SPACE_LENGTH = 100
SPACES_PER_SIDE = 5
PLAYER_RADIUS = 35 / 2
PLAYER_GAP = 5

# program state
running = True
hasWinner = False

# window configuration
pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Board Game Visualization")

# building the board spaces
spaces = []
for i in range(20):
    # top row
    if i <= SPACES_PER_SIDE:
        spaces.append((OFFSET + SPACE_LENGTH * i, OFFSET, SPACE_LENGTH, SPACE_LENGTH))
    elif i <= 2 * SPACES_PER_SIDE:
        spaces.append((SCREEN_SIZE - 2 * OFFSET, OFFSET + SPACE_LENGTH * (i - SPACES_PER_SIDE), SPACE_LENGTH, SPACE_LENGTH))
    elif i <= 3 * SPACES_PER_SIDE:
        spaces.append((SCREEN_SIZE - 2 * OFFSET - (i - SPACES_PER_SIDE * 2) * SPACE_LENGTH, SCREEN_SIZE - 2 * OFFSET, SPACE_LENGTH, SPACE_LENGTH))
    else:
        spaces.append((OFFSET, SCREEN_SIZE - 2 * OFFSET - (i - SPACES_PER_SIDE * 3) * SPACE_LENGTH, SPACE_LENGTH, SPACE_LENGTH))
    
def clean_number(word):
    digits = re.sub('[^0-9]','', word)
    number = int(digits)
    return number

def input_loop():
    # building the players
    player_positions = [0, 0]
    player_trapped = [False, False]
    player_offsets = [(-PLAYER_RADIUS - PLAYER_GAP / 2, 0), (PLAYER_RADIUS + PLAYER_GAP / 2, 0)]
    player_colors = [(0, 0, 255), (255, 0, 0)]

    line_num = 1
    current_player = 0

    # read the lines of text from the text-based game using standard in
    #   it is assumed that the text game will be piped in to the visual
    for line in sys.stdin:
        words = line.strip().split()
        print(line.strip())
        if len(words) == 0:
            line_num = 1
            continue
        
        # if reading the first line for a turn, grab the player index
        if line_num == 1:
            current_player = clean_number(words[1]) - 1
        # if reading the second line for a turn, grab the rolled values
        # TODO: implement the rolls appearing on screen
        elif line_num == 2:
            roll_1 = clean_number(words[5])
            roll_2 = clean_number(words[8])
        # if reading the third line for a turn, this varies
        elif line_num == 3:
            # if the word trap is in the line, either they have gotten trapped
            #   or escaped a trap and will be moving again
            # TODO: implement a trap visual for the screen
            if "trap" in line:
                # nothing happens if stuck in a trap, only care about escape
                if "escape" in line:
                    player_trapped[current_player] = False
            # 
            else:
                move = clean_number(words[2])
                space = clean_number(words[9])
                lap = clean_number(words[12])
                player_positions[current_player] = space
        # if reading fourth line, it can only mean that you were trapped 
        #   or won the game
        elif line_num == 4:
            if "won" not in line:
                player_trapped[current_player] = True

        # move counter for next line
        line_num += 1

        # clear the screen
        screen.fill((255, 255, 255))

        # draw game board
        for space in spaces:
            pygame.draw.rect(screen, (0, 0, 0), space, width=1) 

        # draw players
        for player_i in range(len(player_positions)):
            player_space = spaces[player_positions[player_i]]

            # TODO: adjust for four players to allow centering when alone
            # if player_positions.count(player_positions[player_i]) == 2:
            #     player_location = (player_space[0] + SPACE_LENGTH / 2 - PLAYER_RADIUS, player_space[1] + SPACE_LENGTH / 2)
            # else:
            #     player_location = (player_space[0] + SPACE_LENGTH / 2, player_space[1] + SPACE_LENGTH / 2)

            player_location = (player_space[0] + SPACE_LENGTH / 2 + player_offsets[player_i][0], player_space[1] + SPACE_LENGTH / 2 + player_offsets[player_i][1])

            pygame.draw.circle(screen, player_colors[player_i], player_location, PLAYER_RADIUS)


# TODO: determine if threading can fix issues with window locking
def main_loop():
    running = True
    while running: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # update display
        pygame.display.update()

# main_thread = threading.Thread(target=main_loop)
input_thread = threading.Thread(target=input_loop)

# threads = [main_thread, input_thread]
threads = [input_thread]

# start all threads
for t in threads:
    t.start()

main_loop()

# wait for threads
for t in threads:
    t.join()

pygame.quit()