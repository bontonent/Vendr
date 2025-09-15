import requests
from bs4 import BeautifulSoup
import json_read_catalog
from tqdm import tqdm
import connect_database

class Vendr:
    def __init__(self):
        self.products_url = [] # save products_url
        # create url element for work
        self.url_positions = [] # save all catalog company
        self.url_products = [] # save all product page with salary

        # user agent for all page in this .py script
        self.header = {
            "user-agent": "Mozilla/5.0 (Linux i551 x86_64) AppleWebKit/535.17 (KHTML, like Gecko) Chrome/49.0.1341.243 Safari/601"
        }

    def main_directory(self,positions):
        # create all necessary url products
        self.open_categories(positions)

        # Get all necessary data from url elements
        for url_product in tqdm(self.url_products):
            #print(url_product)
            self.get_data(url_product)

    def get_data(self,url_product):
        # clear all data
        name_company = None;median_salary = None;min_salary = None;max_salary = None;describe = None
        # create sou
        product_page = requests.get(url_product, headers=self.header)
        soup_product = BeautifulSoup(product_page.content, "lxml")
        print(url_product)
        for query_name in soup_product.find_all("h1"):
            name_company = query_name.text.replace("What is ","")
            if name_company == "Sorry, we couldn't load this page. Please try again later." or name_company=="There was a problem loading this page. Please try again later.":
                return
        for i_salary,query_salary in enumerate(soup_product.find_all("span",class_="v-fw-600")):
            if i_salary == 1:
                min_salary = query_salary.text
            if i_salary == 2:
                max_salary = query_salary.text
        for query_salary in soup_product.find_all("div",class_="rt-Flex _rangeAverage_118fo_42"):
            median_salary = query_salary.text.replace("Median: ","")
        for query_describe in soup_product.find_all("p",class_="rt-Text"):
            describe = query_describe.text

        if name_company == None:
            name_company = None
        else:
            try:name_company = name_company
            except:name_company=None
        if median_salary == None:
            median_salary = None
        else:
            try:median_salary = float(median_salary.replace("$", "").replace(",", "."))
            except:median_salary = None
        if min_salary == None:
            min_salary = None
        else:
            try:min_salary = float(min_salary.replace("$", "").replace(",", "."))
            except:min_salary = None
        if max_salary == None:
            max_salary = None
        else:
            try:max_salary = float(max_salary.replace("$", "").replace(",", "."))
            except:max_salary=None
        if describe == None:
            describe = None
        else:
            try:describe = describe.strip()
            except:describe = None



        # Element for SQL
        print(name_company)
        print(median_salary)
        print(min_salary)
        print(max_salary)
        print(describe)
        connect_database.create_row(
            name_company
            ,min_salary
            ,median_salary
            ,max_salary
            ,describe
        )

        for min_salar in soup_product.find_all("span",class_="v-fw-600 v-fs-12"):
            print(min_salar.text)


    # work with catalog
    def open_categories(self,positions):

        # create url for all profession
        for position in positions:
            position_text = position.replace(" ", "-").lower()
            url_position = f"https://www.vendr.com/categories/{position_text}"

            profession_page = requests.get(url_position, headers = self.header)
            career_soup = BeautifulSoup(profession_page.content, "lxml")


            for parse_category in career_soup.find_all("h2"):
                if (parse_category.text == "Browse all categories") | (parse_category.text[:10] == "Categories"):
                    continue
                # !!! wait can be error Devops change on another
                array_jrcts =json_read_catalog.json_read_cat(position_text, parse_category.text)
                for array_jrct in array_jrcts:
                    self.url_products.append(array_jrct)




if __name__ == "__main__":
    # we get work positions
    positions = ["IT Infrastructure"
        #, "DevOps"
        #, "Data Analytics and Management"
                 ]
    Vendr = Vendr()
    # start work with url element
    Vendr.main_directory(positions)