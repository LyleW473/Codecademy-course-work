def movie_review(rating):
    if rating <= 5:
        return "Avoid at all costs!"
    elif rating < 9:
        return "This one was fun."
    else: 
        return "Outstanding!"

print(movie_review(7))