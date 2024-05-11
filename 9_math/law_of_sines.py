import math

def law_of_sines(alpha=None, side_a=None, beta=None, side_b=None):

    args_provided = sum(arg is not None for arg in [alpha, side_a, beta, side_b])
    
    if args_provided != 3:
        raise ValueError("Exactly three arguments must be provided.")
    
    if any(val is not None and val <= 0 for val in [alpha, side_a, beta, side_b]):
        raise ValueError("Angles and sides must be positive non-zero values")

    if alpha is not None and (alpha <= 0 or alpha >= 180):
        raise ValueError("Angle alpha must be between 0 and 180 degrees")

    if beta is not None and (beta <= 0 or beta >= 180):
        raise ValueError("Angle beta must be between 0 and 180 degrees")
    
    if alpha is not None and beta is not None:
        gamma = 180 - alpha - beta
        if gamma <= 0:
            raise ValueError("Invalid triangle: Sum of angles must be less than 180 degrees")
    
    if alpha == None:
        alpha = math.degrees(math.asin(math.sin(math.radians(beta)) * (side_a / side_b)))

    elif beta == None:
        beta = math.degrees(math.asin(math.sin(math.radians(alpha)) * (side_b / side_a)))

    elif side_a == None:
        side_a = side_b * math.sin(math.radians(alpha)) / math.sin(math.radians(beta))

    elif side_b == None:
        side_b = side_a * math.sin(math.radians(beta)) / math.sin(math.radians(alpha))

    alpha = round(alpha, 2)
    beta = round(beta, 2)

    return alpha, side_a, beta, side_b
