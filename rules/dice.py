import random

def roll_dice(notation: str) -> int:
    parts = notation.lower().replace(" ", "").split("d")
    num = int(parts[0]) if parts[0] else 1
    if '+' in parts[1]:
        sides, mod = map(int, parts[1].split('+'))
    elif '-' in parts[1]:
        sides, mod = parts[1].split('-')
        mod = -int(mod)
        sides = int(sides)
    else:
        sides = int(parts[1])
        mod = 0

    rolls = [random.randint(1, sides) for _ in range(num)]
    return sum(rolls) + mod
