import random


def random_port():
    return random.randint(20000, 30000)


LOCALHOST = "localhost"
QUEUE = 10

ADDRESS = (LOCALHOST, random_port())
