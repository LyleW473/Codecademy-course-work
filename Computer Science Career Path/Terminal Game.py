# Import modules
import pygame, random

# Initialise Pygame
pygame.init()

"""
Survive the night game 

- There will be a hunge, thirst and fatigue bar
- Stay warm (stoke the fire)
- Stay awake to avoid danger
- Danger bar increases as fatigue bar increases, wild animals can smell you.
- Use random module to randomly decide whether an item break
- The player must survive for (X) seconds/ minutes

"""


class Player:
    def __init__(self, hunger, fatigue, thirst):

        # Variable used to record the start of the game
        self.start_time = 0

        # Status
        self.alive = True
        self.hunger = hunger
        self.fatigue = fatigue
        self.thirst = thirst
        self.danger = 0

        # Inventory key (Dictionary holding the types of items. The dictionary inside each value is the item and the quantity of it left)
        self.inventory = { "drinks": {"Litres of coffee": 0.5, "Litres of water": 2}, "food": {"Cheese sandwich": 1, "Left-over Pizza slices": 2}, "tools" : {"Matchstick": 2, "Lighter": 1} } 

        # Tool status
        self.matchstick_active = False

        # Start the game
        self.game() 

    def stoke_fire(self):
        # Check if a matchstick has been lit
        pass

    def quench_first(self):
        # Choose drink
        pass
    
    def eat_food(self):
        # Choose food item
        pass

    def use_matchstick(self):
        # Use random to decide whether the matchstick broke or not
        pass
    
    def use_lighter(self):
        pass

    def game(self):
        input_process = False
        time_list_dictionary = {"start_time": 0, "total_elapsed_time": 0} 

        # While the player is alive
        while self.alive == True:
            # If the input process is active
            if input_process == False:

                # Record the time that the input process has been inactive
                if time_list_dictionary["start_time"] == 0: # If the start time has no value, then that means that its either been reset or hasn't started previously
                    time_list_dictionary["start_time"] = pygame.time.get_ticks()

                # TEST
                # pygame.time.delay(5000)
                # input_process = True

                # Record the time that the input process becomes active
                time_list_dictionary["total_elapsed_time"] += pygame.time.get_ticks() - time_list_dictionary["start_time"]
                # Reset the start time so that a new one can be recorded
                time_list_dictionary["start_time"] = 0

                # TEST
                # input_process = False
                 

            print(time_list_dictionary)



player = Player(100, 0, 0)