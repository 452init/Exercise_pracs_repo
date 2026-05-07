def proverb(*args, qualifier=None) -> list[str]:

    result: list = []

    if not args:
        return  result
    result = [f"For want of a {current} the {next_item} was lost." for current, next_item in zip(args, args[1:])]

    items = args[0] if qualifier is None else f"{qualifier} {args[0]}"

    result.append(f"And all for the want of a {items}.")

    return result