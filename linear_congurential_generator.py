import numpy, random, cv2


class LCG():
    """ class for creating an LCG generator and assigning its values to an 2D array."""

    @staticmethod
    def LCG(multiplier: int = None, increment: int = None, first_value: int = None, modulus: int = 256) -> int:
        if first_value is None:
            first_value = random.randint(0, 256)
        if multiplier is None:
            multiplier = random.randint(0, 256)
        if increment is None:
            increment = random.randint(0, 256)
        next_value = (multiplier * first_value + increment) % modulus
        return next_value


    
    
ra = numpy.zeros((512,512), numpy.uint8)
lcg = LCG()

with numpy.nditer(ra, op_flags = ["readwrite"]) as rai:
    first_value = random.randint(0, 256)
    rai[0][...] = first_value
    rai.iternext()
    for i in range(512*512):
        rai[0][...] = lcg.LCG(first_value = first_value)
        rai.iternext()
        
cv2.imshow("randomly generated image using LCG", ra)
cv2.waitKey(0)
cv2.destroyAllWindows()
