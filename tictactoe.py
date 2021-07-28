"""
Tic Tac Toe Player
"""

import math

import copy

global X, O, jugadas

X = "X"
O = "O"

EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    jugadas = 1

    for i in range(3):
        for j in range(3):
            if board [i][j] != EMPTY: 
                jugadas += 1

    if jugadas %2 == 0:
        player = O
    else:
        player = X

    return(player)

    raise NotImplementedError

def oponente(board):
    """
    Returns player who has the next turn on a board.
    """

    jugadas = 1

    for i in range(3):
        for j in range(3):
            if board [i][j] != EMPTY: 
                jugadas += 1

    if jugadas %2 == 0:
        oponente = X
    else:
        oponente = O

    return(oponente)

    raise NotImplementedError



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []

    for i in range(3):
        for j in range(3):
            if board [i][j] == EMPTY: 
            #    print("rango i: ",i)
            #    print("rango j: ",j)

                actions.append((i,j))

    return(actions)


    raise NotImplementedError


def result(board, action):
    #print("result: ", action)
    """
    Returns the board that results from making move (i, j) on the board.
    """

    i = action[0]
    j = action[1]

    if i < 0 or i > 2 or j < 0 or j > 3:
        raise ValueError("indice fuera de rango o tablero lleno") 
    if board[i][j] != EMPTY:
        raise ValueError("casilla ocupada") 


    #new_board = copy.deepcopy(board)

    board[i][j] = player(board)

    return(board)

    #raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    ganador = ""
    
    for i in range(3):
        if board[i][0] == X and board[i][1] == X and board[i][2] == X:
            ganador = X 
        elif board[i][0] == O and board[i][1] == O and board[i][2] == O:
            ganador = O

    for j in range(3):
        if board[0][j] == X and board[1][j] == X and board[2][j] == X:
            ganador = X 
        elif board[0][j] == O and board[1][j] == O and board[2][j] == O:
            ganador = O
    
    if board[0][2] == X and board[1][1] == X and board[2][0] == X:
        ganador = X
    elif board[0][2] == O and board[1][1] == O and board[2][0] == O:
        ganador = O  

    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        ganador = X
    elif board[0][0] == O and board[1][1] == O and board[2][2] == O:
            ganador = O  

    if ganador == X:
        return X
    elif ganador == O:
        return O
    else:
        return None


    raise NotImplementedError


def terminal(board):

    """
    Returns True if game is over, False otherwise.
    """

    vacio = False

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
               vacio = True
               break

    termino = False

    if vacio:
        vencedor = winner(board)
        if vencedor == X or vencedor == O:
            termino = True
        else:
            termino = False
    else:
        termino = True

    return termino


    raise NotImplementedError


def utility(board):
    print("utility")
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    ElTermino = terminal(board)
       
    if ElTermino == True:
        ElMejor = winner(board)

        if ElMejor == X:
            utilidad = 1
        elif ElMejor == O:
            utilidad = -1
        else:
            utilidad = 0

        return utilidad

def minimax(board):
    
    #Returns the optimal action for the current player on the board.
    
    print("minimax")

    ia = player(board)

    noia = oponente(board)
    
    mejor_puntaje = -math.inf

    new_board = copy.deepcopy(board)

    for action in actions(board):
        i = action[0]
        j = action[1]
        
        board[i][j] = ia

        modo = 2

        deep = 1
        
        puntaje_final = score(board, deep, modo, ia, noia) 

        board[i][j] = EMPTY
    
        if puntaje_final > mejor_puntaje:
            mejor_puntaje = puntaje_final
            jugada = action

    return(jugada)

    raise NotImplementedError


def score(board, deep, modo, ia, noia):
    
    termino = terminal(board)

    if termino == True:
        ganador = winner(board)
        if ganador == ia:
            puntaje_retorno = 1

        elif ganador == noia:
            puntaje_retorno = -1 

        else:
            puntaje_retorno = 0 

        return puntaje_retorno
        
    if modo == 1:

        mayor_puntaje = -math.inf
      
        for action in actions(board):
            i = action[0]
            j = action[1]


            board[i][j] = ia


            modo = 2
            puntaje = score(board, deep+1, modo, ia, noia)
            board[i][j] = EMPTY

            mayor_puntaje = max(puntaje,mayor_puntaje)

        return  mayor_puntaje

    else:
        mayor_puntaje = math.inf
        for action in actions(board):
            i = action[0]
            j = action[1]


            board[i][j] = noia

            modo = 1
            puntaje = score(board, deep+1, modo, ia, noia)

            board[i][j] = EMPTY

            mayor_puntaje = min(puntaje, mayor_puntaje)

        return mayor_puntaje
