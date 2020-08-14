class Card:
    
    def __init__(self, color, rank):
        if color not in ["red", "yellow", "green"]:
            raise ValueError
        self.color = color 
        if rank not in range(0, 10):
            raise ValueError
        self.rank = rank 
    
    def score(self):
        color_values = {"red": 3, "yellow": 2, "green":1}
        return color_values[self.color] * self.rank 
    
