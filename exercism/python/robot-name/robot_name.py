import random
import string

class Robot:
    def __init__(self):
        self.name = self.random_name()

    def random_name(self):
        my_string = string.ascii_uppercase
        rand_nums = random.randrange(100, 999)
        rand_letters = ''.join(random.choices(my_string, k=2))
        return rand_letters+str(rand_nums)

    def reset(self):
        old_name = self.random_name()
        while old_name == self.name:
            self.name = self.random_name()
        return self.name
