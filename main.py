import random

# Initialise variables
response = {"lose": ["I am afraid not. Please try again.","That is a good password but not my password. Keep going.","That is not my password. It's really easy to guess my password."],
"win": "Well done! You must work for MI6. Give my regards to James Bond."}
my_password = "my_password"

def is_correct(guess,password):
    if guess == password:
        return True
    else:
        return False