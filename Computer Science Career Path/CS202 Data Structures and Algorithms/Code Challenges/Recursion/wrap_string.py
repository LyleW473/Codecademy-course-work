# define wrap_string() here
def wrap_string(string, n):
    result = ""
    # If n is less than or equal to 0
    if n <= 0:
        # Return the string
        return string
    else:
        # Concatenate "<" to the front of the string
        result += "<"

        # Concatenate the string into the middle
        result += wrap_string(string, n - 1)

        # Concatenate ">" to the end of the string
        result += ">"

    # Return the wrapped string
    return result

wrapped = wrap_string("Pearl", 3)
print(wrapped)