def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if ((a == b and b == c) and (a != 0)):
        return True
    else:
        return False


def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if ((a == b or a == c or b == c) and (a + b > c and a + c > b and b + c > a)):
        return True
    else:
        return False


def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if ((a == b or b == c or c == a) or (a + b < c or a + c < b or b + c < a)):
        return False
    else:
        return True
