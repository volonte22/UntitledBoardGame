import pygame
from network import Network

width = 1280
height = 720
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Untitled Client")

clientNumber = 0

#images
playerOneCardBackImage = pygame.image.load('resources/backgroundOfCard.jpg')
background = pygame.image.load('resources/one.jpg')

#text
pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
myfont = pygame.font.SysFont('Courier', 18)

#initalizing network

#start of the game count
turnCount = 0

class Player():
    def __init__(self, x, y, width, height, color, turnCount):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height) # helps with drawing character
        self.vel = 3
        self.turnCount = 1

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
        # end turn button
        colorA = (107, 130, 73)
        colorB = (133, 33, 33)
        if turnCount == 0:
            pygame.draw.rect(win, (107, 130, 73), (1090, 315, 140, 80))
        else:
            pygame.draw.rect(win, (133, 33, 33), (1090, 315, 140, 80))

        pygame.draw.rect(win, (0, 0, 0), (1090, 315, 140, 80), 3)
        textsurface = myfont.render('End Turn', False, (0, 0, 0))
        win.blit(textsurface, (1115, 345))

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

        mousePos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        endButtonRect = pygame.Rect(1090, 315, 140, 80)
        if click[0] == 1:
            if endButtonRect.collidepoint(mousePos):
                if self.turnCount == 0:
                    self.turnCount = 1
                else:
                    self.turnCount = 0
        self.update()




    def setTurnStart(self):
        self.turnCount = 1
    def setTurnSecond(self):
        self.turnCount = 0

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

    def draw(self, win, turnCount):
        # background of middle board & players hands
        pygame.draw.rect(win, (99, 84, 60), (320, 570, 640, (720-570)))
        pygame.draw.rect(win, (99, 84, 60), (320, 0, 640, 150))
        pygame.draw.rect(win, (0,0,0), (320, 0, 640, 150),4)
        pygame.draw.rect(win, (0,0,0), (320, 570, 640, (720-570)),4)
        pygame.draw.rect(win, (99, 84, 60), (240, 220, 800, 280))
        pygame.draw.rect(win, (0, 0, 0), (240, 220, 800, 280), 4)

        #decks on right side of screen
        pygame.draw.rect(win, (0,0,0), (1115, 440, 91, 123), 4)
        win.blit(playerOneCardBackImage, (1115, 440))
        pygame.draw.rect(win, (0, 0, 0), (1115, 190-33, 91, 123), 4)
        win.blit(playerOneCardBackImage, (1115, 190-33))


      #  win.blit("End Turn", 1105, 330)

        win.blit(playerOneCardBackImage, (350, 20))

        

def redrawWindow(win,Player,Card,boardLook,Player2):
    win.blit(background, (0, 0))
    boardLook.draw(win, turnCount)
    Player.draw(win)
    Player2.draw(win)
    Card.draw(win)
    pygame.display.update()


def main():
    n = Network()
    startPos = read_pos(n.getPos())
    p = Player(startPos[0], startPos[1], 100, 100, (0, 255, 0), 1)
    p2 = Player(0, 0, 100, 100, (0,255, 0), 0)

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