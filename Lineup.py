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
    quadrants: dict
    
    def __init__(self):
        self._input_player()
        self._reset_rotations()

        
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
        
        self.lib = _make_player_lib("L")
        self.mb1 = _make_player_lib("MB1")
        self.mb2 = _make_player_lib("MB2")
    def _reset_rotations(self):
        self.quadrants = {"Q1": self.setter, "Q2": self.oh1, "Q3": self.mb2, "Q4": self.rs, "Q5": self.oh2, "Q6": self.lib}
        self.sittingMiddle = self.mb1
    def _validate_row(self):
        for i in range(1,7):
            quadrant = "Q" + str(i)

            # if player is a backrow player but is in the front
            if self.quadrants.get(quadrant).getRow() == "Back" and 2 <= i <= 4:
                # is player is libero in the front
                if self.quadrants.get(quadrant).getPosition() == "L" and 2 <= i <= 4:
                    # calculate opposite quadrant to swap libero and middles in correct position
                    if i <= 3:
                        oppositeQuadrant = "Q" + str(i + 3)
                    else:
                        oppositeQuadrant = "Q" + str(i - 3)

                    self.quadrants[quadrant] = self.sittingMiddle
                    self.sittingMiddle = self.quadrants.get(oppositeQuadrant)
                    self.quadrants[oppositeQuadrant] = self.lib
                # non-libero backrow player in front
                else:
                    sub: Player = self.quadrants.get(quadrant).getSub()
                    self.quadrants[quadrant] = sub
            # else if player is a frontrow player but is in the back
            elif self.quadrants.get(quadrant).getRow() == "Front" and (i == 1 or i >= 5):
                sub: Player = self.quadrants.get(quadrant).getSub()
                self.quadrants[quadrant] = sub    
    def rotate(self, rotation: int):
        for i in range(rotation - 1):
            # Store the first person
            first = self.quadrants.get("Q1")
            
            # Shift all players over from the next higher quadrant
            for i in range(1, 6):
                self.quadrants["Q" + str(i)] = self.quadrants.get("Q" + str(i + 1))
            
            # Put the first person in the missing quadrants
            self.quadrants["Q6"] = first
        
        self._validate_row()
    def get_frontrow(self) -> tuple:
        q4: Player = self.quadrants.get("Q4")
        q3: Player = self.quadrants.get("Q3")
        q2: Player = self.quadrants.get("Q2")
        return (q4, q3, q2)
    def get_backrow(self) -> tuple:
        q5: Player = self.quadrants.get("Q5")
        q6: Player = self.quadrants.get("Q6")
        q1: Player = self.quadrants.get("Q1")
        return (q5, q6, q1)
def _get_sub_input() -> str:
    sub = input("Will there subs? (i.e. More than 7 starting players) (y/n): ").lower()
    while "y" not in sub and "n" not in sub:
        sub = input("Please input whether you want subs in your rotations (y/n): ").lower()
    return sub
def _make_player_sub(position: str) -> Player:
    row_string = "Will this player play back-row (\"Back\"), front-row (\"Front\"), or both (\"Both\")?: "
    message = POSITION_MESSAGE.get(position)
    return Player(name = input(message), pos = position, row = input(row_string))
def _make_player_no_sub(position: str) -> Player:
    message = POSITION_MESSAGE.get(position)
    return Player(input(message), pos=position, row = "Both")
def _make_player_lib(position: str) -> Player:
    row = "Back" if position.upper() == "L" else "Front"
    message = POSITION_MESSAGE.get(position)
    return Player(input(message), position, row, lib=True)
    
if __name__ == "__main__":
    hello = Lineup()