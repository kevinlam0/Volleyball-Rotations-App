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
VALID_SUBS = {
    "S": {"S", "RS", "DS"}, 
    "RS": {"S", "DS", "RS"}, 
    "OH1": {"DS"}, 
    "OH2": {"DS"}
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
        self.reset_rotations()

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
    def reset_rotations(self):
        self.quadrants = {"Q1": self.setter, "Q2": self.oh1, "Q3": self.mb2, "Q4": self.rs, "Q5": self.oh2, "Q6": self.lib}
        self.sittingMiddle = self.mb1
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

    # ---- Rotate players in the lineup ---- # 
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

    # ---- Edit Lineup ---- #
    def edit_lineup(self, edit: int):
        if edit == 1:
            self._edit_player()
        elif edit == 2:
            self._add_substitution()
        elif edit == 3:
            self._delete_substitution()     
    # - Specific private lineup edit methods - #
    def _edit_player(self):
        """
        This function edits the starters
        It will replace the old player with a new Player obj
        """
        
        # Print out all the positions
        print("\nPosition abbreviations: S, RS, OH1, OH2, L, MB1, MB2") 
        
        # Grab a valid position 
        position = input("\nPlease enter the player's position you want to edit or \"Q\" if you want to quit editing player: ").upper()
        possible_inputs = {"RS", "S", "OH1", "OH2", "MB1", "MB2", "L", "Q"}
        
        # error check, loop until user has entered valid position
        while position not in possible_inputs: 
            position = input("Please enter a valid position or quit (Q): ").upper()

        if position == "Q":
            return 
        
        # name of new player
        new_name = input("What is the new " + position + "'s name?: ")

        # only ask if player will play front/back row if they are Wing Player/Setter
        if position != 'L' and position != 'MB1' and position != 'MB2':
            player_row = input("Will this player play back-row (\"Back\"), front-row (\"Front\"), or both (\"Both\")?: ")

        # create new player based on given position and name
        if position == 'S':
            self.setter = Player(new_name, pos = "S", row = player_row)
        elif position == 'RS':
            self.rs = Player(new_name, pos = "RS", row = player_row)
        elif position == 'OH1':
            self.oh1 = Player(new_name, pos = "OH1", row = player_row)
        elif position == 'OH2':
            self.oh2 = Player(new_name, pos = "OH2", row = player_row)
        elif position == 'L':
            self.lib = Player(new_name, pos = "L", row = "Back", lib = True)
        elif position == 'MB1':
            self.mb1 = Player(new_name, pos = "MB1", row = "Front", lib = True)
        elif position == 'MB2':
            self.mb2 = Player(new_name,pos = "MB2", row = "Front", lib = True)
        
        self.reset_rotations()    
    def _add_substitution(self):
        """
        Adds a sub to a starter.
        Only can add to S, RS, or OHs
        There are validations to make sure the input of the sub is legal
        """
        
        # Print all valid positions to add subs to
        print("\nPosition abbreviations: S, RS, OH1, OH2") 
        position = input("\nPlease enter the player's position you want to add a substitute for or \"Q\" if you want to quit adding a sub: ").upper()
        possible_inputs = {"S", "RS", "OH1", "OH2", "Q"}
        
        # Error checking, making sure the position input is valid
        while position not in possible_inputs:
            position = input("Please enter a valid position or quit (Q): ").upper()
        
        if position == "Q":
            return 
        
        # if given position's row is set to either 'Front' or 'Back,' they already have a substitute
        if position == 'S' and self.setter.getRow() != 'Both':
            print("The Setter already has a substitute.")
            return
        elif position == 'RS' and self.rs.getRow() != 'Both':
            print("The Right Side already has a substitute.")
            return
        elif position == 'OH1' and self.oh1.getRow() != 'Both':
            print("The Outside Hitter 1 already has a substitute.")
            return
        elif position == 'OH2' and self.oh2.getRow() != 'Both':
            print("The Outside Hitter 2 already has a substitute.")
            return

        # Getting information on the sub
        new_name = input("What is the new substitute's name?: ")
        player_row = input("Will this player play back-row (\"Back\"), front-row (\"Front\"), or both (\"Both\")?: ")
        
        # Only ask for the sub's position if it is for a setter or right side
        if "S" in position:
            subs_position = input("What is this sub's position?: ").upper()
            
            # Make sure the sub has a valid position for the person they are subbing in for. 
            if position == 'S':
                while subs_position not in VALID_SUBS[position]:
                    subs_position = input("Please provide a valid position for the sub of a setter (S, RS, DS): ").upper()
                self.setter.setSub(new_name, subs_position, player_row)
                
            elif position == 'RS':
                while subs_position not in VALID_SUBS[position]:
                    subs_position = input("Please provide a valid position for the sub of a right side (S, RS, DS): ").upper()
                print(new_name, subs_position, player_row)
                self.rs.setSub(new_name, subs_position, player_row)
            
        elif position == 'OH1':
            self.oh1.setSub(new_name, "DS", player_row)
        elif position == 'OH2':
            self.oh2.setSub(new_name, "DS", player_row)
        
        self.reset_rotations()
    def _delete_substitution(self):
        """
        Deletes a substitute of a starter if the sub exists.
        Will only delete S, RS, or OHs
        """
        
        # Print out the possible positions to delete from. 
        print("\nPosition abbreviations: S, RS, OH1, OH2") 
        position = input("\nPlease enter the player's position you want to delete a substitute for or \"Q\" to quit deleting a player.\n(Note: if the player is a DS, enter which position that player is filling in for): ").upper()
        possible_inputs = {"S", "RS", "OH1", "OH2", "Q"}
        
        # error check, loop until user has entered valid position
        while position not in possible_inputs:
            position = input("Please enter a valid position or quit (Q): ").upper()
        
        if position == "Q":
            return 
        
        # if row is set to 'Both,' they don't have an existing substitute
        if position == 'S' and self.setter.getRow() == 'Both':
            print("The Setter has no substitute to delete.")
            return
        elif position == 'RS' and self.rs.getRow() == 'Both':
            print("The Right Side has no substitute to delete.")
            return
        elif position == 'OH1' and self.oh1.getRow() == 'Both':
            print("The Outside Hitter 1 has no substitute to delete.")
            return
        elif position == 'OH2' and self.oh2.getRow() == 'Both':
            print("The Outside Hitter 2 has no substitute to delete.")
            return

        # delete substitute if one exists
        if position == 'S':
            self.setter.deleteSub()
        elif position == 'RS':
            self.rs.deleteSub()
        elif position == 'OH1':
            self.oh1.deleteSub()
        elif position == 'OH2':
            self.oh2.deleteSub()

        self.reset_rotations()

# ---- Private helper methods ---- #
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