import requests
from bs4 import BeautifulSoup

class Vendr:
    def __init__(self,positions):
        self.products_url = [] # save products_url
        # create url element for work
        self.url_positions = []
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
        # print(len(self.products_url))

    def open_categories(self):
        # for url_position in self.url_positions:
        url_position = "https://www.vendr.com/categories/devops"
        profetion_page = requests.get(url_position, headers = self.header)
        career_soup = BeautifulSoup(profetion_page.content, "lxml")

        # # I think It is don't auto text for avoid parsing data (rt-Text rt-r-size-2 rt-truncate)
        for parse_category in career_soup.find_all("h2"):
            if parse_category.text == "Browse all categories":
                continue
            code_category_url = parse_category.text.replace("(","").replace(")","").replace("/","-").replace(" ","-").lower()
            # create url to category
            categories_url = f"https://www.vendr.com/categories/{code_category_url}?page=1"
            self.get_element_catalog(categories_url)

    def get_element_catalog(self, url_category):
        catalog_page = requests.get(url_category, headers=self.header)
        catalog_soup = BeautifulSoup(catalog_page.content, "lxml")
        for element_catalog in catalog_soup.find_all("a",class_="_card_gl3kq_9 _card_1u7u9_1 _cardLink_1q928_1"):
            print(element_catalog.get("href"))






if __name__ == "__main__":
    # we get work positions
    positions = ["DevOps", "IT Infrastructure", "Data Analytics and Management"]
    Vendr = Vendr(positions)
    # start work with url element
    Vendr.main_directory()