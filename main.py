from jogo_da_velha import CriarBoard, FazMovimento, GetInputValido, PrintBoard, VerificaGanhador, VerificaMovimento

from minimax import MovimentoIA

jogador = 0 # jogador 1
board = CriarBoard()
ganhador = VerificaGanhador(board)

while(not ganhador):
    PrintBoard(board)
    print('============') 
    if(jogador == 0):
        i,j = MovimentoIA(board, jogador)
    else:
        #i,j = MovimentoIA(board, jogador)
        i = GetInputValido('Digite a linha: ')
        j = GetInputValido('Digite a Coluna: ')
    
    if (VerificaMovimento(board, i, j)):
        FazMovimento(board,i,j,jogador)
        jogador = (jogador + 1)%2
    else:
        print('A posição informada já esta ocupada')
    
    ganhador = VerificaGanhador(board)

print('=============')
PrintBoard(board)
print('=============')
print('Ganhador : ',ganhador)
print('=============')