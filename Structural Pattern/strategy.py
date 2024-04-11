import types 

class Strategy:
    """ The Strategy Pattern class """

    def __init__(self, function=None):
        self.name = "Default Strategy"

        # If a reference to a function is provided, replace the execute method
        if function:
            self.execute = types.MethodType(function, self)

    def execute(self):  # This gets replaced by another version if another function is provided
        """ The default method that prints the name of the strategy being called """
        print(f"{self.name} is used!")

# Replacement method 1
def strategy_one(self):
    print(f"{self.name} is used to execute method 1.")

# Replacement method 1
def strategy_two(self):
    print(f"{self.name} is used to execute method 2.")

# Lets's create our default strategy
s0 = Strategy()
# Lets's execute our default strategy
s0.execute()

# Lets's create the first variation of our default strategy by providing a function
s1 = Strategy(strategy_one)
# Let's set its name
s1.name = "Strategy One"
# Let's execute the strategy
s1.execute()

s2 = Strategy(strategy_two)
s2.name = "Strategy Two"
s2.execute()