from Player import Player
class Volleyball_Rotations_Generator:
    homeRotation = None
    serveReceive = None
    setter, oh1, oh2, lib, mb1, mb2, rs = "", "", "", "", "", "", ""
    quadrants: dict
    maxLengthOfName = 0
    sittingMiddle: Player
    
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

    def displayRotation(self, rotation, positions = False): # rotation represents which rotation should be displayed
        for i in range(rotation - 1):
            self.rotate()

        try:
            frontRow = (self.quadrants.get("Q4"), self.quadrants.get("Q3"), self.quadrants.get("Q2"))
            backRow = (self.quadrants.get("Q5"), self.quadrants.get("Q6"), self.quadrants.get("Q1"))
            a = frontRow[0].getName()
            b = frontRow[1].getName()
            c = frontRow[2].getName()
            d = backRow[0].getName()
            e = backRow[1].getName()
            f = backRow[2].getName()

            if positions:
                p1 = frontRow[0].getPosition()
                p2 = frontRow[1].getPosition()
                p3 = frontRow[2].getPosition()
                p4 = backRow[0].getPosition()
                p5 = backRow[1].getPosition()
                p6 = backRow[2].getPosition()
                print(f'|{a + " (" + p1 + ")":^15}|{b + " (" + p2 + ")":^15}|{c + " (" + p3 + ")":^15}|')
                print(f'|{d + " (" + p4 + ")":^15}|{e + " (" + p5 + ")":^15}|{f + " (" + p6 + ")":^15}|')

            else:
                print(f'|{a:^15}|{b:^15}|{c:^15}|')
                print(f'|{d:^15}|{e:^15}|{f:^15}|')

        except: 
            print("Something wrong occurred while creating strings of front-row and back-row.")
        
        
    # def makeHomeRotation(self, positions = False):
    #     count = 6
    #     self.homeRotation = []
    
    #     while count > 0:
    #         try:
    #             frontRow = (self.quadrants.get("Q4"), self.quadrants.get("Q3"), self.quadrants.get("Q2"))
    #             backRow = (self.quadrants.get("Q5"), self.quadrants.get("Q6"), self.quadrants.get("Q1"))
    #             if positions:
    #                 frontString = "|  {a} ({p1})  |  {b} ({p2})  |  {c} ({p3})  |".format(a = frontRow[0].getName(), b = frontRow[1].getName(), c= frontRow[2].getName(), p1 = frontRow[0].getPosition(), p2 = frontRow[1].getPosition(), p3 = frontRow[2].getPosition())
    #                 backString = "|  {a} ({p1})  |  {b} ({p2})  |  {c} ({p3})  |".format(a = backRow[0].getName(), b = backRow[1].getName(), c= backRow[2].getName(), p1 = backRow[0].getPosition(), p2 = backRow[1].getPosition(), p3 = backRow[2].getPosition())
    #             else:
    #                 frontString = "|  {a}  |  {b}  |  {c}  |".format(a = frontRow[0].getName(), b = frontRow[1].getName(), c= frontRow[2].getName())
    #                 backString = "|  {a}  |  {b}  |  {c}  |".format(a = backRow[0].getName(), b = backRow[1].getName(), c = backRow[2].getName())

    #         except: 
    #             print("Something wrong occurred while creating strings of front-row and back-row.")
                
    #         self.homeRotation.append((frontString, backString))
    #         self.rotate()
    #         count -= 1
    
    # def printRotations(self, rotations):
    #     count = 1
    #     # print("\n")
    #     for rotation in rotations:
    #         frontRow, backRow = rotation
    #         print("Rotation {a}".format(a = count))
    #         print(frontRow)
    #         print(backRow + "\n")
    #         count += 1
            
    
        
if __name__ == "__main__":
    generator = Volleyball_Rotations_Generator()
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

    generator.inputPlayers()
    
    generator.displayRotation(5, positions = True)
    # generator.makeHomeRotation(positions=True)
    # print("\nAdam-Niko 6-2")
    # generator.printRotations(generator.homeRotation)
    
    
    
    
    
    
    