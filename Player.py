class Player:
    position: str
    name: str
    
    def __init__(self, name: str, pos: str):
        self.name = name
        self.position = pos
    
    def getName(self):
        return self.name
    
    def getPosition(self):
        return self.position
    