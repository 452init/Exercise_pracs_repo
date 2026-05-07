import random
import string

class Robot:
    used_names = []

    def __init__(self):
        self.name = self._generate_unique_name()

    def random_name(self):
        letters = ''.join(random.choices(string.ascii_uppercase, k=2))
        numbers = f"{random.randrange(0, 1000):03d}"
        return letters + numbers

    def reset(self):
        self.name = self._generate_unique_name()
        return self.name

    def _generate_unique_name(self):
        new_name = self.random_name()
        while new_name in Robot.used_names:
            new_name = self.random_name()
        Robot.used_names.append(new_name)
        return new_name
