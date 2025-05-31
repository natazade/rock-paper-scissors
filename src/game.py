"""the game between user and computer. 

Author: Nahid Atazadeh
Date of created: 28.05.2025
Description: they have three choices: Rock, Paper, Scissors. Scissors crush Paper, Paper crush Rock and Rock crush Scissors.
"""


import random
from typing import List, Tuple, Dict


class RockPaperScissors:
   
    def __init__(self):          
        self.choices: List[str] = ['rock' , 'paper' , 'scissors']

    def get_player_choice(self) -> str:
        user_choice: str = input(f'please enter your choice: ({self.choices})')
        if user_choice.lower() in self.choices:
            return user_choice.lower()
        print(f'invalid choice. you must select from {self.choices}')
        return self.get_player_choice()   

    def get_computer_choice(self) -> str:
        return random.choice(self.choices)

    def decide_winner(self , user_choice: str , computer_choice: str) -> str:
        """ rerutn the winner between computer and user
                
        :param user_choice: the value that user choiced
        :param computer_choice: the value that comuter choiced
        :return: the winner
        """
        if user_choice == computer_choice:
            return 'It"s tie'
        winn_combinarions: List[Tuple[str,str]] = [('scissors' , 'paper'), ('paper' , 'rock') , ('rock' , 'scissors')]
        for win_comb in winn_combinarions:
            if (user_choice == win_comb[0]) and (computer_choice == win_comb[1]):
                return 'congratulations!  you won!'

        return 'oh no! the computer won!'        
  
    def play(self):
        """play between user and computer that select three value.
        - Get user choice.
        - Get computer choice.
        - Decide the winner.
        - Print the result.
        """
        user_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice() 
        winner_message = self.decide_winner(user_choice , computer_choice)   
        print(winner_message)
    
 
if __name__ == '__main__':
    game = RockPaperScissors()
    
    while True:
        game.play()

        computer_game = input('Dou you want to play again? (enter any key to play again, enter q/Q to exit)')
        if computer_game.lower() == 'q':
            break

