import pygame
 
width = 1280
height = 720
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0

#images
playerOneCardBackImage = pygame.image.load('resources/backgroundOfCard.jpg')
background = pygame.image.load('resources/one.jpg')

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height) # helps with drawing character
        self.vel = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self): # check if player presses button or mouse up and down
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.rect = (self.x, self.y, self.width, self.height) #coordinates is top left, so down is adding (top left is 0,0)
            

class Card():
    def __init__(self, x, y, width, height, health, spell, damage, color):
        self.x = x
        self.y = y
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self.spell = spell
        self.damage = damage
        self.color = color
        self.rect = (x, y, width, height)

    def draw(self, win):
        #pygame.draw.rect(win, self.color, self.rect)
        win.blit(playerOneCardBackImage, (self.rect))

    def select(self):
        mousePos = pygame.mouse.get_pos()

class Deck():
    def __init__(self, x, y, width, height, cards):
        self.x = x
        self.y = y
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.cards = cards

    def draw(self, win):
        # draws both players hands & background of hands
        pygame.draw.rect(win, (99, 84, 60), (320, 570, 640, (720-570)))
        pygame.draw.rect(win, (99, 84, 60), (320, 0, 640, 150))
        pygame.draw.rect(win, (0,0,0), (320, 0, 640, 150),4)
        pygame.draw.rect(win, (0,0,0), (320, 570, 640, (720-570)),4)
        

def redrawWindow(win,Player,Card,Deck):
    win.blit(background,(0,0))
    Player.draw(win)
    Card.draw(win)
    Deck.draw(win)
    pygame.display.update()


def main():
    p = Player(50, 50, 100, 100, (0, 255, 0))
    c = Card(100, 100, 50, 100, 1, 1, 1, (0,255,0))
    d = Deck(500, 600, 200, 400, 1)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
       # win.blit(background, (0,0))
        redrawWindow(win,p,c,d)


main()