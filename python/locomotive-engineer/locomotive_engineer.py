"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    wagon_list = [*args]
    return wagon_list


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    [a, b, c, *rest] = each_wagons_id
    *list_of_wagons, = c, *missing_wagons, *rest, a, b

    return list_of_wagons


def add_missing_stops(routing_dict , **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    my_value_list = []

    for value in kwargs.values():
        my_value_list.append(value)
    routing_dict['stops'] = my_value_list

    return routing_dict


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    extended_route_info = {**route, **more_route_information}

    return extended_route_info


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    list_of_rows = []

    *unpacked_rows, = zip(*wagons_rows)

    for item in unpacked_rows:
        list_of_rows.append(list(item))
    return list_of_rows
