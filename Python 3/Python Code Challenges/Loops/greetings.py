def add_greetings(names):
    strings = []
    for name in names:
        strings.append("Hello, " + name)
    return strings

print(add_greetings(["Owen", "Max", "Sophie"]))