import Player
class Volleyball_Rotations_Generator:
    homeRotation = None
    serveReceive = None
    setter, oh1, oh2, lib, mb1, mb2, rs = "", "", "", "", "", "", ""
    quadrants = None
    maxLengthOfName = 0
    
    def __init__(self):
        self.homeRotation = None
        self.serveReceive = None

        
    def inputPlayers(self):
        """
        Gets the starting line up.
        Fills in the quadrants defaulted at rotation 1.
        Gets the max length of the names for formatting reasons. 
        """
        self.setter, self.oh1, self.oh2 = Player(input("Who is your starting Setter?: "), "S"), Player(input("Who is your starting Outside Hitter 1?: "), "OH1"), Player(input("Who is your starting Outside Hitter 2?: "), "OH2")
        self.lib, self.mb1, self.mb2, self.rs = Player(input("Who is your starting Libero?: "),"L") , Player(input("Who is your starting Middle Blocker 1?: "), "MB1"), Player(input("Who is your starting Middle Blocker 2?: "), "MB2"), Player(input("Who is your starting Right Side?: "), "RS")
        self.quadrants = {"Q1": self.setter, "Q2": self.oh1, "Q3": self.mb1, "Q4": self.rs, "Q5": self.oh2, "Q6": self.lib}
        
        word_list = [self.setter, self.oh1, self.oh2, self.rs, self.mb1, self.mb2, self.lib]
        for word in word_list:
            if len(word) > self.maxLengthOfName:
                self.maxLengthOfName = len(word)
        
    
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
        
    def makeHomeRotation(self):
        ans = []
        count = 6
        
        while count > 0:
            frontRow = (self.quadrants.get("Q4"), self.quadrants.get("Q3"), self.quadrants.get("Q2"))
            backRow = (self.quadrants.get("Q5"), self.quadrants.get("Q6"), self.quadrants.get("Q1"))
            frontString = "|  {a}  |  {b}  |  {c}  |".format(a = frontRow[0], b = frontRow[1], c= frontRow[2])
            backString = "|  {a}  |  {b}  |  {c}  |".format(a = backRow[0], b = backRow[1], c = backRow[2])
            ans.append((frontString, backString))
            self.rotate()
            count -= 1
            
        return ans 
        
        
if __name__ == "__main__":
    generator = Volleyball_Rotations_Generator()
    print("|  Name  |  helllo jds  |  fdsjkfls  |")
    generator.inputPlayers()
    
    rotations = generator.makeHomeRotation()
    count = 1
    for rotation in rotations:
        frontRow, backRow = rotation
        print("Rotation {a}".format(a = count))
        print(frontRow)
        print(backRow)
        print("\n")
        count += 1
    
    
    
    
    
    