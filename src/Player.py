VALID_POSITIONS = {'S', 'RS', 'OH1', 'OH2', 'L', 'MB1', 'MB2', 'DS'} 
VALID_ROW = {'back', 'front', 'both'}
class Player:
    position: str
    name: str
    row: str
    sub = None
    
    def __init__(self, name: str, pos: str, row: str, sub = None, lib = False):
        self.name = _handle_name(name)
        self.position = _handle_position(pos)
        self.row = _handle_row(row)
        
        # Look for sub if the player does not play both rows
        if not self.row == "Both" and sub == None and not lib:
            self.find_sub()
        else:
            self.sub = sub
         
    def get_name(self) -> str:
        return self.name
    
    def get_position(self) -> str:
        return self.position
    
    def get_sub(self):
        return self.sub
    
    def get_row(self) -> str:
        return self.row
    
    def find_sub(self):
        if self.row == "Front":
            self.set_sub(input("Who is " + self.name + "'s back-row sub?: "), "DS", "Back")
            
        elif self.row == "Back":
            self.set_sub(input("Who is " + self.name + "'s front-row sub?: "), input("What is this player's position?: "), "Front")
    
    def set_sub(self, name, position, row):
        row = row.lower()
        if row == "front":
            self.sub = Player(name, position, row, sub = self)
            self.row = "Back"
        elif row == "back":
            self.sub = Player(name, position, row, sub = self)
            self.row = "Front"
            
    def delete_sub(self):
        self.sub = None
        self.row = "Both"
    
def _handle_name(name: str) -> str:
    while name.strip() == "":
        name = input("The name of this player cannot be blank. Please input a name: ")
    return name.capitalize()

def _handle_position(pos: str) -> str:
    playersPosition = pos.upper()
    while (playersPosition not in VALID_POSITIONS):
        playersPosition = input("Please input a valid position (S, OH1, OH2, RS, L, MB1, MB2): ").upper()
    return playersPosition.upper()

def _handle_row(row: str) -> str:
    row = row.lower()
    while row not in VALID_ROW:
        row = input("The row input was not valid. Please provide a row (Front, Back, Both): ").lower()
    return row.capitalize()