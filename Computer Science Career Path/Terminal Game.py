# Import modules
import random

"""
Survive the night game 

- There will be a hunger, hydration and fatigue bar
- Stay warm (stoke the fire) (reduces fatigue and lowers danger)
- Stay awake to avoid danger
- Danger bar increases as fatigue bar increases, wild animals can smell you.
- Use random module to randomly decide whether an item break
- Instead of time, the player needs to get some goals achieved before they run out of turns, otherwise they've lost

"""


class Player:
    def __init__(self, hunger, fatigue, hydration):

        # Variable used to record the start of the game
        self.start_time = 0

        # Status
        self.alive = True
        self.hunger = hunger
        self.fatigue = fatigue
        self.hydration = hydration
        self.danger = 0

        # Inventory key (Dictionary holding the types of items. The dictionary inside each value is the item and the quantity of it left)
        self.inventory = { "drinks": [["Litres of coffee", 0.5], ["Litres of water", 2]]    , "food": [  ["Cheese sandwich", 2], ["Left-over pizza slices", 2]   ]  ,  "tools" : [  ["Matchstick", 2], ["Lighter", 1] ]} 

        # Tool status
        self.matchstick_active = False
        self.turns = 10

        # Start the game
        self.game() 

    def stoke_fire(self):
        # Check if a matchstick has been lit
        pass

    # Use items

    def quench_first(self):
        # Choose drink
        pass
    
    def eat_food(self, food_item_index):
        # Decrement the quantity of the food
        self.inventory["food"][food_item_index][1] -= 1

        # Display that the food item has been eaten
        print(f'{self.inventory["food"][food_item_index][0]} has been eaten!')

    def use_matchstick(self):
        #print(self.inventory["tools"]["Matchstick"])
        # Use random to decide whether the matchstick broke or not
        pass
    
    def use_lighter(self):
        pass


    # Support
    def ask_input(self, list_of_options, input_message):
        
        # Initial ask for user input
        action = input(input_message)

        # Keep asking for user input if the user entered unexpected input
        while action not in list_of_options:
            print("Invalid input!")
            action = input(input_message)

        return action


    def game(self):
        choosing_food = False

        # While the player is alive
        while self.alive == True:

            # Check that the player still has turns
            if self.turns <= 0:
                break


            # Display the players' current stats
            print(f"Hunger:{self.hunger}, Hydration:{self.hydration}, Fatigue:{self.fatigue}, Danger: {self.danger}")

            # Ask for user input from the player
            action = self.ask_input(["1", "2", "3"], "Eat food (1), Re-hydrate (2), Stoke fire (3) ")

            # Based on the action, do something
            match action:
                # Eat food
                case "1":
                    choosing_food = True 

            # Check if the player has chosen action 1
            if choosing_food == True:

                # Ask for user input from the player
                action = self.ask_input(["1", "2"],f'Eat one: {self.inventory["food"][0][0]} x {self.inventory["food"][0][1]} (1)  or {self.inventory["food"][1][0]} x {self.inventory["food"][1][1]} (2) ') 
                
                
                # Do the appropriate actions based on the choice made
                match action:
                    # Cheese sandwich
                    case "1":  
                        # If the quantity of food is greater than 0
                        if self.inventory["food"][0][1] > 0:
                            # Eat the cheese sandwich
                            self.eat_food(0) # Feed in the index that the food is at
                        else:
                            print(f'There are no more {self.inventory["food"][0][0]}es!')

                        # Set choosing food variable back to False
                        choosing_food = False
                        # Take a turn away from the player
                        self.turns -= 1

                    # Pizza slices
                    case "2":
                        # If the quantity of food is greater than 0
                        if self.inventory["food"][1][1] > 0:
                            # Eat the pizza slice
                            self.eat_food(1) # Feed in the index that the food is at
                        else:
                            print(f'There are no more {self.inventory["food"][1][0]}!')

                        # Set choosing food variable back to False
                        choosing_food = False
                        # Take a turn away from the player
                        self.turns -= 1


            # Do the following after every turn
            # Increase danger, hydration, hunger, fatigue
            self.danger += 15
            self.hydration -= 10
            self.fatigue += 10
            self.hunger += 15
  


player = Player(hunger = 0, hydration = 100, fatigue = 30)