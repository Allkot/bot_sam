import random

def pas_gen(password_lengh):
    password = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password_gen = ""

    for symbol in range(password_lengh):
        password_gen += random.choice(password)
    return password_gen