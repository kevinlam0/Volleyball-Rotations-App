from Player import Player

POSITION_MESSAGE = {
    "S": "Who is your starting Setter?: ",
    "OH1": "Who is your starting Outside Hitter 1?: ",
    "OH2": "Who is your starting Outside Hitter 2?: ",
    "RS": "Who is your starting Right Side?: ",
    "L": "Who is your starting Libero?: ",
    "MB1": "Who is your starting Middle Blocker 1?: ",
    "MB2": "Who is your starting Middle Blocker 2?: "
    }

class Lineup:
    setter: Player
    oh1: Player
    oh2: Player
    lib: Player 
    mb1: Player
    mb2: Player
    rs: Player 
    sitting_middle: Player
    
    def __init__(self):
        self.setter = self.rs = self.oh1 = self.oh2 = self.lib = self.mb1 = self.mb2 = None 
        self._input_player()
        
    def _input_player(self):
        sub = _get_sub_input()
        
        # If there will be subs
        if "y" in sub:
            self.setter = _make_player_sub("S")
            self.rs = _make_player_sub("RS")
            self.oh1 = _make_player_sub("OH1")
            self.oh2 = _make_player_sub("OH2")
        
        elif "n" in sub:
            self.setter= _make_player_no_sub("S")
            self.rs = _make_player_no_sub("RS")
            self.oh1 = _make_player_no_sub("OH1")
            self.oh2 = _make_player_no_sub("OH2")
        
        self.lib = Player(name = input("Who is your starting Libero?: "),pos = "L", row = "Back", lib = True)
        self.mb1 = Player(name = input("Who is your starting Middle Blocker 1?: "), pos = "MB1", row = "Front", lib = True)
        self.mb2 = Player(name = input("Who is your starting Middle Blocker 2?: "), pos = "MB2", row = "Front", lib = True)
        
def _get_sub_input() -> str:
    sub = input("Will there subs? (i.e. More than 7 starting players) (y/n): ").lower()
    while "y" not in sub and "n" not in sub:
        sub = input("Please input whether you want subs in your rotations (y/n): ").lower()
    return sub
def _make_player_sub(position: str) -> Player:
    row_string = "Will this player play back-row (\"Back\"), front-row (\"Front\"), or both (\"Both\")?: "
    message = POSITION_MESSAGE.get(position)
    return Player(name = input(message), pos=position.upper(), row = input(row_string))
def _make_player_no_sub(position: str) -> Player:
    message = POSITION_MESSAGE.get(position)
    return Player(input(message), position, "Both")

if __name__ == "__main__":
    hello = Lineup()