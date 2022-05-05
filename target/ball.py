from bullet import Bullet

class Ball(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speedx = 0
        self.speedy = 0
        self.bullet = []
        self.img = loadImage("ship.png")
        self.w = 32
        self.h = 32
        
        self.kPressed = { "w":0, 
                            "a":0,
                            "s":0,
                            "d":0}
        
        
    def update(self):
        
        
        
        if keyPressed == True:
 
                
            if key == "w" or key == "W":
                self.speedy -= 1
    
            if key == "s" or key == "S":
                self.speedy += 1
            
            if key == "a" or key == "A":
                self.speedx -= 1
            
            if key == "d" or key == "D":
                self.speedx += 1
        
        
        
        #Update x and y based on speed
        self.x += self.speedx
        self.y += self.speedy
        
        self.checkIfWall()
        
        #Apply friction
        self.speedx *= 0.95
        self.speedy *= 0.95
        
        for b in self.bullet:
            b.update()
            if b.x > 1280:
                self.bullet.remove(b)
        
    def render(self):
        
        for b in self.bullet:
            b.render()
           
        image(self.img, self.x - (self.w / 2), self.y - (self.h / 2))   
             
        # fill(255)
        # ellipse(self.x, self.y, 10,10)
        
        
        
    def checkIfWall(self):
        
        
        if self.y < 10:
            self.y = 12
            self.speedy = 1
            
        if self.y > 720:
            self.y = 715
            self.speedy = -1
            
        if self.x < 10:
            self.x = 12
            self.speedx = 1
            
        if self.x > 1000:
            self.x = 995
            self.speedx = -1
    
    def fire(self):
        self.bullet.append( Bullet(self.x, self.y))
        
    # def sendKeyDown(self, keyPr):
    #     for v in self.kPressed.keys():
    #         if keyPr == v:
    #             kPressed[v] = 1
