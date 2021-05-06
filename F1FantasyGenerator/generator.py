'''
@aurhor: Benjamin Pörhö, PTIVIS19H
filename: F1FantasyGenerator
Advanced Python Programming (5cr), miniproject.
This program is used to generate a team for you in F1 fantasy.
You are allowed to choose one F1 constructor and five F1 drivers.
Maximum budget is 100M and the program tells also the budget leftover.
Constructor and drivers collect points for you based on how they succeed.
You can make your own team at https://fantasy.formula1.com/team/create.
The prices what I have used are current (6.5.2021) fantasy prices.
Have fun!
'''

import random

class Generator:
    def __init__ (self, f1constructor, driver, engine, budget, leftover):
        self.f1constructor = f1constructor
        self.driver = driver
        self.budget = budget
        self.leftover = leftover
    
    def check (self)