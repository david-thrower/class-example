class Beverage:
    """docstring for Beverage."""

    def __init__(self,
                 name: str,
                 color: str,
                 flavor: str):
        self.name = name
        self.color = color
        self.flavor = flavor

    def __str__(self):
        return str(self.__dict__)

    def print_summary(self):
        for k, v in self.__dict__.items():
            print(f"{k} is: {v}")
