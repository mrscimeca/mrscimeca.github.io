from ball import Ball
from enemy import Enemy

enemy1 = []
points = 0
startGame = False

WIDTH = 1280
HEIGHT = 720

def setup():
    size(WIDTH, HEIGHT)
    
    #Setup Character
    global ball1
    ball1 = Ball(20,100)
    
    #Setup Enemies
    global enemy1
    for i in range(20):
        enemy1.append(Enemy(600, random(20, 700)))
        
    
    global mainFont
    mainFont = createFont("Stencil", 20)
    textFont(mainFont)
    
def draw():
    global startGame
    background(0)
    
    if startGame == False:
         titleScreen()
         
    else:
        mainGame()

def mainGame():
    update()
    render()
        
    if points > 19:
        fill(255)
        text("YOU WIN!!", 280, 180)

def titleScreen():
    text("WELCOME TO VIDEOGAME!", 280, 50)


def update():
    global ball1, points, enemy1
    ball1.update()

    for e in enemy1:
        e.update()
        for b in ball1.bullet:
            if e.isCollision(b):
                enemy1.remove(e)
                points = points + 1
        
        
def render():
    ball1.render()
    
    for e in enemy1:
        e.render()
    
    fill(255)
    text(points, 40, 20)
    
def mousePressed():
    global startGame
    startGame = True
    ball1.fire()
    
# def keyPressed():
#     keyPr = 0
    
#     if key == "a" or key == "A":
#         keyPr = "a"
        
#     if key == "s" or key == "S":
#         keyPr = "s"
    
#     if key == "w" or key == "W":
#         keyPr = "w"
        
#     if key == "d" or key == "D":
#         keyPr = "d"
    
#     ball1.sendKeyDown(keypr)
        
