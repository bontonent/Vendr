import requests
from bs4 import BeautifulSoup

class Vendr:
    def __init__(self,positions):
        # create url element for work
        self.url_positions = []
        for position in positions:
            position_text = position.replace(" ","-").lower()
            self.url_positions.append(f"https://www.vendr.com/categories/{position_text}")

    def main_directory(self):
        # try work with him( maybe need User agent
        # for start work only with
        # https://www.vendr.com/categories/devops
        url = "https://www.vendr.com/categories/devops"
        print("work")

        page = requests.get(url)
        page_soup = BeautifulSoup(page.content, "lxml")

        for titles in page_soup.find_all("h1"):
            print(titles.text)






if __name__ == "__main__":
    # we get work positions
    positions = ["DevOps", "IT Infrastructure", "Data Analytics and Management"]
    Vendr = Vendr(positions)
    # start work with url element
    Vendr.main_directory()