import numpy, random, cv2


class LCG():
    """ class for creating an LCG generator and assigning its values to an 2D array."""

    def LCG(multiplier: int = None, increment: int = None, first_value: int = None, modulus: int = 256) -> int:
        if first_value is None:
            first_value = random.randint(0, 256)
        if multiplier is None:
            multiplier = random.randint(0, 256)
        if increment is None:
            increment = random.randint(0, 256)
        
