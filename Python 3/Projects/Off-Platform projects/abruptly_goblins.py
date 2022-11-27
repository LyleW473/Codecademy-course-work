gamers = []

def add_gamer(gamer, gamers_list):
    # Check if the keys "name" and "availability" exist in the gamer dictionary.
    if "name" and "availability" in gamer.keys():
        # Append the gamer to the list passed into the function
        gamers_list.append(gamer)

kimberly = {"name": "Kimberly Warner", "availability": ["Monday", "Tuesday", "Friday"]}
add_gamer(kimberly, gamers)

# Adding more gamers
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

print(gamers)

def build_daily_frequency_table():
    dictionary = {}
    days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    # Return a dictionary with the days as the keys, with the default values all being 0.
    return dictionary.fromkeys(days, 0)

count_availability = build_daily_frequency_table()
print(count_availability)

def calculate_availability(gamers_list, available_frequency):
    # Iterate through all gamers inside the gamers list
    for gamer in gamers_list:
        # For every day that the gamer is available
        for day in gamer["availability"]:
            #print(gamer["name"], day)
            # Increase the frequency of that day in the available frequency list.
            available_frequency[day] += 1

calculate_availability(gamers, count_availability)
print(count_availability)

def find_best_night(availability_table):
    # First attempt

    # highest_count = 0
    # # Iterate through the values inside the availability table
    # for value in availability_table.values():
    #     # Find the highest value, replacing the old "highest count" if it is greater.
    #     if value > highest_count:
    #         highest_count = value

    # # Iterate through keys inside of the availability table
    # for key in availability_table:
    #     # If the key's value is equal to the highest count
    #     if availability_table.get(key) == highest_count:
    #         print(key)

    # Second attempt

    best_night = [0,0]
    # Iterate through the keys and values of the availability table simultaneously
    day_value_table = zip(availability_table.keys(), availability_table.values())
    # For each day,value in the table
    for day, value in day_value_table:
        # If the value is better than the value from the previous night
        if value > best_night[1]:
            # Set the best night's value as the current value
            best_night[1] = value 
            # Set the best night (the day) as the current day
            best_night[0] = day 

    print(f' The best night is {best_night[0]} with a count of {best_night[1]}')
    return best_night[0]

game_night = find_best_night(count_availability)
print(game_night)

def available_on_night(gamers_list, best_day):
    attending_gamers = []
    unable_to_attend_gamers = [] 
    # Iterate through the gamers list
    for gamer in gamers_list:
        # Iterate through the list of days that the gamer is available
        for day in gamer["availability"]:
            # If one of the days they are available on includes the best day
            if day == best_day:
                # Append them to the attending gamers list
                attending_gamers.append(gamer["name"])
    
        # Check if the gamer is not in the attending gamers list, this means they are unable to attend
        if gamer["name"] not in attending_gamers:
            # So append them to the unable to attend list. 
            # Note: This time I appended the entire dictionary because we are arranging a second night, the calculate_availability function looks for a gamers["availability"]
            unable_to_attend_gamers.append(gamer)

    return attending_gamers, unable_to_attend_gamers

attending_game_night, unable_to_attend_best_night = available_on_night(gamers, "Thursday")
print(f' The gamers attending game night are: {attending_game_night}')
print(f'The gamers unable to attend game night are: {unable_to_attend_best_night}')

# Generating an E-mail for the participants
def send_email(gamers_who_can_attend, day, game):
    # Iterate through the gamers who can attend this game night
    for gamer in gamers_who_can_attend:
        # If the gamer type is a string, this means that they were are scheduled for the first game night
        if type(gamer) == str:
            form_email = "{gamer}, you have been invited to play {game} on {day}".format(gamer = gamer, game = game, day = day)
            print(form_email)
        # If the gamer type is a dictionary, this means that they were scheduled for the second game night
        elif type(gamer) == dict:
            form_email = "{gamer}, you have been invited to play {game} on {day}".format(gamer = gamer["name"], game = game, day = day) # Change the gamer to be the name of the gamer
            print(form_email)           
        
send_email(attending_game_night, game_night, "Abruptly Goblins!")
    
# Second night
second_night_availability = build_daily_frequency_table()
calculate_availability(unable_to_attend_best_night, second_night_availability)
second_night = find_best_night(second_night_availability)
available_second_game_night = available_on_night(gamers, second_night)[1] # Note: Set available_second_game_night as the 2nd return value from available_on_night
send_email(available_second_game_night, second_night, "Abruptly Goblins!")