import random

name = "Lyle"
question = "Is the Earth flat?"
answer = ""
random_number = random.randint(1, 11)
print(random_number)

if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful."
elif random_number == 10:
  answer = "Definitely not."
elif random_number == 11:
  answer = "Nope."
else: 
  answer = "Error"

if len(question) == 0:
    print("Enter a question")
else:
    if len(name) == 0:
        print("Question:", question)
    else:
        print(f'{name} asks: {question}')

    print(f"Magic 8-Ball's answer: {answer}")
