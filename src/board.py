class Board():
    def __init__(self):
        self.title = None
        self.pictures = None
        self.dims = None
        self.price = None
        self.description = None
        self.contact = None

    def board_builder(self, details: dict) -> bool:
        """
        Function accepts dictionary. Returns False if the list is empty
        otherwise it will fill out the class instance attributes and return
        True.
        """
        if not details:
            return False

        for key, value in details.items():
            pass

        return True
