# class-example
A demo example for classes

## Recommendations and best practices:

0. Strong recommendation: install Atom on your computer and install python-ide (open source tool similar to Pycharm with Kite, alternatively, PyCharm with Kite).
1. Start a main file in the root directory of your project (main.py): Arranged in the order: 1. imports 2. GLOBALS 3. class instantiations 4. functional description fo the task as a function, 5. the task function called nested in if __name__ == "__main__":
2. Create a parent class and package it: 1. create a folder in your project named beverage 2. Create an empty file named  __init__.py (that let's Python know you want Python to treat the contents of this folder as a module. It will compile the contents in .pyc so it runs much faster). Create a file named beverage.py (a Python module), then create a class named Beverage on this module. This becomes like a form for describing a drink, with some functions or **class methods** that perform operations on itself.
3. Create a child class: Tea that inherets from Beverage (done as an example). This means that Tea is a Beverage (plus whatever else you added to it)
4. Create a child class: Green Tea that inherets the class Tea (This is an exercise to take a shot at)
5. Now run main.py.
