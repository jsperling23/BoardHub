import requests
import json
from bs4 import BeautifulSoup
from board import Board

# do something
if __name__ == "__main__":
    URL = "https://craigslist.org/search/sga?lat=37.495&lon=-122.268&query=\
           surfboard&search_distance=60#search=2~gallery~273"
    request = requests.get(URL)
    soup = BeautifulSoup(request.text, 'html.parser')
    raw_list = soup.find('script', id="ld_searchpage_results")
    if raw_list and raw_list.string:
        board_list = json.loads(raw_list.string)
        for board in board_list["itemListElement"]:
            listing = Board()
            listing.board_builder(board)
            print(listing.download_images())
            break
