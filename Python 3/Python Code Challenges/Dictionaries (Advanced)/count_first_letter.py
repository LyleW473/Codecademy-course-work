def count_first_letter(names):
    letters = {}
    
    for key in names.keys():
        if key[0] in letters:
            letters[key[0]] += len(names[key])
        else:
            letters[key[0]] = 0
            letters[key[0]] += len(names[key])
    return letters

print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))