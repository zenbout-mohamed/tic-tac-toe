import pygame
import sys
import random
from utilisateur import Utilisateur
from ia import ia_easy, ia_medium, ia_hard
 
pygame.init()
 
WIDTH, HEIGHT = 900, 900
 
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe!")

BOARD = pygame.image.load("assets/Board.png")
X_IMG = pygame.image.load("assets/X.png")
O_IMG = pygame.image.load("assets/O.png")

joueur1 = Utilisateur("Joueur1")
joueur2 = Utilisateur("Joueur2")

niveau_ia_joueur2 = "easy"
partie_en_cours = True

BG_COLOR = (214, 201, 227)

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
graphical_board = [[[None, None], [None, None], [None, None]], 
                    [[None, None], [None, None], [None, None]], 
                    [[None, None], [None, None], [None, None]]]

to_move = 'X'

SCREEN.fill(BG_COLOR)
SCREEN.blit(BOARD, (64, 64))

pygame.display.update()

def render_board(board, ximg, oimg):
    global graphical_board
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                # Création de l'image X :
                graphical_board[i][j][0] = ximg
                graphical_board[i][j][1] = ximg.get_rect(center=(j*300+150, i*300+150))
            elif board[i][j] == 'O':
                # Création de l'image O :
                graphical_board[i][j][0] = oimg
                graphical_board[i][j][1] = oimg.get_rect(center=(j*300+150, i*300+150))

def add_XO(board, graphical_board, to_move):
    current_pos = pygame.mouse.get_pos()
    converted_x = (current_pos[0]-65)/835*2
    converted_y = current_pos[1]/835*2
    if board[round(converted_y)][round(converted_x)] != 'O' and board[round(converted_y)][round(converted_x)] != 'X':
        board[round(converted_y)][round(converted_x)] = to_move
        if to_move == 'O':
            to_move = 'X'
        else:
            to_move = 'O'
    
    render_board(board, X_IMG, O_IMG)

    for i in range(3):
        for j in range(3):
            if graphical_board[i][j][0] is not None:
                SCREEN.blit(graphical_board[i][j][0], graphical_board[i][j][1])
    
    return board, to_move
# ia.py



def ia_easy(board, signe):
    # Stratégie facile : choix aléatoire parmi les emplacements libres
    return random.choice([i for i, case in enumerate(board) if case == 0])

def ia_medium(board, signe):
    # Stratégie moyenne : implémentez une stratégie plus avancée ici
    pass

def ia_hard(board, signe):
    # Stratégie difficile : implémentez une stratégie encore plus avancée ici
    pass


def ia(board, signe):
    # Vérifier si le signe est valide de l'ia :
    if signe not in ['X', 'O']:
        print("Erreur : Le signe doit être 'X' ou 'O'")
        return False

    # Trouver les emplacements libres sur le plateau
    emplacements_libres = [i for i, case in enumerate(board) if case == 0]

    # Vérifier s'il y a des emplacements libres
    if not emplacements_libres:
        print("Erreur : Aucun emplacement libre sur le plateau")
        return False

    # Choisir un emplacement aléatoire parmi les emplacements libres
    choix = random.choice(emplacements_libres)

    return choix

while partie_en_cours:
    # Logique du jeu
    tour_de_l_ia = True
    # Tour de l'IA
    if tour_de_l_ia:
        if niveau_ia_joueur2 == "easy":
            choix = ia_easy(board, "O")
        elif niveau_ia_joueur2 == "medium":
            choix = ia_medium(board, "O")
        elif niveau_ia_joueur2 == "hard":
            choix = ia_hard(board, "O")
# À la fin de la partie, mettez à jour les scores, l'historique, et sauvegardez


game_finished = False

def check_win(board):
    winner = None
    for row in range(0, 3):
        if((board[row][0] == board[row][1] == board[row][2]) and (board [row][0] is not None)):
            winner = board[row][0]
            for i in range(0, 3):
                graphical_board[row][i][0] = pygame.image.load(f"assets/Winning {winner}.png")
                SCREEN.blit(graphical_board[row][i][0], graphical_board[row][i][1])
            pygame.display.update()
            return winner

    for col in range(0, 3):
        if((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)):
            winner =  board[0][col]
            for i in range(0, 3):
                graphical_board[i][col][0] = pygame.image.load(f"assets/Winning {winner}.png")
                SCREEN.blit(graphical_board[i][col][0], graphical_board[i][col][1])
            pygame.display.update()
            return winner
   
    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
        winner =  board[0][0]
        graphical_board[0][0][0] = pygame.image.load(f"assets/Winning {winner}.png")
        SCREEN.blit(graphical_board[0][0][0], graphical_board[0][0][1])
        graphical_board[1][1][0] = pygame.image.load(f"assets/Winning {winner}.png")
        SCREEN.blit(graphical_board[1][1][0], graphical_board[1][1][1])
        graphical_board[2][2][0] = pygame.image.load(f"assets/Winning {winner}.png")
        SCREEN.blit(graphical_board[2][2][0], graphical_board[2][2][1])
        pygame.display.update()
        return winner
          
    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
        winner =  board[0][2]
        graphical_board[0][2][0] = pygame.image.load(f"assets/Winning {winner}.png")
        SCREEN.blit(graphical_board[0][2][0], graphical_board[0][2][1])
        graphical_board[1][1][0] = pygame.image.load(f"assets/Winning {winner}.png")
        SCREEN.blit(graphical_board[1][1][0], graphical_board[1][1][1])
        graphical_board[2][0][0] = pygame.image.load(f"assets/Winning {winner}.png")
        SCREEN.blit(graphical_board[2][0][0], graphical_board[2][0][1])
        pygame.display.update()
        return winner
    
    if winner is None:
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != 'X' and board[i][j] != 'O':
                    return None
        return "DRAW"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            board, to_move = add_XO(board, graphical_board, to_move)

            if game_finished:
                board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
                graphical_board = [[[None, None], [None, None], [None, None]], 
                                    [[None, None], [None, None], [None, None]], 
                                    [[None, None], [None, None], [None, None]]]

                to_move = 'X'

                SCREEN.fill(BG_COLOR)
                SCREEN.blit(BOARD, (64, 64))

                game_finished = False

                pygame.display.update()
            
            if check_win(board) is not None:
                game_finished = True
                joueur1.score += 10  
                joueur1.historique_scores.append(10)
                joueur1.sauvegarder()

                joueur2.score -= 5  
                joueur2.historique_scores.append(-5)
                joueur2.sauvegarder()
            
            pygame.display.update()





