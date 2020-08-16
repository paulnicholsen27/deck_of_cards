class Card:
    
    def __init__(self, color, rank):
        if color.lower() not in ["red", "yellow", "green"]:
            raise ValueError("Color must be 'red', 'yellow' or 'green'.")
        self.color = color.lower() 
        if rank not in range(0, 10):
            raise ValueError("Rank must be an integer between 0-9, inclusive.")
        self.rank = rank 
    
    def score(self):
        color_values = {"red": 3, "yellow": 2, "green":1}
        return color_values[self.color] * self.rank 
    
