class Bullet(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speedx = 40
        self.w = 20
        self.h = 4
        
    def update(self):
        self.x += self.speedx
    

        
    def render(self):
        fill(255, 100,100)
        ellipse(self.x, self.y, self.w, self.h)
