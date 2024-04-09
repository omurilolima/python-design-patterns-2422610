import time

class Producer:
    """ Define the 'resource-intensive' object to instantiate! """
    def produce(self):
        print("Produces is working hard")

    def meet(self):
        print("Producer has time to meet you now!")
    
class Proxy:
    """ Define the 'relatively less resource-intensive' proxy to instanciate """
    def __init__(self):
        self.occupied = 'No'
        self.producer = None

    def produce(self):
        """ Check if Producer is avaiable """
        print("Artist checking if Producer is available")

        if self.occupied == 'No':
            # If the producer is available, create a producer object!
            self.producer = Producer()
            time.sleep(2)

            # Make the producer meet the guest!
            self.producer.meet()

        else:
            # Otherwise, don't instantiate a producer
            time.sleep(2)
            print("Producer is busy!")

# Instantiate a Proxy
p = Proxy()

# Make the proxy: Artist produce until Producer is avaiable
p.produce()

# Change the state to 'occypied'
p.occupied = 'Yes'

# Make the Producer produce
p.produce()