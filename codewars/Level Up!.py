def xp_to_target_lvl(current_xp=None, target_lvl=None):
    result = []
    x = 314
    if type(current_xp) != int or type(target_lvl) != int:
        return "Input is invalid."

    if target_lvl <= 0 or target_lvl > 170 or current_xp < 0:
        return "Input is invalid."

    for level in range(2, target_lvl + 1):
        result.append(x)
        x = int(x * (1.25 if level < 10 else 1.25 - (level // 10 / 100)))

    return sum(result) - current_xp if (sum(
        result) - current_xp) > 0 else f'You have already reached level {target_lvl}.'


if __name__ == '__main__':
    print(xp_to_target_lvl(2, 3))
