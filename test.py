class Test(object):
    def __init__(self, x):
        self.x = x
        
    def update(self):
        self.x += 1
        
    def render(self):
        rect(self.x, 100, 50,50)