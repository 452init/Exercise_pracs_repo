"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """

    letters = ["A", "B", "C", "D"]
    for n in range(number):
        index = n % 4
        yield letters[index]

def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    seat_list = []
    row  = 1
    total_seat_generated = 0

    letters = ["A", "B", "C", "D"]
    
    while total_seat_generated < number:
        if row == 13:
            row += 1
            continue
        for letter in letters:
            if total_seat_generated >= number:
                break
            yield f"{row}{letter}"
            total_seat_generated += 1
        row += 1

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    seat = generate_seats(len(passengers))
    seat_assignments = dict(zip(passengers, seat))
    return seat_assignments

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for seat in seat_numbers:
        tickets_without_zero_code = len(seat) + len(flight_id)
        if tickets_without_zero_code < 12:
            zero_codes = "0" * (12 - tickets_without_zero_code)
            ticket_code = seat + flight_id + zero_codes
            yield ticket_code
