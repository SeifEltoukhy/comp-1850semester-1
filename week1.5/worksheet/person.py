# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self,name,birth):
        if not isinstance(name,str):
            raise TypeError("name should be a string")
        if name == "":
            raise ValueError("name cannot be empty")
        if not isinstance(birth, date):
            raise TypeError("birth should be a date")
        self.name=self
        self.birth=birth
    def initials(self):
        """Returns the initials of the person's name."""
        parts = self.name.split()
        initials = ""
        for part in parts:
            initials += part[0].upper()
        return initials
    
    def is_birthday(self):
        """Returns True if today is the person's birthday."""
        today = date.today()

        if self.birth.month == today.month and self.birth.day == today.day:
            return True
        else:
            return False


    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
