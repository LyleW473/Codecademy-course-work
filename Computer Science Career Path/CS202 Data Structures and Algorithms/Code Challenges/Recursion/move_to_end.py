# define move_to_end() here
def move_to_end(input_list, item):
  result = []
  # If the length of the list is 0, return an empty list
  if len(input_list) == 0:
        return []
  else:
    # If the first item is the input item
    if input_list[0] == item:
        # Move the item to the end
        result += move_to_end(input_list[1:], item)
        # Add the item to the list
        result.append(input_list[0])
    # Otherwise
    else:
        # Move the item to the front of the list
        result.append(input_list[0])
        # Add everything else after
        result += move_to_end(input_list[1:], item)

    return result

gemstones = ["Amber", "Sapphire", "Amber", "Jade"]
print(move_to_end(gemstones, "Amber"))
print(move_to_end(gemstones, "Sapphire"))