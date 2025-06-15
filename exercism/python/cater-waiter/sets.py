"""Functions for compiling dishes and ingredients for a catering company."""


from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    """Remove duplicates from `dish_ingredients`.

    :param dish_name: str - containing the dish name.
    :param dish_ingredients: list - dish ingredients.
    :return: tuple - containing (dish_name, ingredient set).

    This function should return a `tuple` with the name of the dish as the first item,
    followed by the de-duped `set` of ingredients as the second item.
    """

    new_set = set(dish_ingredients)

    tupled_set = (dish_name, new_set)

    return tupled_set


def check_drinks(drink_name, drink_ingredients):
    """Append "Cocktail" (alcohol)  or "Mocktail" (no alcohol) to `drink_name`, based on `drink_ingredients`.

    :param drink_name: str - name of the drink.
    :param drink_ingredients: list - ingredients in the drink.
    :return: str - drink_name appended with "Mocktail" or "Cocktail".

    The function should return the name of the drink followed by "Mocktail" (non-alcoholic) and drink
    name followed by "Cocktail" (includes alcohol).

    """
    from sets_categories_data import ALCOHOLS

    ingredient_set = set(drink_ingredients)

    if ingredient_set.isdisjoint(ALCOHOLS):
        return drink_name + ' ' + 'Mocktail'
    else:
        return drink_name + ' ' + 'Cocktail'



def categorize_dish(dish_name, dish_ingredients):
    """Categorize `dish_name` based on `dish_ingredients`.

    :param dish_name: str - dish to be categorized.
    :param dish_ingredients: set - ingredients for the dish.
    :return: str - the dish name appended with ": <CATEGORY>".

    This function should return a string with the `dish name: <CATEGORY>` (which meal category the dish belongs to).
    `<CATEGORY>` can be any one of  (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).
    All dishes will "fit" into one of the categories imported from `sets_categories_data.py`

    """

    from sets_categories_data import VEGAN, VEGETARIAN, PALEO, KETO, OMNIVORE

    if dish_ingredients.issubset(VEGAN):
        return dish_name + ': ' + 'VEGAN'
    elif dish_ingredients.issubset(VEGETARIAN):
        return dish_name + ': ' + 'VEGETARIAN'
    elif dish_ingredients.issubset(PALEO):
        return dish_name + ': ' + 'PALEO'
    elif dish_ingredients.issubset(KETO):
        return dish_name + ': ' + 'KETO'
    else:
        return dish_name + ': ' + 'OMNIVORE'


def tag_special_ingredients(dish):
    """Compare `dish` ingredients to `SPECIAL_INGREDIENTS`.

    :param dish: tuple - of (dish name, list of dish ingredients).
    :return: tuple - containing (dish name, dish special ingredients).

    Return the dish name followed by the `set` of ingredients that require a special note on the dish description.
    For the purposes of this exercise, all allergens or special ingredients that need to be tracked are in the
    SPECIAL_INGREDIENTS constant imported from `sets_categories_data.py`.
    """

    from sets_categories_data import SPECIAL_INGREDIENTS
    ingredients = dish[1]
    dish_name = dish[0]
    ingredients_set = set(ingredients)

    ingredients_intersection = ingredients_set.intersection(SPECIAL_INGREDIENTS)
    return (dish_name, ingredients_intersection)


def compile_ingredients(dishes):
    """Create a master list of ingredients.

    :param dishes: list - of dish ingredient sets.
    :return: set - of ingredients compiled from `dishes`.

    This function should return a `set` of all ingredients from all listed dishes.
    """
    master_dish_set = set()

    for ingredients in dishes:
        master_dish_set = master_dish_set.union(ingredients)
    return master_dish_set


def separate_appetizers(dishes, appetizers):
    """Determine which `dishes` are designated `appetizers` and remove them.

    :param dishes: list - of dish names.
    :param appetizers: list - of appetizer names.
    :return: list - of dish names that do not appear on appetizer list.

    The function should return the list of dish names with appetizer names removed.
    Either list could contain duplicates and may require de-duping.
    """

    set_of_dishes = set(dishes)
    set_of_appetizers = set(appetizers)

    dish_set_without_appetizer = set_of_dishes.difference(set_of_appetizers)
    return list(dish_set_without_appetizer)


def singleton_ingredients(dishes, intersection):
    """Determine which `dishes` have a singleton ingredient (an ingredient that only appears once across dishes).

    :param dishes: list - of ingredient sets.
    :param intersection: constant - can be one of `<CATEGORY>_INTERSECTIONS` constants imported from `sets_categories_data.py`.
    :return: set - containing singleton ingredients.

    Each dish is represented by a `set` of its ingredients.

    Each `<CATEGORY>_INTERSECTIONS` is an `intersection` of all dishes in the category. `<CATEGORY>` can be any one of:
        (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).

    The function should return a `set` of ingredients that only appear in a single dish.
    """

    from sets_categories_data import example_dishes, EXAMPLE_INTERSECTION
    added_set = set()

    for dish in dishes:
        singleton_ingredients = dish.difference(intersection)
        added_set = added_set.union(singleton_ingredients)
    return added_set
