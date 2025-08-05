import pygame
from pygame import K_RIGHT, K_LEFT

from  game import Game
pygame.init()


pygame.display.set_caption("Comet fall game")
screen = pygame.display.set_mode((1080,850))
fond = pygame.image.load("/home/nedh/PycharmProjects/Comet_fall_game/PygameAssets-main/bg.jpg")


# Création d'une instance de la classe Game pour charger le jeu
game = Game()

# Maintenir la fenêtre ouverte
running = True
while running:
    # Afficher le fond
    screen.blit(fond, (0, -100))

    # Afficher le joueur
    screen.blit(game.player.image, game.player.rect)

    # véification des touches droite et gauche
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    # Mise à jour de l'affichage
    pygame.display.flip()

    #boucle d'événements du clavier (deplacement, fermeture de la fenêtre)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False




