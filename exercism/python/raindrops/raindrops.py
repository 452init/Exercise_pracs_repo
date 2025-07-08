def convert(number):
    final_result = ""
    if number % 3 == 0:
        final_result += "Pling"
    if number % 5 == 0:
        final_result += "Plang"
    if number % 7 == 0:
        final_result += "Plong"
    if final_result == "":
        return str(number)
    return final_result
