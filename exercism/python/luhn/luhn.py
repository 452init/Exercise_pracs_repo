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

            i = 1
            while i < len(integer_list): #doubls the required values in the list
                integer_list[i] *= 2
                i += 2

            #splits all the values in the list
            result = [int(num) for num in "".join([str(n) for n in integer_list])]

            #sums the result and checks for mod 10 validity
            if sum(result) % 10 == 0:
                return True
            else:
                return False
