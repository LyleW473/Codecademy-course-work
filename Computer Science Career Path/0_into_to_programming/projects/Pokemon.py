class Trainer:
    def __init__(self):
        self.pokemon_collection = self.create_pokemons() # Collection of Pokemon objects
        self.pokemon_names = [pokemon.name for pokemon in self.pokemon_collection] # Collection of the Pokemons' names
        print(f"You have the following pokemons: {self.pokemon_names}")

    def create_pokemons(self):
        # Create pokemon instances
        pikachu = Pokemon("Pikachu", 100, 20, 60, 15)
        charizard = Pokemon("Charizard", 250, 40, 100, 50)  
        mewtwo = Pokemon("Mewtwo", 175, 30, 80, 10)

        # Return the objects as a list
        return [pikachu, charizard, mewtwo]

    def increase_pokemon_health(self, pokemon):
        # Increase the pokemon's health
        pokemon.increase_health()

    def initiate_fight(self, pokemon1_index, pokemon2_index):
        # Variables to switch between the player's pokemon and the AI pokemon
        pokemon1_turn = True
        pokemon2_turn = False   

        # Select the pokemon's that are fighting based on the index passed in
        pokemon1 = self.pokemon_collection[pokemon1_index]
        pokemon2 = self.pokemon_collection[pokemon2_index]

        # Make temp variable holding the original health of the enemy pokemon
        pokemon2_original_health = pokemon2.health

        print(f"Fight started between {pokemon1.name} and {pokemon2.name}")


        # Fight loop
        while True:
            # If the player's pokemon has 0 health or less, the AI has won
            if pokemon1.health <= 0:
                print(f"{pokemon2.name} has won!")
                break
            elif pokemon2.health <= 0:
                print(f"{pokemon1.name} has won!")
                break

            # Display the pokemon's stats
            print(f"{pokemon1.name}: Health = {pokemon1.health}, Energy = {pokemon1.energy}, Attack Power = {pokemon1.attack_power}, Energy Drain = {pokemon1.energy_drain}")
            print(f"{pokemon2.name}: Health = {pokemon2.health}, Energy = {pokemon2.energy}, Attack Power = {pokemon2.attack_power}, Energy Drain = {pokemon2.energy_drain}")

            # Player's turn
            if pokemon1_turn == True:
                print(f"{pokemon1.name}'s turn!")

                # Get input
                action = input("Choose an action: Attack, Rest, HealthPotion ")

                # If the action isn't given, then keep asking for input
                while action not in ["Attack", "Rest", "HealthPotion"]:
                    print("Invalid input, please re-enter your answer")
                    action = input("Choose an action: Attack, Rest, HealthPotion")

                # Do an action based on the user input
                match action:

                    case "Attack":
                        # Player's pokemon should attack the enemy pokemon
                        pokemon1.attack(pokemon2)

                    case "Rest":
                        # Pokemon rests, gaining HP and energy
                        pokemon1.rest()

                    case "HealthPotion":
                        # Heath potion has been used on the pokemon
                        pokemon1.increase_health()

                # Set the turn to be the AI's turn
                pokemon2_turn = True

            # AI's turn
            if pokemon2_turn == True:
                print(f"{pokemon2.name}'s turn!")
                
                # If the AI pokemon has lost more than half of its health and their rage ability hasn't been activated already
                if pokemon2.health <= (pokemon2_original_health // 2) and pokemon2.rage_activated == False:
                    # Use rage ability
                    pokemon2.rage()
                    # Set the pokemon's rage ability as activated
                    pokemon2.rage_activated = True

                # Otherwise just keep attacking normally
                else:
                    pokemon2.attack(pokemon1)

                # Set the turn to be the player's turn
                pokemon1_turn = True



class Pokemon:
    def __init__(self, name, health, attack_power, energy, energy_drain, rage_activated = False):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.energy = energy
        self.energy_drain = energy_drain
        self.rage_activated = rage_activated 

    def __repr__(self):
        print(self.name)
        
    def attack(self, target):
        # If the energy is greater the pokemon's energy drain
        if self.energy >= self.energy_drain:
            # Reduce the target's HP
            target.health -= self.attack_power
            print(f"{target.name} has lost {self.attack_power} health!")
            # Reduce the current pokemon's energy
            self.energy -= self.energy_drain
        else:
            print(f"{self.name} insufficient energy to attack! {self.name} will rest!")
            # Call the rest method
            self.rest()
        
    def increase_health(self):
        # Increase HP
        self.health += 50
        print(f"{self.name} has gained 30 health!")

    def rest(self):
        # Increase energy
        self.energy += 30
        # Increase HP slightly
        self.health += 15

        print(f"{self.name} has rested and has gained 30 energy and 15 health!")

    def rage(self):
        self.attack_power += 15
        self.health += 20
        print(f"{self.name} is furious! {self.name} has gained 20 health and now does {self.attack_power} damage!")
    
my_trainer = Trainer()
my_trainer.initiate_fight(0, 2)
