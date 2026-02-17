from itertools import zip_longest, chain


def transpose(text) -> str:
    lines = text.splitlines()

    max_len = 0
    padded_lines = []
    for line in reversed(lines):
        max_len = max(max_len, len(line))

        padded_lines.append(chain(line))

    lines = list(reversed(padded_lines))
    transposed = zip_longest(*lines, fillvalue='')

    return '\n'.join(''.join(row) for row in transposed)
