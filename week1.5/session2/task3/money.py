# Week 1.5, Session 2: Task 3

class Money:
    """
    An amount of money, in British Pounds Sterling.
    """

    def __init__(self, pounds, pence):
        """
        Creates a Money object, given the number of pounds and pence.
        """
        if not isinstance(pounds,int):
            raise TypeError("pounds cant be negative ")
        if pounds < 0:
            raise ValueError("value must be graeter than zero")
        self.pounds = pounds
        self.pence = pence

    def __str__(self):
        """
        Returns a string representation of this Money.
        """
        # Add code here to return an appropriate string representation
        # Use the currency symbol for British Pounds Sterling
        # Represent pence with a leading zero if needed (e.g. '05')

    def __add__(self, other):
        """
        Adds this Money to another Money, returning the total.
        """
        # Add code here to check that parameter 'other' is a Money object,
        # add self to other, then return the sum as a new Money object
        # (see README for hints and tips)
        if not isinstance(other,Money):
            raise TypeError("not money pbject")

        Sum_pounds = self.pounds+other.pounds
        extrapound=(self.pence+other.pence)//100
        sumpence=(self.pence+other.pence)%100

        return Money(Sum_pounds)
