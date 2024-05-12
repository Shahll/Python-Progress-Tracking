import math

def law_of_cosines(side_a=None, side_b=None, side_c=None, gamma=None):

    args_provided = sum(arg is not None for arg in [side_a, side_b, side_c, gamma])
    
    if args_provided != 3:
        raise ValueError("Exactly three arguments must be provided.")
    
    if any(val is not None and val <= 0 for val in [side_a, side_b, side_c, gamma]):
        raise ValueError("Angles and sides must be positive non-zero values")

    if gamma is not None and (gamma <= 0 or gamma >= 180):
        raise ValueError("Angle gamma must be between 0 and 180 degrees")
    
    if side_a == None:
        side_a = side_b * math.cos(math.radians(gamma)) + math.sqrt(side_c ** 2 - side_b ** 2 * math.sin(math.radians(gamma) ** 2))

    elif side_b == None:
        side_b = [round((side_a * math.cos(math.radians(gamma)) + modifier * math.sqrt(
            side_c ** 2 - side_a ** 2 * math.sin(math.radians(gamma)) ** 2)), 2)for modifier in [-1, 1]]

    elif side_c == None:
        side_c = math.sqrt(side_a ** 2 + side_b ** 2 - 2 * side_a * side_b * math.cos(math.radians(gamma)))

    elif gamma == None:
        gamma = math.degrees(math.acos((side_a ** 2 + side_b ** 2 - side_c ** 2) / (2 * side_a * side_b)))

    side_a = round(side_a, 2)
    side_c = round(side_c, 2)
    gamma = round(gamma, 2)

    return side_a, side_b, side_c, gamma
