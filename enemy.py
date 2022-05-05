class Enemy(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = loadImage("alien.png")
        self.h = 32
        self.w = 32
    def update(self):
        self.move()

        
    def move(self):
        self.x += random(-1,0)
        self.y += random(-2,2)
    
    def isCollision(self, b):
        if b.x + b.w > self.x and b.x - b.w < self.x + self.w and b.y > self.y - self.h/2 and b.y < self.y + self.h:
            return True
        else:
            return False
        
        
        # for bull in bullist:
            
        #     if bull.x > self.x:
        #         return True
            
        #     else:
        #         return False
        
        
        
    def render(self):
        image(self.img, self.x - self.w / 2 , self.y - self.h / 2)
        # fill(150, 150, 0)
        # rect(self.x, self.y, 15, 15)
        
    
