from globPi import Globpi

class MasterProtocol:

    def __init__(self, piObject: Globpi, id: int):
        """
        Initializes an instance of the MasterProtocol class.
        Args:
            piObject (Globpi): An instance of the Globpi class representing the global pi object.
            id (int): The ID of the worker.
        Returns:
            None
        """
        self.piObject = piObject  # an instance of the class Globpi
        self.id = id

    def prepare_request(self):
        """
        Prepares the request to be sent to the worker.
        Returns:
            str: The prepared request containing the steps and worker ID.
        """
        return self.piObject.get_steps() + ' ' + str(self.id)  # master (server) will send steps and worker ID to each worker

    def process_reply(self, the_input):
        """
        Processes the reply received from a worker.
        """
        _partialPi = float(the_input)
        self.piObject.addToglobPi(_partialPi)
