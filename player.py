import  pygame

# Classe pour gérer les joueurs
# un sprite est un objet ou un élément qui peut être dessiné à l'écran et qui peut être déplacé
class Player(pygame.sprite.Sprite):

    def __init__(self):
        # Initialisation de la classe Sprite
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.velocity = 3
        self.image = pygame.image.load("/home/nedh/PycharmProjects/Comet_fall_game/PygameAssets-main/player.png")
        # Redimensionnement de l'image du joueur sur l'ecran c'est à dire sa position
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 610

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity