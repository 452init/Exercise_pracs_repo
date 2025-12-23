class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        #splits the string and into individual characters
        string_num = "".join(self.card_num.split())

        #branch for checking validity of the string
        if len(string_num) < 2 or not string_num.isdigit():
            return False
        else:
            #changes the strings to ints and reverse the list
            integer_list = [int(i) for i in string_num]
            integer_list = list(reversed(integer_list))

            #enumerates the integer_list then doubles the required values in the list and subtracts 9 if the doubled num is greater than 9
            result = [((num * 2) - 9 if num * 2 > 9 else (num * 2)) if idx % 2 !=0 else num for idx, num in enumerate(integer_list)]

            #sums the result and checks for mod 10 validity
            return sum(result) % 10 == 0
