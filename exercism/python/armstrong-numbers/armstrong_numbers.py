def is_armstrong_number(number):
    armstrong = 0
    list_of_nums = [int(num) for num in str(number)]
    length_of_list = len(list_of_nums)
    for n in list_of_nums:
        armstrong += (n ** length_of_list)
    if armstrong == number:
        return True
    else:
        return False
