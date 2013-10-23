"""Module for clouds, such as those imparting food or representing poison.

Clouds are basic objects in the creatures' world providing some form of field of
effect.

Each cloud type may define:
    DEFAULT_SIZE - The starting size of the cloud
    MIN_SIZE     - The smallest possible size of the cloud before being removed
    SHADE        - Colour of the cloud; given as a RGB tuple
    IMPACT_RATE  - Multiplicative impact wrt food when absorbed or eaten
"""

class Cloud:
    """Base class for cloud objects."""
    DEFAULT_SIZE = 40
    MIN_SIZE = 20
    IMPACT_RATE = 1
    SHADE = (200, 100, 100)

    def __init__(self, x, y, size=None):
        """Setup a new cloud object."""
        if not size:
            size = self.DEFAULT_SIZE
        self.x = x
        self.y = y
        self.size = size

    def contains(self, x, y):
        """Determine if a location conflicts with the posion does."""
        if (x - self.x)**2 + (y - self.y)**2 < self.size**2:
            return True
        return False

class Food(Cloud):
    """Class for basic food for the creatures. Yum."""
    pass

class Poison(Cloud):
    """Class for poison doses.

    These objects are deprecating to creatures, causing them to become more
    hungry.  They are the anti-food.
    """
    DEFAULT_SIZE = 25
    MIN_SIZE = 15
    IMPACT_RATE = -1
    SHADE = (100, 200, 100)

