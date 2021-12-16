import numpy as np
import pygame
import sys
import math

def gamefun(ROW_COUNT,COLUMN_COUNT,PIECES_NO):

    # Defining colours
    BLUE = (0,0,255)
    BLACK = (0,0,0)
    RED = (255,0,0)
    YELLOW = (255,255,0)

    # ROW_COUNT = int(input("Enter row Count!!"))
    # if(ROW_COUNT<=0):
    #     ROW_COUNT=int(input("Enter correct row count!"))
    # COLUMN_COUNT = int(input("Enter column Count!!"))
    # if(COLUMN_COUNT<=0):
    #     COLUMN_COUNT=int(input("Enter correct column count!"))
    # PIECES_NO = int(input("Enter NO Slices!!"))
    # if(PIECES_NO<=0):
    #     PIECES_NO=int(input("Enter Correct No of Pieces!"))

    #function to create board
    def board_create():
        board = np.zeros((ROW_COUNT,COLUMN_COUNT))
        return board

    #function to drop piece
    def piece_drop(board, row, col, piece):
        board[row][col] = piece

    #Checking whether entered position is valid or not
    def check_valid_location(board, col):
        return board[ROW_COUNT-1][col] == 0

    def get_next_open_row(board, col):
        for r in range(ROW_COUNT):
            if board[r][col] == 0:
                return r
    #Printing board
    def board_print(board):
        print(np.flip(board, 0))

    # Logic for winning
    def winning_logic(board, piece):
        # Check horizontal locations for win
        # for c in range(COLUMN_COUNT-3):
        # 	for r in range(ROW_COUNT):
        # 		if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
        # 			return True
        for c in range(COLUMN_COUNT + 1 - PIECES_NO):
            for r in range(ROW_COUNT):
                ctr = False
                for i in range(PIECES_NO):
                    if board[r][c + i] == piece:
                        ctr = True
                    else:
                        ctr = False
                        break
                if ctr == True:
                    break
            if ctr == True:
                break
        if ctr == True:
            return True


        # Check vertical locations to win
        # for c in range(COLUMN_COUNT):
        # 	for r in range(ROW_COUNT-3):
        # 		if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
        # 			return True
        # Check vertical locations to win
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT+ 1 - PIECES_NO):
                ctr = False
                for i in range(PIECES_NO):
                    if board[r+i][c] == piece:
                        ctr = True
                    else:
                        ctr = False
                        break
                if ctr == True:
                    break
            if ctr == True:
                break
        if ctr == True:
            return True

        # Check positively sloped diaganols
        # for c in range(COLUMN_COUNT-3):
        # 	for r in range(ROW_COUNT-3):
        # 		if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
        # 			return True
        # Check positively sloped diaganols
        for c in range(COLUMN_COUNT +1 -PIECES_NO):
            for r in range(ROW_COUNT+ 1 - PIECES_NO):
                ctr = False
                for i in range(PIECES_NO):
                    if board[r+i][c+i] == piece:
                        ctr = True
                    else:
                        ctr = False
                        break
                if ctr == True:
                    break
            if ctr == True:
                break
        if ctr == True:
            return True

        # Check negatively sloped diaganols
        # for c in range(COLUMN_COUNT-3):
        # 	for r in range(3, ROW_COUNT):
        # 		if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
        # 			return True
        # Check negatively sloped diaganols
        for c in range(COLUMN_COUNT+1-PIECES_NO):
            for r in range(1-PIECES_NO, ROW_COUNT):
                ctr = False
                for i in range(PIECES_NO):

                    if board[r - i][c + i] == piece:
                        ctr = True
                    else:
                        ctr = False
                        break
                if ctr == True:
                    break
            if ctr == True:
                break
        if ctr == True:
            return True

    def draw_board(board):
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
                pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
        
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):		
                if board[r][c] == 1:
                    pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
                elif board[r][c] == 2: 
                    pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
        pygame.display.update()


    board = board_create()
    board_print(board)
    game_over = False
    turn = 0

    pygame.init()

    SQUARESIZE = 100

    width = COLUMN_COUNT * SQUARESIZE
    height = (ROW_COUNT+1) * SQUARESIZE

    size = (width, height)

    RADIUS = int(SQUARESIZE/2 - 5)

    screen = pygame.display.set_mode(size)
    draw_board(board)
    pygame.display.update()

    myfont = pygame.font.SysFont("monospace", 50)
    play = True
    while play:
        while not game_over:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
                    posx = event.pos[0]
                    if turn == 0:
                        pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
                    else:
                        pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
                pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
                    #print(event.pos)
                    # Asking for Input of Player 1
                    if turn == 0:
                        posx = event.pos[0]
                        col = int(math.floor(posx/SQUARESIZE))

                        if check_valid_location(board, col):
                            row = get_next_open_row(board, col)
                            piece_drop(board, row, col, 1)

                            if winning_logic(board, 1):
                                label = myfont.render("Player 1 wins!!", 1, RED)
                                screen.blit(label, (40,10))
                                game_over = True


                    # #Asking for Input of Player 2
                    else:
                        posx = event.pos[0]
                        col = int(math.floor(posx/SQUARESIZE))

                        if check_valid_location(board, col):
                            row = get_next_open_row(board, col)
                            piece_drop(board, row, col, 2)

                            if winning_logic(board, 2):
                                label = myfont.render("Player 2 wins!!", 1, YELLOW)
                                screen.blit(label, (40,10))
                                game_over = True

                    board_print(board)
                    draw_board(board)

                    turn += 1
                    turn = turn % 2
                    
                    if game_over:
                        # pygame.time.wait(3000)
                        again=str(input("Do you want to play again, type yes or no:  "))
                        if again == "no":
                            play = False
                            return("No")
                            break
                        if again == "yes":
                            play = True
                            return("Yes")
