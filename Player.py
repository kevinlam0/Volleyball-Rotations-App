class Player:
    position: str
    name: str
    row: str
    sub = None
    
    def __init__(self, name: str, pos: str, row: str, sub = None, lib = False):
        if name == "":
            raise Exception("You cannot have a blank name for a player.")
        
        
        self.name = name.capitalize()
        self.position = pos.upper()
        
        
        
        
        if "both" in row.lower():
            self.row = "Both"
        elif "front" in row.lower():
            self.row = "Front"
        elif "back" in row.lower():
            self.row = "Back"
        
        if not self.row == "Both" and sub == None and not lib:
            self.findSub(self.row)
        else:
            self.sub = sub
        
    
    def getName(self):
        return self.name
    
    def getPosition(self):
        return self.position
    
    def findSub(self, row):
        if row == "Front":
            self.sub = Player(input("Who is " + self.name + "'s back-row sub?: "), "DS", "Back", sub = self)
            
        elif row == "Back":
            self.sub = Player(input("Who is " + self.name + "'s front-row sub?: "), input("What is this player's position?: "), "Front", sub = self)
    
    def getSub(self):
        
        return self.sub
    
    def getRow(self):
        return self.row
    