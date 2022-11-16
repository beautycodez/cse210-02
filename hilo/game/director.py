from game.card import Card
import random
class Director:
    def __init__(self):
        
        self.is_playing = True
        self.score = 300
        self.totalscore = 0
        self.card = random.randint(1,13)
        self.guess = ""
        
        

    def start_game (self):
        print (f"The card is {self.card} ")
        while self.is_playing:
            self.get_inputs ()
            self.do_updates ()
            self.print_output()
            self.get_guess()
        


    def get_inputs(self):
        """Ask the user is they want to keep playing

        Arg: 
            Self (Director): An instance of Director
        """

        play_turn = input ("Higher or lower? [h/l]")

        if play_turn == "h":
            self.score += 100

        play_turn = input ("Play again? [y/n]")
        self.is_playing = (play_turn == "y")
        
        

    def do_updates (self):
        if not self.is_playing:
            return
        card = Card ()
        self.card= card.see_card()  
        


    def print_output (self):
        print (f"The car is: {self.card}")

    def get_guess (self):
        self.guess = input ("Higher or lower? [h/l]")
    
        
        

        
        
