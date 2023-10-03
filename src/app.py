def example(number_a: int | float, number_b: int | float) -> float:
    """
    Args:
        number_a (int): First argument of addition
        number_b (int): Second argument of addition

    Returns:
        (int) Result of the sum a and b arguments
    Raises:
        TypeError: if one of parameters type doesn't match with integer or float types
    """
    if isinstance(number_a, (int, float)) and isinstance(number_b, (int, float)):
        result = float(number_a + number_b)
    else:
        raise TypeError("At least one type isn't integer or float, enter valid values to sum the arguments")
    return result
