from Player import Player
class Volleyball_Rotations_Generator:
    homeRotation = None
    serveReceive = None
    setter, oh1, oh2, lib, mb1, mb2, rs = "", "", "", "", "", "", ""
    quadrants: dict
    maxLengthOfName = 0
    sittingMiddle: Player
    
    def __init__(self):
        self.homeRotation = None
        self.serveReceive = None

        
    def inputPlayers(self):
        """
        Gets the starting line up.
        Fills in the quadrants defaulted at rotation 1.
        Gets the max length of the names for formatting reasons. 
        """
        
        self.setter= Player(name = input("Who is your starting Setter?: "), pos = "S", row = input("Will this player play back-row (\"Back\"), front-row (\"Front\"), or both (\"Both\")?: "))
        self.rs = Player(name = input("Who is your starting Right Side?: "), pos = "RS", row = input("Will this player play back-row (\"Back\"), front-row (\"Front\"), or both (\"Both\")?: "))
        
        self.oh1 = Player(name = input("Who is your starting Outside Hitter 1?: "), pos = "OH1", row = input("Will this player play back-row (\"Back\"), front-row (\"Front\"), or both (\"Both\")?: "))
        self.oh2 = Player(name = input("Who is your starting Outside Hitter 2?: "), pos= "OH2", row = input("Will this player play back-row (\"Back\"), front-row (\"Front\"), or both (\"Both\")?: "))
        
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
    
        
        elif self.quadrants.get("Q1").getRow() == "Front":
            sub: Player = self.quadrants.get("Q1").getSub()
            self.quadrants["Q1"] = sub
            
        elif self.quadrants.get("Q4").getRow() == "Back":
            sub: Player = self.quadrants.get("Q4").getSub()
            self.quadrants["Q4"] = self.quadrants.get("Q4").getSub()
        
    def makeHomeRotation(self):
        ans = []
        count = 6
        
        while count > 0:
            try:
                frontRow = (self.quadrants.get("Q4"), self.quadrants.get("Q3"), self.quadrants.get("Q2"))
                backRow = (self.quadrants.get("Q5"), self.quadrants.get("Q6"), self.quadrants.get("Q1"))
                frontString = "|  {a}  |  {b}  |  {c}  |".format(a = frontRow[0].getName(), b = frontRow[1].getName(), c= frontRow[2].getName())
                backString = "|  {a}  |  {b}  |  {c}  |".format(a = backRow[0].getName(), b = backRow[1].getName(), c = backRow[2].getName())
            
            except:
                print(backString)
                print("Something")
            ans.append((frontString, backString))
            self.rotate()
    
            count -= 1
            
        count = 1
        for rotation in ans:
            frontRow, backRow = rotation
            print("Rotation {a}".format(a = count))
            print(frontRow)
            print(backRow)
            print("\n")
            count += 1
            
        
        
if __name__ == "__main__":
    generator = Volleyball_Rotations_Generator()
    # print("|  Name  |  helllo jds  |  fdsjkfls  |")
    generator.inputPlayers()
    
    generator.makeHomeRotation()
    # print(generator.quadrants.get("Q1").getPosition())
    
    
    
    
    
    
    