import pygame
from network import Network

width = 1280
height = 720
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0

#images
playerOneCardBackImage = pygame.image.load('resources/backgroundOfCard.jpg')
background = pygame.image.load('resources/one.jpg')

#initalizing network


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

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height) #coordinates is top left, so down is adding (top left is 0,0)

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])
            

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

class boardLook():
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
        

def redrawWindow(win,Player,Card,boardLook,Player2):
    win.blit(background,(0,0))
    Player.draw(win)
    Player2.draw(win)
    Card.draw(win)
    boardLook.draw(win)
    pygame.display.update()


def main():
    n = Network()
    startPos = read_pos(n.getPos())
    p = Player(startPos[0], startPos[1], 100, 100, (0, 255, 0))
    p2 = Player(0, 0, 100, 100, (0,255, 0))

    c = Card(100, 100, 50, 100, 1, 1, 1, (0,255,0))
    d = boardLook(500, 600, 200, 400, 1)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(60)
        p2Pos = read_pos(n.send(make_pos((p.x, p.y))))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
       # win.blit(background, (0,0))
        redrawWindow(win,p,c,d,p2)


main()