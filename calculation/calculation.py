"""This is our calculation base class / Abstract Class"""


class Calculation:
    """ Calculation Class """
    # Default Constructor
    def __init__(self, value_a, value_b):
        """Initialize the values"""
        self.value_a = value_a
        self.value_b = value_b
