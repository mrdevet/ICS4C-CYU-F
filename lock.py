class Lock:
    '''
    A Lock respresents a combination lock on a locker.

    Arguments:
     * num_1 - The first number in the combination
     * num_2 - The second number in the combination
     * num_3 - The third number in the combination
    '''
    
    def __init__ (self, num_1, num_2, num_3):
        '''
        Create a lock and set its combination.
        '''
        # Check and set the combination numbers
        if not isinstance(num_1, int) or not isinstance(num_2, int) or not isinstance(num_3, int):
            raise TypeError("The combination numbers must be integers!")
        if min(num_1, num_2, num_3) < 1 or max(num_1, num_2, num_3) > 60:
            raise ValueError("The combination numbers must be between 1 and 60!")
        self.num_1 = num_1
        self.num_2 = num_2
        self.num_3 = num_3

        # Start the lock as locked
        self.locked = True


    def __str__ (self):
        '''
        Represent the lock as a string.
        '''
        # Get a string representation of the combination
        combo = f"{self.num_1}-{self.num_2}-{self.num_3}"

        # Get a string representation of the state
        if self.locked:
            state = "locked"
        else:
            state = "unlocked"

        # Return these together
        return f"Lock({combo}, {state})"


    ### METHODS - put your code down here

    
