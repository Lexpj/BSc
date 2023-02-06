class Camera:
    
    def __init__(self):
        self.x = 0
        self.y = 0
        self.newx = 0
        self.newy = 0
        
        self.mult = 0.4
    
    def update(self):
        if self.x != self.newx:
            dif = self.newx-self.x
            self.x += dif * self.mult
            
        if self.y != self.newy:
            dif = self.newy-self.y
            self.y += dif * self.mult