from Lineup import Lineup
from Menu import Menu

class Volleyball_Rotations_Generator:
    court: Lineup
    menu: Menu
    
    def __init__(self):
        self.menu = Menu()
        self.court = Lineup()
            
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

    def edit_rotation(self):
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
            
        self.court.edit_lineup(user_input)
    
    def run_menu(self):
        user_input = self.menu.get_user_input()
        while user_input != 3:
            if user_input == 2:
                self.edit_rotation()
            elif user_input == 1:
                self.displayRotation()
            user_input = self.menu.get_user_input()
        
    def end(self):
        print("\nThank you for using our generator. Hope to see you again!\n")
        
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
            generator.edit_rotation()

        user_menu_input = generator.menu()
    
