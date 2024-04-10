def count_to(count):
    """ Our iterator implementation """

    # Our list
    numbers_in_german = ["eins", "zwei", "drei", "vier", "funf"]

    # Our built-in iterator
    # creates a tuple suche as (1, "eins")
    iterator = zip(range(count), numbers_in_german)

    # Iterate through our iterable list
    # Extract the German numbers
    # Put them in a generator called number
    for position, number in iterator:

        # Return a "generator" containing numbers in German
        yield number


# Let's test the generator
for num in count_to(4):
    print(num)
