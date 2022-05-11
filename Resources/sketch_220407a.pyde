from ball import Ball
from enemy import Enemy


class config():
    enemy1 = []
    points = 0
    startGame = False
    WIDTH = 1280
    HEIGHT = 720
    mainFont = 0
    enemy_count = 20


ball1 = Ball(20,100)

def setup():
    size(config.WIDTH, config.HEIGHT)
    
    #Sets image, needed here since processing lib
    ball1.img = loadImage("ship.png")
    
    #Setup Enemies
    for i in range(config.enemy_count):
        config.enemy1.append(Enemy(600, random(20, 700)))
        
    
    #Set Font
    config.mainFont = createFont("Stencil", 20)
    textFont(config.mainFont)
    
def draw():
    background(0)
    
    #Title Screen
    if config.startGame == False:
         titleScreen()
    else:
        mainGame()


def mainGame():
    update()
    render()
        
    if config.points > config.enemy_count - 1:
        fill(255)
        text("YOU WIN!!", 280, 180)

def titleScreen():
    text("WELCOME TO VIDEOGAME!", 280, 50)


def update():
    ball1.update()

    for e in config.enemy1:
        e.update()
        for b in ball1.bullet:
            if e.isCollision(b):
                config.enemy1.remove(e)
                config.points = config.points + 1
        
def render():
    ball1.render()
    
    for e in config.enemy1:
        e.render()
    
    fill(255)
    text(config.points, 40, 20)
    
def mousePressed():
    config.startGame = True
    ball1.fire()
