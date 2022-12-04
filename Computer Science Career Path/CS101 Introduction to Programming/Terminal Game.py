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
        self.inventory = { "drinks": [["Coffee", 0.5], ["Water", 2]]    , "food": [  ["Cheese sandwich", 2], ["Left-over pizza slices", 2]   ]  ,  "tools" : [  ["Matchstick", 2], ["Lighter", 1] ]} 

        # Tool status
        self.matchstick_active = False
        self.turns = 10

        # Display the players' initial stats
        print("-------------------------------------------------------------------------------------------------")
        print(f"Hunger:{self.hunger}, Hydration:{self.hydration}, Fatigue:{self.fatigue}, Danger: {self.danger}, Turns remaining: {self.turns}")
        print("-------------------------------------------------------------------------------------------------")

        # Start the game
        self.game() 

    # Use items

    def quench_thirst(self, drink_item_index):

        # If the drink was coffee
        if drink_item_index == 0:
            # Decrement the quantity of the drink
            self.inventory["drinks"][drink_item_index][1] -= 0.25
            # Decrease fatigue (The minimum value is 0
            self.fatigue = max(0, self.fatigue - 40)
            # Increase hydration slightly (The maximum value is 100)
            self.hydration = min(self.hydration + 10, 100)
            # Display message
            print(f'0.25 litres of {self.inventory["drinks"][drink_item_index][0]} has been consumed! Fatigue is now {self.fatigue}! Hydration is now at {self.hydration}! You are feeling refreshed!')


        # If the drink was water
        elif drink_item_index == 1:
            # Decrement the quantity of the drink
            self.inventory["drinks"][drink_item_index][1] -= 0.5
            # Increase hydration (The maximum value is 100)
            self.hydration = min(self.hydration + 30, 100)
            # Display message
            print(f'0.5 litres of {self.inventory["drinks"][drink_item_index][0]} has been consumed! Hydration is now {self.hydration}! That hit the spot..')
    

    def eat_food(self, food_item_index):
        # Decrement the quantity of the food
        self.inventory["food"][food_item_index][1] -= 1

        # Decrease hunger (The mninimum value is 0)
        self.hunger = max(0, self.hunger - 30)

        # Display that the food item has been eaten
        print(f'{self.inventory["food"][food_item_index][0]} has been eaten! Hunger is now {self.hunger}!')

    def light_fire(self, tool_item_index):
        # 20 % chance of breaking
        matchstick_random_number = random.randrange(0, 4)
        # 5 % chance of breaking
        lighter_random_number = random.randrange(0, 19) 

        # If the matchstick was used
        if tool_item_index == 0:
            # If the random number is 3, then the matchstick broke
            if matchstick_random_number == 3: # 3 = random selected number
                print(f'The {self.inventory["tools"][tool_item_index][0]} broke!')

            # If it isn't then the fire was successfully lit
            else:
                # Decrease danger (The minimum value is 0)
                self.danger = max(0, self.danger - 10)
                # Display message
                print(f'The {self.inventory["tools"][tool_item_index][0]} successfully lit a fire! With light you feel more comfortable! Danger is now at {self.danger}')

            # Decrement the quantity of the tool (regardless of whether it was successful or not)
            self.inventory["tools"][tool_item_index][1] -= 1

        # If the lighter was used
        if tool_item_index == 1:
            # If the random number is 9, then the lighter broke
            if lighter_random_number == 9: # 9 = random selected number
                print(f'The {self.inventory["tools"][tool_item_index][0]} stopped working!')
                # Decrement the quantity of the tool as it is no longer working
                self.inventory["tools"][tool_item_index][1] -= 1

            # If it isn't then the fire was successfully lit
            else:
                # Decrease danger (The minimum value is 0)
                self.danger = max(0, self.danger - 10)
                # Display message
                print(f'The {self.inventory["tools"][tool_item_index][0]} successfully lit a fire! With light you feel more comfortable! Danger is now at {self.danger}')


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

        # Actions 
        choosing_action = True
        choosing_food = False
        choosing_drink = False
        choosing_tool = False

        # While the player is alive
        while self.alive == True:

            # Check that the player still has turns
            if self.turns <= 0:
                break

            # If the player can choose an action
            if choosing_action == True:
                # Ask for user input from the player
                action = self.ask_input(["1", "2", "3"], "Eat food (1), Re-hydrate (2), Light a fire (3) ")

                # Based on the action, do something
                match action:
                    # Eat food
                    case "1":
                        choosing_food = True
                    # Re-hydrate
                    case "2":
                        choosing_drink = True
                    # Light a fire
                    case "3":
                        choosing_tool = True

                # Set choosing action to False
                choosing_action = False

            # Check if the player has chosen action 1
            if choosing_food == True:

                # Ask for user input from the player
                action = self.ask_input(["1", "2", "3"],f'Eat one: {self.inventory["food"][0][0]} x {self.inventory["food"][0][1]} (1)  or {self.inventory["food"][1][0]} x {self.inventory["food"][1][1]} (2) or Go back (3) ') 
                
                
                # Do the appropriate actions based on the choice made
                match action:
                    # Cheese sandwich
                    case "1":  
                        # If the quantity of food is greater than 0
                        if self.inventory["food"][0][1] > 0:
                            # Eat the cheese sandwich
                            self.eat_food(0) # Feed in the index that the food is at in the list
                            # Set choosing food variable back to False
                            choosing_food = False
                            # Take a turn away from the player
                            self.turns -= 1
                        else:
                            print(f'There are no more {self.inventory["food"][0][0]}es!')


                    # Pizza slices
                    case "2":
                        # If the quantity of food is greater than 0
                        if self.inventory["food"][1][1] > 0:
                            # Eat the pizza slice
                            self.eat_food(1) # Feed in the index that the food is at in the list
                            # Set choosing food variable back to False
                            choosing_food = False
                            # Take a turn away from the player
                            self.turns -= 1
                        else:
                            print(f'There are no more {self.inventory["food"][1][0]}!')

                    # Go back
                    case "3":
                        # Go back to choosing the action
                        choosing_food = False
                        choosing_action = True

            # Check if the player has chosen action 2:
            if choosing_drink == True:

                # Ask for user input from the player
                action = self.ask_input(["1", "2", "3"],f'Drink 250 ml: {self.inventory["drinks"][0][0]} x {self.inventory["drinks"][0][1]} (1)  or {self.inventory["drinks"][1][0]} x {self.inventory["drinks"][1][1]} (2) or Go back (3) ') 
            
                # Do the appropriate actions based on the choice made
                match action:
                    # Coffee
                    case "1":  
                        # If the quantity of the drink is greater than 0
                        if self.inventory["drinks"][0][1] > 0:
                            # Drink coffee
                            self.quench_thirst(0) # Feed in the index that the drink is at in the list
                            # Set choosing drink variable back to False
                            choosing_drink = False
                            # Take a turn away from the player
                            self.turns -= 1          
                        else:
                            print(f'There is no more {self.inventory["drinks"][0][0]}!')

                    # Water
                    case "2":  
                        # If the quantity of the drink is greater than 0
                        if self.inventory["drinks"][1][1] > 0:
                            # Drink water
                            self.quench_thirst(1) # Feed in the index that the drink in the list

                            # Set choosing drink variable back to False
                            choosing_drink = False
                            # Take a turn away from the player
                            self.turns -= 1
                        else:
                            print(f'There is no more {self.inventory["drinks"][1][0]}!')

                    # Go back
                    case "3":
                        # Go back to choosing the action
                        choosing_drink = False
                        choosing_action = True

            # Check if the player has chosen action 3:
            if choosing_tool == True:
                # Ask for user input from the player
                action = self.ask_input(["1", "2", "3"],f'Use one: {self.inventory["tools"][0][0]} x {self.inventory["tools"][0][1]} (1)  or {self.inventory["tools"][1][0]} x {self.inventory["tools"][1][1]} (2) or Go back (3) ') 
            
                # Do the appropriate actions based on the choice made
                match action:
                    # Matchstick
                    case "1":  
                        # If the quantity of the tool is greater than 0
                        if self.inventory["tools"][0][1] > 0:
                            # Light a fire using a matchstick
                            self.light_fire(0)
                            # Set choosing_tool variable back to False
                            choosing_tool = False
                            # Take a turn away from the player
                            self.turns -= 1          
                        else:
                            print(f'You broke all the {self.inventory["tools"][0][0]}s...')

                    # Lighter
                    case "2":  
                        # If the quantity of the tool is greater than 0
                        if self.inventory["tools"][1][1] > 0:
                            # Light a fire using the lighter
                            self.light_fire(1)
                            # Set choosing_tool variable back to False
                            choosing_tool = False
                            # Take a turn away from the player
                            self.turns -= 1
                        else:
                            print(f'The {self.inventory["tools"][1][0]} stopped working!')

                    # Go back
                    case "3":
                        # Go back to choosing the action
                        choosing_tool = False
                        choosing_action = True

            # Do the following after every turn
            # Only if the player has completed their turn completely e.g. have eaten food
            if choosing_drink == False and choosing_food == False and choosing_action == False and choosing_tool == False:
                # Do the following after every turn
                # Increase danger, hydration, hunger, fatigue
                self.danger += 15
                self.hydration -= 10
                self.fatigue += 10
                self.hunger += 10

                # Reset all choosing variables
                choosing_action = True
                choosing_food = False
                choosing_drink = False

                # Display the players' current stats
                print("-------------------------------------------------------------------------------------------------")
                print(f"Hunger:{self.hunger}, Hydration:{self.hydration}, Fatigue:{self.fatigue}, Danger: {self.danger}, Turns remaining: {self.turns}")
                print("-------------------------------------------------------------------------------------------------")
    
        

player = Player(hunger = 0, hydration = 100, fatigue = 30)