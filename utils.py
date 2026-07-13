import random

def generate_secure_token(token_length):
    character_pool = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
    return "".join(random.choices(character_pool, k=token_length))