import pygame
from pygame.locals import QUIT, RESIZABLE, K_RETURN, K_SPACE, KEYDOWN, KEYUP
import sys
import button
import os

pygame.init()

# Modification de la résolution de la taille de la fenetre :
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic Tac Toe :")

# Variable du Jeu :
game_paused = False
menu_state = "main"


# État initial
current_state = menu_state

# Position et taille du bouton
lien_rect = pygame.Rect(200, 200, 100, 50)
# Couleurs
white = (255, 255, 255)
red = (255, 0, 0)
#Nous définissons le type de caractère ainsi que la taille de notre catactère sélectionnée par l'utilisateur :
font = pygame.font.SysFont("Montserrat", 60)

# Nous avons défini la couleur de notre choix en utilisant la variable (TEXT_COLOR) en lui attribuant les couleurs respectives [RGB].
TEXT_COL = (255, 255, 255)

# Nous chargeons les images des buttons que nous avons sélectionnée sur internet et
# de les insérer dans nos variables qui prendront en compte le chargement de nos images :
resume_img = pygame.image.load("images/button_resume.png").convert_alpha()
options_img = pygame.image.load("images/button_options.png").convert_alpha()
quit_img = pygame.image.load("images/button_quit.png").convert_alpha()
video_img = pygame.image.load('images/button_video.png').convert_alpha()
audio_img = pygame.image.load('images/button_audio.png').convert_alpha()
keys_img = pygame.image.load('images/button_keys.png').convert_alpha()
back_img = pygame.image.load('images/button_back.png').convert_alpha()

#create button instances
resume_button = button.Button(304, 125, resume_img, 1)
options_button = button.Button(297, 250, options_img, 1)
quit_button = button.Button(336, 375, quit_img, 1)
video_button = button.Button(226, 75, video_img, 1)
audio_button = button.Button(225, 200, audio_img, 1)
keys_button = button.Button(246, 325, keys_img, 1)
back_button = button.Button(332, 450, back_img, 1)

# Couleurs
blanc = (255, 255, 255)
rouge = (255, 0, 0)

# Font
font = pygame.font.Font(None, 36)

# Fonction pour créer un bouton
def creer_bouton(x, y, largeur, hauteur, couleur, texte, action):
    rect = pygame.Rect(x, y, largeur, hauteur)
    pygame.draw.rect(screen, couleur, rect)

    texte_surface = font.render(texte, True, blanc)
    texte_rect = texte_surface.get_rect(center=rect.center)
    screen.blit(texte_surface, texte_rect)

    # Vérifie si le bouton est cliqué
    clic_souris = pygame.mouse.get_pressed()
    if rect.collidepoint(pygame.mouse.get_pos()) and clic_souris[0] == 1:
        action()







def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))
  
def ouvrir_fichier():
          chemin_fichier = "C:/Users/Utilisateur/Desktop/tic-tac-toe/play.py"
          if os.path.exists(chemin_fichier):
            os.system(f"start {chemin_fichier}")  # Ouvre le fichier avec le programme par défaut
            # print(ouvrir_fichier)
#game loop
run = True
while run:

  screen.fill((52, 78, 91))

  #check if game is paused: :
  if game_paused == True:
    #check menu state
    if menu_state == "main":
      # draw pause screen buttons 
      if resume_button.draw(screen):
        print(ouvrir_fichier())
        # game_paused = False
        
      
      if options_button.draw(screen):
        menu_state = "options"
      if quit_button.draw(screen):
        run = False
    #check if the options menu is open
    if menu_state == "options":
      #draw the different options buttons
      if video_button.draw(screen):
        print("Paramètre Vidéo")
      if audio_button.draw(screen):
        print("Paramètre Audio")
      if keys_button.draw(screen):
        print("Change Key Bindings")
      if back_button.draw(screen):
        menu_state = "main"
  else:
    draw_text("Appuyer sur ESPACE pour entrer. ", font, TEXT_COL, 160, 250)

  #event handler

  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        game_paused = True
    if event.type == pygame.QUIT:
      run = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
          if event.button == 1:  # Bouton gauche de la souris
              if 200 < event.pos[0] < 400 and 200 < event.pos[1] < 250:
                  ouvrir_fichier()
    
    # Dessin de l'objet (lien)
    # Effacement de l'écran
    # screen.fill(blanc)

    # Création du bouton avec la fonction ouvrir_fichier comme action
    # creer_bouton(200, 200, 200, 50, rouge, "Play", ouvrir_fichier)

    # Rafraîchissement de l'écran
    pygame.display.flip()
    
    pygame.display.update()

pygame.quit()





 
