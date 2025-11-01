import requests
import pytesseract


class Board():
    def __init__(self):
        self.title = None
        self.pictures = None
        self.dims = None
        self.price = None
        self.description = None
        self.location = None
        self.contact = None

    def board_builder(self, details: dict) -> bool:
        """
        Function accepts dictionary. Returns False if the dict is empty
        otherwise it will fill out the class instance attributes and return
        True.
        """
        if not details:
            return False

        self.title = details['item']['name']
        self.pictures = details['item']['image']
        self.price = details['item']['offers']['price']
        self.description = details['item']['description']
        self.location = (
            details['item']['offers']['availableAtOrFrom']['geo']['latitude'],
            details['item']['offers']['availableAtOrFrom']['geo']['latitude'])

        return True

    def download_images(self) -> bool:
        """
        Downloads images and saves them
        """
        if not self.pictures:
            return False

        ocr_buf = []
        count = 0
        for image_url in self.pictures:
            image = requests.get(image_url)
            with open(f'images/image{count}.png', "wb") as pic:
                pic.write(image.content)
            data = pytesseract.image_to_string(f'images/image{count}.png')
            count += 1
            ocr_buf.append(data)
            print(ocr_buf)

        return True

    def to_dict(self) -> dict:
        """
        Returns a dictionary form of the object
        """
        board = {
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "location": self.location,
            "pictures": self.pictures,
            "dims": self.dims,
            "contact": self.contact,
        }
        return board
