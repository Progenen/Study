class Rectangle:
    def __init__(self, a, b):
        self.a = a,
        self.b = b,

    def get_sqr (self):
        return self.a * self.b
    
    def get_perimeter (self):
        return (self.a + self.b) * 2
        
    def get_ratio (self):
        if (self.a > self.b):
            return self.a / self.b
        
        return self.b / self.a