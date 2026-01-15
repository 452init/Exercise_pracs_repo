import string

class PhoneNumber:
    def __init__(self, number):
        self.number = number
        
        self.result = ''.join(num for num in self.number if num.isdigit())
            
        if any(n.isalpha() for n in self.number):
            raise ValueError("letters not permitted")
        if len(self.number) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(self.result) > 11:
            raise ValueError("must not be greater than 11 digits")
        if self.result[0] != '1' and len(self.result) > 10:
            raise ValueError("11 digits must start with 1")
        if self.result[3] == '0' or len(self.result) == 11 and self.result[4] == '0':
            raise ValueError("exchange code cannot start with zero")
        if self.result[3] == '1' or len(self.result) == 11 and self.result[4] == '1':
            raise ValueError("exchange code cannot start with one")
        if self.result[0] == '0' or len(self.result) == 11 and self.result[1] == '0':
            raise ValueError("area code cannot start with zero")
        if self.result[0] == '1' or len(self.result) == 11 and self.result[1] == '1':
            raise ValueError("area code cannot start with one")
        if any(l in string.punctuation for l in self.number):
            raise ValueError("punctuations not permitted")
        if len(self.result) == 11 and self.result[0] == '1':
            self.cleaned = self.result[1:]
        if len(self.result) == 10:
            self.cleaned = self.result
