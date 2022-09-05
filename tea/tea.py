from beverage.beverage import Beverage

# Inherts Beverage, becomes a Beverage plus whatever else you add to it


class Tea(Beverage):  # (Beverage) means it inherets from (is a) Beverage
    """Class Tes:

    Params:
        name: str: the name of the drink,
        color: str: what color the drink is,
        flavor: str: describe the flavor of the drink
    """

    def __init__(self,
                 tannin_content_percent: float,
                 name: str,
                 color: str,
                 flavor: str):

        super().__init__(name, color, flavor)
        # This you always do when you create a class that inherets from
        # another class. It is an instructio that tells Python: ""When
        # a userr creates an instance of the class Tea, start by creating an
        # instance of the class Beverage, then create add to it everything
        # below here
        self.tannin_content_percent = tannin_content_percent
