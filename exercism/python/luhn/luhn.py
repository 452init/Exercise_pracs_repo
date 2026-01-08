class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        #splits the string and into individual characters
        string_num = "".join(self.card_num.split())

        #branch for checking validity of the string
        if len(string_num) < 2 or not string_num.isdigit():
            return False

        #Helper function for doubling odd number digits
        def luhn_double(digit):
            doubled = digit * 2
            return doubled - 9 if doubled > 9 else doubled

        #Generates all the digits in required order by luhn's algorithm, sums the
				#result and checks for mod 10 validity

				return sum(
						luhn_double(int(d)) if i % 2 else int(d)
						for i, d in enumerate(string_num[::-1])
						) % 10
