
def power(x: float, y: int) -> float:
    result = 1.0
    power = y

    # tweek for the algorithm work with negative power
    if y < 0:
        power, x = -power, 1.0 / x

    # if power < 0 evaluates False
    # that happens when bits shift down to 0 or less
    while power:
        # evaluates if power is odd
        if power & 1:
            # If odd, multiply per x to not loose that factor in interger division
            result *= x
        # right bit shift -> divides by 2
        power = power >> 1
        # Accumulate power
        x = x * x
    return result   

print(power(2, -13))