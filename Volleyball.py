from Player import Player
from Lineup import Lineup
VALID_SUBS = {"S": {"S", "RS", "DS"}, "RS": {"S", "DS", "RS"}, "OH1": {"DS"}, "OH2": {"DS"}}

class Volleyball_Rotations_Generator:
    introduced: bool
    court: Lineup
    
    def __init__(self):
        self.court = Lineup()
        self.introduced = False
    
    # def inputPlayers(self):
    #     """
    #     Gets the starting line up.
    #     Fills in the quadrants defaulted at rotation 1.
    #     Gets the max length of the names for formatting reasons. 
    #     """
    #     sub = input("Will there subs? (i.e. More than 7 starting players) (y/n): ").lower()
    #     while "y" not in sub and "n" not in sub:
    #         sub = input("Please input whether you want subs in your rotations (y/n): ").lower()
            
    #     row_string = "Will this player play back-row (\"Back\"), front-row (\"Front\"), or both (\"Both\")?: "
        
    #     # If there will be subs
    #     if "y" in sub:
    #         self.setter = Player(name = input("Who is your starting Setter?: "), pos = "S", row = input(row_string))
    #         self.rs = Player(name = input("Who is your starting Right Side?: "), pos = "RS", row = input(row_string))
            
    #         self.oh1 = Player(name = input("Who is your starting Outside Hitter 1?: "), pos = "OH1", row = input(row_string))
    #         self.oh2 = Player(name = input("Who is your starting Outside Hitter 2?: "), pos= "OH2", row = input(row_string))
        
    #     elif "n" in sub:
    #         self.setter= Player(name = input("Who is your starting Setter?: "), pos = "S", row = "Both")
    #         self.rs = Player(name = input("Who is your starting Right Side?: "), pos = "RS", row = "Both")
            
    #         self.oh1 = Player(name = input("Who is your starting Outside Hitter 1?: "), pos = "OH1", row = "Both")
    #         self.oh2 = Player(name = input("Who is your starting Outside Hitter 2?: "), pos= "OH2", row = "Both")
        
    #     self.lib = Player(name = input("Who is your starting Libero?: "),pos = "L", row = "Back", lib = True)
    #     self.mb1 = Player(name = input("Who is your starting Middle Blocker 1?: "), pos = "MB1", row = "Front", lib = True)
    #     self.mb2 = Player(name = input("Who is your starting Middle Blocker 2?: "), pos = "MB2", row = "Front", lib = True)
        
    #     self.reset_rotations()
    
    # def rotate(self, rotation):
    #     """
    #     Rotates the players
    #     """
        
    #     for i in range(rotation - 1):
    #         # Store the first person
    #         first = self.quadrants.get("Q1")
            
    #         # Shift all players over from the next higher quadrant
    #         for i in range(1, 6):
    #             self.quadrants["Q" + str(i)] = self.quadrants.get("Q" + str(i + 1))
            
    #         # Put the first person in the missing quadrants
    #         self.quadrants["Q6"] = first
        
    #     self.validate_row()

    # def validate_row(self):
    #     for i in range(1,7):
    #         quadrant = "Q" + str(i)

    #         # if player is a backrow player but is in the front
    #         if self.quadrants.get(quadrant).getRow() == "Back" and 2 <= i <= 4:
    #             # is player is libero in the front
    #             if self.quadrants.get(quadrant).getPosition() == "L" and 2 <= i <= 4:
    #                 # calculate opposite quadrant to swap libero and middles in correct position
    #                 if i <= 3:
    #                     oppositeQuadrant = "Q" + str(i + 3)
    #                 else:
    #                     oppositeQuadrant = "Q" + str(i - 3)

    #                 self.quadrants[quadrant] = self.sittingMiddle
    #                 self.sittingMiddle = self.quadrants.get(oppositeQuadrant)
    #                 self.quadrants[oppositeQuadrant] = self.lib
    #             # non-libero backrow player in front
    #             else:
    #                 sub: Player = self.quadrants.get(quadrant).getSub()
    #                 self.quadrants[quadrant] = sub
    #         # else if player is a frontrow player but is in the back
    #         elif self.quadrants.get(quadrant).getRow() == "Front" and (i == 1 or i >= 5):
    #             sub: Player = self.quadrants.get(quadrant).getSub()
    #             self.quadrants[quadrant] = sub

            
    def displayRotation(self, rotation, positions):
        """
        This function prints out the input rotations. 

        Args:
            rotation (int): This will tell the functions which rotation to print
            positions (boolean): This will tell the function whether or not they want the positions of the players printed. 
        """
        # rotate appropriate amount of times to get to correct rotation
        # self.rotate(rotation)
        self.court.rotate(rotation)

        try:
            # Get the players in the correct row
            frontRow: tuple = self.court.get_frontrow()
            backRow: tuple = self.court.get_backrow()
            # frontRow = (self.quadrants.get("Q4"), self.quadrants.get("Q3"), self.quadrants.get("Q2"))
            # backRow = (self.quadrants.get("Q5"), self.quadrants.get("Q6"), self.quadrants.get("Q1"))

            # after assigning frontRow and backRow, reset rotations for future use
            self.court.reset_rotations()

            # 6 players for current specified rotation
            a = frontRow[0].getName()
            b = frontRow[1].getName()
            c = frontRow[2].getName()
            d = backRow[0].getName()
            e = backRow[1].getName()
            f = backRow[2].getName()

            if positions:   # if positions are to be displayed, assign each position to default variables
                p1 = frontRow[0].getPosition()
                p2 = frontRow[1].getPosition()
                p3 = frontRow[2].getPosition()
                p4 = backRow[0].getPosition()
                p5 = backRow[1].getPosition()
                p6 = backRow[2].getPosition()

                # print with equally spaced columns (15 characters wide)
                print(f'|{a + " (" + p1 + ")":^15}|{b + " (" + p2 + ")":^15}|{c + " (" + p3 + ")":^15}|')
                print(f'|{d + " (" + p4 + ")":^15}|{e + " (" + p5 + ")":^15}|{f + " (" + p6 + ")":^15}|')

            else:   # if positions are not to be displayed, only print the players out
                print(f'|{a:^15}|{b:^15}|{c:^15}|')
                print(f'|{d:^15}|{e:^15}|{f:^15}|')

        except: 
            print("Something wrong occurred while creating strings of front-row and back-row.")

    def edit_player(self):
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

    def add_substitution(self):
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

    def delete_substitution(self):
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

    def menu(self) -> int:
        """
        This will be the menu that asks for the user's input of what they want to do
        Returns:
            int: This will tell us what the user wants to do
        """
        
        # Only printing the introduction once
        if self.introduced == False:    
            print("Hello! Welcome to the Volleyball Rotations App!\nPlease enter your players.")
            self.introduced = True

        # Print the options
        print("\nPlease select a menu option by typing it in (1-3):")
        print("1. Display a rotation")
        print("2. Edit a rotation")
        print("3. Quit")

        # Asking for the users' input until they provide a valid input. 
        try:
            user_input = int(input())

        except:
            user_input = int(input("Please enter a valid menu option: "))

        while not (1 <= user_input <= 3):
            user_input = int(input("Please enter a valid menu option: "))

        return user_input
    
    # def reset_rotations(self):
    #     self.quadrants = {"Q1": self.setter, "Q2": self.oh1, "Q3": self.mb2, "Q4": self.rs, "Q5": self.oh2, "Q6": self.lib}
    #     self.sittingMiddle = self.mb1
        
if __name__ == "__main__":
    generator = Volleyball_Rotations_Generator()

    user_menu_input = generator.menu()

    # Run until user quits
    while user_menu_input != 3: 
        
        # ---- Displays rotatino ---- 
        if user_menu_input == 1: 
            # Boolean for displaying the positions
            display_position = False    

            print('Which rotation would you like displayed?\nPlease give a number 1-6, or type 0 to display all rotations')
            
            # Searching for a valid rotaton to display
            while True:
                try:    
                    rotation = int(input("Rotation: "))
                    while not (0 <= rotation <= 6):
                        print('\nError: please give a number 1-6, or type 0 to display all rotations')
                        rotation = int(input("Rotation: "))
                    break

                except:
                    print('\nError: please give a number 1-6, or type 0 to display all rotations')
                    rotation = int(input("Rotation: "))
                    pass
            
            display = input("Would you like to display every player's position? (y/n): ").lower()
            while "y" not in display and "n" not in display:
                display = input("Please choose whether or not you want to display the rotations (y/n): ").lower()
                
            if "y" in display:
                display_position = True

            # Display every rotation
            if rotation == 0:
                for i in range(1, 7):
                    print("\nRotation {a}".format(a = i))
                    generator.displayRotation(i, display_position)
                  
            # Display specific rotation  
            else:
                print("\nRotation " + str(rotation))
                generator.displayRotation(rotation, display_position)

        # ---- Edit players or subs ----
        elif user_menu_input == 2:  
            user_input = ""
            
            print("\nPlease select a menu option by typing it in (1-3):")
            print("1. Edit a player")
            print("2. Add a substitution")
            print("3. Delete a substitution ")

            try:    # error check, loop until user has entered valid option
                user_input = int(input())

            except:
                user_input = int(input("Please enter a valid menu option: "))

            while user_input < 1 or user_input > 3:
                user_input = int(input("Please enter a valid menu option: "))

            if user_input == 1: # edit a starter
                generator.edit_player()

            if user_input == 2: # add a substitute
                generator.add_substitution()

            if user_input == 3: # delete a substitute
                generator.delete_substitution()

        user_menu_input = generator.menu()
    
