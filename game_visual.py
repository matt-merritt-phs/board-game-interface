import pygame

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

# building the players
player_positions = [0, 0]
player_offsets = [(-PLAYER_RADIUS - PLAYER_GAP / 2, 0), (PLAYER_RADIUS + PLAYER_GAP / 2, 0)]
player_colors = [(0, 0, 255), (255, 0, 0)]

def draw_frame():
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

# TODO: implement reading from stdin
def input_loop():
    draw_frame()

# TODO: determine if threading can fix issues with window locking
def main_loop():
    running = True
    while running: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # update display
        pygame.display.update()

# TODO: wait for both functions to finish before quitting
draw_frame()
main_loop()
pygame.quit()

