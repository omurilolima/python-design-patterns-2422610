class House(object):
    # The class being visited
    def accept(self, visitor):
        """ Interface to accept a visitor """
        visitor.visit(self)  # Triggers the visiting operation!

    def work_on_hvac(self, hvac_specialist):
        # Note that we now have a reference to the hvac especialist object
        print(self, "worked on by", hvac_specialist)

    def work_on_electricity(self, eletrician):
        # Note that we now have a reference to the electrician object
        print(self, "worked on by", eletrician)

    def __str__(self):
        """ Return the class name when the House object is printed """
        return self.__class__.__name__

class Visitor(object):
    """ Abstract visitor """
    def __str__(self):
        """ Retirm the class name when the Visitor object is printed """
        return self.__class__.__name__

class HvacSpecialist(Visitor):  # Inherits from the parent class, Visitor
    """ Concrete visitor: HVAC specialist """
    def visit(self, house):
        house.work_on_hvac(self)   # Note that the visitor now has a reference to the house object.

class Electrician(Visitor):   # Inherits from the parent class, Visitor
    """ Concrete visitor: electrician """
    def visit(self, house):
        house.work_on_electricity(self)  # Note that the visitor now has a reference to the house object

# Create an HVAC specialist
hv = HvacSpecialist()
# Create an electrician
e = Electrician()
# Create a house
home = House()
# Let the house accept the HVAC specialist and work on the house by invoking the accept method
home.accept(hv)
# Let the house accept the electrician specialist and work on the house by invoking the accept method
home.accept(e)