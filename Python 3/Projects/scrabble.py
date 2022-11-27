letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {letter.lower():point for letter,point in zip(letters,points)}
print(letter_to_points)

letter_to_points[""] = 0
print(letter_to_points)

def score_word(word):
  point_total = 0
  for letter in word.lower():
    if letter not in letter_to_points:
      point_total += 0
    else:
      point_total += letter_to_points[letter]
  return point_total

brownie_points = score_word("BROWNIE")
testing_lower_points = score_word("moonlight")
print(f'"BROWNIE" = {brownie_points}')
print(f'"moonlight" = {testing_lower_points}')

player_to_words = {} 
player_to_words.update({"player1":["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]})

player_to_points = {}

# for player, words in (player_to_words.items()):
#     player_points = 0
#     for word in words:
#         player_points += score_word(word)
#     player_to_points[player] = player_points
# print(player_to_points)

player_to_points = {}
def update_point_totals():
    for player, words in (player_to_words.items()):
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points
    
    print(player_to_points)

def play_word(player, word):
    if player in player_to_words.keys():
        print(player)
        player_to_words[player].append(word)

        # Update the point totals
        update_point_totals()

play_word("player1", "HELLO")
play_word("Prof Reader", "MIDNIGHT")
play_word("Lexi Con", "ambidextrous")
print(player_to_words)