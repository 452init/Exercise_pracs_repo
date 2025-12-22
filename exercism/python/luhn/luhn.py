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

            for i in range(1, len(integer_list), 2): #doubls the required values in the list
                integer_list[i] *= 2

            #splits all the values in the list

            result = []
            for doubled in integer_list:
                if doubled > 9:
                    doubled -=9
                    result.append(doubled)
                else:
                    result.append(doubled)

            #sums the result and checks for mod 10 validity
            return sum(result) % 10 == 0
