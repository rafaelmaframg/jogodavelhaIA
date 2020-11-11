import pygame
from jogo_da_velha import CriarBoard, FazMovimento, GetInputValido,\
                        PrintBoard, VerificaGanhador, VerificaMovimento
from minimax import MovimentoIA

pygame.font.init()

def draw_board(win, board):
    height = 600
    width = 600
    tamanho = 600/3

    for i in range(1, 3):
        pygame.draw.line(win, (0,0,0),(0, i *tamanho),(width, i* tamanho),3)
        pygame.draw.line(win, (0,0,0),(i* tamanho, 0),(i * tamanho, height),3)
    for i in range(3):
        for j in range(3):
            font = pygame.font.SysFont('Cosmicsans',100)

            x = j*tamanho
            y = i*tamanho
            text = font.render(board[i][j], 1,(128,0,0))
            win.blit(text,((x+75),(y+75)))

def redraw_window(win, board):
    win.fill((255, 255, 255))
    draw_board(win, board)

def main():
    win = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('jogo da velha')

    board = CriarBoard()

    redraw_window(win, board)
    pygame.display.update()
    
    jogador = 0 # jogador 1
    ganhador = VerificaGanhador(board)

    while(not ganhador):
        PrintBoard(board) 
        if(jogador == 0):
            jogou = False
            while (not jogou):
                for event in pygame.event.get():
                    if(event.type == pygame.QUIT):
                        return
                    elif(event.type == pygame.MOUSEBUTTONUP):
                        pos = pygame.mouse.get_pos()
                        i = int(pos[1]/200)
                        j = int(pos[0]/200)
                        print(i,j)
                        jogou = True
                 
        else:
            i,j = MovimentoIA(board, jogador)
            #i = GetInputValido('Digite a linha: ')
            #j = GetInputValido('Digite a Coluna: ')
        
        if (VerificaMovimento(board, i, j)):
            FazMovimento(board,i,j,jogador)
            jogador = (jogador + 1)%2
        
        ganhador = VerificaGanhador(board)
        redraw_window(win, board)
        pygame.display.update()

    while(True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                return
main()