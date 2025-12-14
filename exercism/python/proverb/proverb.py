def proverb(*args, qualifier=None) -> list:
    result = []
    length = len(args)

    if not length:
        return result
    elif length == 1 and qualifier:
        result.append(f"And all for the want of a {qualifier} {args[0]}.")
    elif length == 1:
        result.append(f"And all for the want of a {args[0]}.")
    else:
        for value in range(length-1):
            result.append(f"For want of a {args[value]} the {args[value+1]} was lost.")
        if not qualifier:
            result.append(f"And all for the want of a {args[0]}.")
        else:
            result.append(f"And all for the want of a {qualifier} {args[0]}.")
    return result
