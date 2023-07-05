from threading import RLock

class Globpi:

    def __init__(self, steps):
        """
        Initializes an instance of the Globpi class.

        Args:
            steps (int): The number of steps used for calculating pi.

        Returns:
            None
        """
        self.lock = RLock()
        self.steps = steps
        self.globPi = 0.0

    def addToglobPi(self, threadPi):
        """
        Adds the calculated value of pi from a thread to the global pi value.

        Args:
            threadPi (float): The calculated value of pi from a thread.

        Returns:
            None
        """
        with self.lock:
            self.globPi += threadPi

    def printPi(self):
        """
        Prints the value of pi.

        Returns:
            None
        """
        print("pi is " + str(self.globPi))

    def get_steps(self):
        """
        Returns the number of steps used for calculating pi.

        Returns:
            str: The number of steps as a string.
        """
        return str(self.steps)
