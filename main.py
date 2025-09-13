import requests
from bs4 import BeautifulSoup
import json_read_catalog

class Vendr:
    def __init__(self,positions):
        self.products_url = [] # save products_url
        # create url element for work
        self.url_positions = []
        self.url_product = []
        for position in positions:
            position_text = position.replace(" ","-").lower()
            self.url_positions.append(f"https://www.vendr.com/categories/{position_text}")
        self.header = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
        }

    def main_directory(self):

        # try work with him( maybe need User agent
        # for start work only with
        # https://www.vendr.com/categories/devops
        self.open_categories()


        print(len(self.url_product))

    def open_categories(self):
        # for url_position in self.url_positions:
        url_position = "https://www.vendr.com/categories/devops"
        profetion_page = requests.get(url_position, headers = self.header)
        career_soup = BeautifulSoup(profetion_page.content, "lxml")

        # # I think It is don't auto text for avoid parsing data (rt-Text rt-r-size-2 rt-truncate)
        for parse_category in career_soup.find_all("h2"):
            if (parse_category.text == "Browse all categories") | (parse_category.text == "Categories in DevOps"):
                continue
            # print(parse_category.text)
            array_jrcts =json_read_catalog.json_read_cat("devops", parse_category.text)
            for array_jrct in array_jrcts:
                self.url_product.append(array_jrct)




if __name__ == "__main__":
    # we get work positions
    positions = ["DevOps", "IT Infrastructure", "Data Analytics and Management"]
    Vendr = Vendr(positions)
    # start work with url element
    Vendr.main_directory()