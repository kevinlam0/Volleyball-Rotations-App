class Menu:
    def __init__(self):
        self._introduce()
        
    def _introduce(self):
        print("\nHello! Welcome to the Volleyball Rotations App!\nPlease enter your players.")
    
    def get_user_input(self) -> int:
        print("\nPlease select a menu option by typing it in (1-3):")
        print("1. Display a rotation")
        print("2. Edit a rotation")
        print("3. Quit")
        
        try:
            user_input = int(input())

        except:
            user_input = int(input("Please enter a valid menu option: "))

        while not (1 <= user_input <= 3):
            user_input = int(input("Please enter a valid menu option: "))
            
        return user_input