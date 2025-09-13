import requests
from bs4 import BeautifulSoup
import json_read_catalog

class Vendr:
    def __init__(self,positions):
        self.products_url = [] # save products_url
        # create url element for work
        self.url_positions = []
        self.url_products = []
        for position in positions:
            position_text = position.replace(" ","-").lower()
            self.url_positions.append(f"https://www.vendr.com/categories/{position_text}")
        self.header = {
            "user-agent": "Mozilla/5.0 (Linux i551 x86_64) AppleWebKit/535.17 (KHTML, like Gecko) Chrome/49.0.1341.243 Safari/601"
        }

    def main_directory(self):

        # try work with him( maybe need User agent
        #self.open_categories()


        #print(len(self.url_products))
        # https://www.vendr.com/marketplace/scorebuddy
        url_product = "https://www.vendr.com/marketplace/scorebuddy"
        self.get_data(url_product)

    def get_data(self,url_product):
        product_page = requests.get(url_product, headers=self.header)
        soup_product = BeautifulSoup(product_page.content, "lxml")

        for query_name in soup_product.find_all("h1"):
            name_company = query_name.text
            print(name_company)
        for i_salary,query_salary in enumerate(soup_product.find_all("span",class_="v-fw-600")):
            if i_salary == 1:
                min_salary = query_salary.text
            if i_salary == 2:
                max_salary = query_salary.text
        for query_salary in soup_product.find_all("div",class_="rt-Flex _rangeAverage_118fo_42"):
            median_salary = query_salary.text.replace("Median: ","")
            print(median_salary)
        for query_describe in soup_product.find_all("p",class_="rt-Text"):
            describe = query_describe.text
        print(describe)
        print(min_salary,max_salary)
        # for min_salar in soup_product.find_all("span",class_="v-fw-600 v-fs-12"):
        #     print(min_salar.text)


    # work with catalog
    def open_categories(self):
        # for url_position in self.url_positions:
        url_position = "https://www.vendr.com/categories/devops"
        profession_page = requests.get(url_position, headers = self.header)
        career_soup = BeautifulSoup(profession_page.content, "lxml")


        for parse_category in career_soup.find_all("h2"):
            if (parse_category.text == "Browse all categories") | (parse_category.text == "Categories in DevOps"):
                continue
            # !!! wait can be error Devops change on another
            array_jrcts =json_read_catalog.json_read_cat("devops", parse_category.text)
            for array_jrct in array_jrcts:
                self.url_products.append(array_jrct)




if __name__ == "__main__":
    # we get work positions
    positions = ["DevOps", "IT Infrastructure", "Data Analytics and Management"]
    Vendr = Vendr(positions)
    # start work with url element
    Vendr.main_directory()