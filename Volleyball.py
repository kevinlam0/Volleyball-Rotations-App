from Player import Player
class Volleyball_Rotations_Generator:
    homeRotation = None
    serveReceive = None
    setter, oh1, oh2, lib, mb1, mb2, rs = "", "", "", "", "", "", ""
    quadrants: dict
    maxLengthOfName = 0
    sittingMiddle: Player
    introduced = False
    
    def __init__(self):
        self.homeRotation = []
        self.serveReceive = None

        
    def inputPlayers(self):
        """
        Gets the starting line up.
        Fills in the quadrants defaulted at rotation 1.
        Gets the max length of the names for formatting reasons. 
        """
        sub = input("Will there subs? (i.e. More than 7 starting players) (y/n): ")
        row_string = "Will this player play back-row (\"Back\"), front-row (\"Front\"), or both (\"Both\")?: "
        
        # If there will be subs
        if "y" in sub.lower():
            self.setter = Player(name = input("Who is your starting Setter?: "), pos = "S", row = input(row_string))
            self.rs = Player(name = input("Who is your starting Right Side?: "), pos = "RS", row = input(row_string))
            
            self.oh1 = Player(name = input("Who is your starting Outside Hitter 1?: "), pos = "OH1", row = input(row_string))
            self.oh2 = Player(name = input("Who is your starting Outside Hitter 2?: "), pos= "OH2", row = input(row_string))
        
        else:
            self.setter= Player(name = input("Who is your starting Setter?: "), pos = "S", row = "Both")
            self.rs = Player(name = input("Who is your starting Right Side?: "), pos = "RS", row = "Both")
            
            self.oh1 = Player(name = input("Who is your starting Outside Hitter 1?: "), pos = "OH1", row = "Both")
            self.oh2 = Player(name = input("Who is your starting Outside Hitter 2?: "), pos= "OH2", row = "Both")
        
        self.lib = Player(name = input("Who is your starting Libero?: "),pos = "L", row = "Back", lib = True)
        self.mb1 = Player(name = input("Who is your starting Middle Blocker 1?: "), pos = "MB1", row = "Front", lib = True)
        self.mb2 = Player(name = input("Who is your starting Middle Blocker 2?: "), pos = "MB2", row = "Front", lib = True)
        
        self.quadrants = {"Q1": self.setter, "Q2": self.oh1, "Q3": self.mb2, "Q4": self.rs, "Q5": self.oh2, "Q6": self.lib}
        self.sittingMiddle = self.mb1
        
    
        # word_list = [self.setter.getName(), self.oh1.getName(), self.oh2.getName(), self.rs.getName(), self.mb1.getName(), self.mb2.getName(), self.lib.getName()]
        # for word in word_list:
        #     if len(word) > self.maxLengthOfName:
        #         self.maxLengthOfName = len(word)
        
    def rotate(self):
        """
        Rotates the players
        """
        
        # Store the first person
        first = self.quadrants.get("Q1")
        
        # Shift all players over from the next higher quadrant
        for i in range(1, 6):
            self.quadrants["Q" + str(i)] = self.quadrants.get("Q" + str(i + 1))
        
        # Put the first person in the missing quadrants
        self.quadrants["Q6"] = first
        
        # Adds libero logic
        if self.quadrants.get("Q4").getPosition() == "L":
            self.quadrants["Q4"] = self.sittingMiddle
            self.sittingMiddle = self.quadrants.get("Q1")
            self.quadrants["Q1"] = self.lib
    
        # Adding subbing of front row and back row    
        if self.quadrants.get("Q1").getRow() == "Front":
            sub: Player = self.quadrants.get("Q1").getSub()
            self.quadrants["Q1"] = sub
            
        if self.quadrants.get("Q4").getRow() == "Back":
            sub: Player = self.quadrants.get("Q4").getSub()
            self.quadrants["Q4"] = sub

    def displayRotation(self, rotation, positions): # rotation represents which rotation should be displayed
        # rotate appropriate amount of times to get to correct rotation
        for i in range(rotation - 1):
            self.rotate()

        try:
            # assign each player to default variables to be displayed
            frontRow = (self.quadrants.get("Q4"), self.quadrants.get("Q3"), self.quadrants.get("Q2"))
            backRow = (self.quadrants.get("Q5"), self.quadrants.get("Q6"), self.quadrants.get("Q1"))

            # after assigning frontRow and backRow, reset rotations for future use
            for i in range(7 - rotation):
                self.rotate()

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


    # edit starters
    def edit_player(self):
        player_row = ""
        print("\nPosition abbreviations: S, RS, OH1, OH2, L, MB1, MB2") # print possible positions to edit
        position = input("\nPlease enter the player's position you want to edit: ")
        
        # error check, loop until user has entered valid position
        while position != 'S' and position != 'RS' and position != 'OH1' and position != 'OH2' and position != 'L' and position != 'MB1' and position != 'MB2':
            position = input("Please enter a valid position: ")

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
        
        self.quadrants = {"Q1": self.setter, "Q2": self.oh1, "Q3": self.mb2, "Q4": self.rs, "Q5": self.oh2, "Q6": self.lib}
        self.sittingMiddle = self.mb1


    # add substitutes for starters
    def add_substitution(self):
        player_row = ""
        print("\nPosition abbreviations: S, RS, OH1, OH2")  # print possible positions to edit
        position = input("\nPlease enter the player's position you want to add a substitute for: ")
        
        # error check, loop until user has entered valid position
        while position != 'S' and position != 'RS' and position != 'OH1' and position != 'OH2':
            position = input("Please enter a valid position: ")
        
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

        # name of substitute
        new_name = input("What is the new substitute's name?: ")

        player_row = input("Will this player play back-row (\"Back\"), front-row (\"Front\"), or both (\"Both\")?: ")

        # set substitute based on given name and position
        if position == 'S':
            self.setter.setSub(new_name, position, player_row)
        elif position == 'RS':
            self.rs.setSub(new_name, position, player_row)
        elif position == 'OH1':
            self.oh1.setSub(new_name, position, player_row)
        elif position == 'OH2':
            self.oh2.setSub(new_name, position, player_row)
        
        self.quadrants = {"Q1": self.setter, "Q2": self.oh1, "Q3": self.mb2, "Q4": self.rs, "Q5": self.oh2, "Q6": self.lib}
        self.sittingMiddle = self.mb1

    
    # delete substitute for starters
    def delete_substitution(self):
        player_row = ""
        print("\nPosition abbreviations: S, RS, OH1, OH2")  # print possible positions to edit
        position = input("\nPlease enter the player's position you want to delete a substitute for\n(Note: if the player is a DS, enter which position that player is filling in for): ")
        
        # error check, loop until user has entered valid position
        while position != 'S' and position != 'RS' and position != 'OH1' and position != 'OH2':
            position = input("Please enter a valid position: ")
        
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

        self.quadrants = {"Q1": self.setter, "Q2": self.oh1, "Q3": self.mb2, "Q4": self.rs, "Q5": self.oh2, "Q6": self.lib}
        self.sittingMiddle = self.mb1


    def menu(self):
        global introduced
        if self.introduced == False:    # only print this once at the beginning
            print("Hello! Welcome to the Volleyball Rotations App!\nPlease enter your players.")
            self.inputPlayers()
            self.introduced = True

        print("\nPlease select a menu option by typing it in (1-3):")
        print("1. Display a rotation")
        print("2. Edit a rotation")
        print("3. Quit")

        # ask user for menu input, loop until they provide a valid option
        try:
            user_input = int(input())

        except:
            user_input = int(input("Please enter a valid menu option: "))

        while user_input < 1 or user_input > 3:
            user_input = int(input("Please enter a valid menu option: "))

        return user_input
    
        
if __name__ == "__main__":
    generator = Volleyball_Rotations_Generator()

    user_menu_input = generator.menu()

    while user_menu_input != 3: # while the user hasn't chosen to quit
        if user_menu_input == 1: # display rotation
            display_position = False    # tells if positions should be displayed on rotations

            print('Which rotation would you like displayed?\nPlease give a number 1-6, or type 0 to display all rotations')
            
            while True:
                try:    # error check, loop until user has entered valid option
                    rotation = int(input("Rotation: "))
                    while rotation > 6 or rotation < 0:
                        print('\nError: please give a number 1-6, or type 0 to display all rotations')
                        rotation = int(input("Rotation: "))
                    break

                except:
                    print('\nError: please give a number 1-6, or type 0 to display all rotations')
                    rotation = input("Rotation: ")
                    pass
            
            if "y" in input("Would you like to display every player's position? (y/n): ").lower():
                display_position = True

            if rotation != 0:   # display specific rotation
                print("\nRotation " + str(rotation))
                generator.displayRotation(rotation, display_position)

            else:
                for x in range(1,7):    # display rotations 1-6
                    print("\nRotation " + str(x))
                    generator.displayRotation(x, display_position)

        elif user_menu_input == 2:  # edit players
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
    # generator.inputPlayers()
    # generator.makeHomeRotation()
    # print("Kelly 5-1\n")
    # generator.printRotations(generator.homeRotation)
    # generator.inputPlayers()
    # generator.makeHomeRotation()
    # print("Niko 5-1")
    # generator.printRotations(generator.homeRotation)
    # # print("Kelly-Niko 6-2")
    # generator.inputPlayers()
    # generator.makeHomeRotation()
    # print("Kelly-Niko 6-2")
    # generator.printRotations(generator.homeRotation)

    # generator.inputPlayers()
    
    # generator.displayRotation(5, positions = True)
    # generator.makeHomeRotation(positions=True)
    # print("\nAdam-Niko 6-2")
    # generator.printRotations(generator.homeRotation)
    
