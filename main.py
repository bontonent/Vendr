# scrapy libraries
import requests
from bs4 import BeautifulSoup
import json_read_catalog
# time load library
from tqdm import tqdm
# connect database .py
import connect_database
# create thread
from concurrent.futures import ThreadPoolExecutor
import threading

class Vendr:
    def __init__(self):
        self.products_url = [] # save products_url
        self.url_positions = [] # save all catalog company
        self.url_products = [] # save all product page with salary

        # User-agent for sites
        self.header = {
            "user-agent": "Mozilla/5.0 (Linux i551 x86_64) AppleWebKit/535.17 (KHTML, like Gecko) Chrome/49.0.1341.243 Safari/601"
        }

    # main round
    def main_directory(self,positions):
        # create url products
        with ThreadPoolExecutor(max_workers=5) as thread_position:
            list(
                tqdm(
                    thread_position.map(self.open_categories,positions)
                    , total=len(positions)
                )
            )

        # Work with page url
        with ThreadPoolExecutor(max_workers = 5) as thread_product:
            list(
                tqdm(
                    thread_product.map(self.get_data,self.url_products)
                    , total=len(self.url_products)
                )
            )

    # Get data from products pages
    def get_data(self,url_product):
        # Clear all data
        name_company = None;median_salary = None;min_salary = None;max_salary = None;describe = None

        # Connect to pages
        product_page = requests.get(url_product, headers=self.header)
        soup_product = BeautifulSoup(product_page.content, "lxml")

        print(url_product)

        # Get company name
        for query_name in soup_product.find_all("h1"):
            name_company = query_name.text.replace("What is ","")
            if name_company == "Sorry, we couldn't load this page. Please try again later." or name_company=="There was a problem loading this page. Please try again later.":
                return

        # Get salary min and max
        for i_salary,query_salary in enumerate(soup_product.find_all("span",class_="v-fw-600")):
            if i_salary == 1:
                min_salary = query_salary.text
            if i_salary == 2:
                max_salary = query_salary.text

        # Get median salary
        for query_salary in soup_product.find_all("div",class_="rt-Flex _rangeAverage_118fo_42"):
            median_salary = query_salary.text.replace("Median: ","")

        # Get describe
        for query_describe in soup_product.find_all("p",class_="rt-Text"):
            describe = query_describe.text

        # Need change, None or Not
        # Need change element

        if name_company == None:
            name_company = None
        else:
            try:name_company = name_company
            except:name_company=None

        if median_salary == None:
            median_salary = None
        else:
            # Put in SQL with type Double
            try:median_salary = float(median_salary.replace("$", "").replace(",", "."))
            except:median_salary = None

        if min_salary == None:
            min_salary = None
        else:
            # Put in SQL with type Double
            try:min_salary = float(min_salary.replace("$", "").replace(",", "."))
            except:min_salary = None

        if max_salary == None:
            max_salary = None
        else:
            # Put in SQL with type Double
            try:max_salary = float(max_salary.replace("$", "").replace(",", "."))
            except:max_salary=None

        if describe == None:
            describe = None
        else:
            try:describe = describe.strip()
            except:describe = None


        # Print all data
        print(name_company)
        print(median_salary)
        print(min_salary)
        print(max_salary)
        print(describe)

        # Connect to database and create rows
        thread_db = threading.Thread(
            target = connect_database.create_row
            , args= (
                name_company
                ,min_salary
                ,median_salary
                ,max_salary
                ,describe
            )
        )
        thread_db.start()
        thread_db.join()


    # Check main catalog profession
    def open_categories(self,position):

        # Connect to page
        position_text = position.replace(" ", "-").lower()
        url_position = f"https://www.vendr.com/categories/{position_text}"
        profession_page = requests.get(url_position, headers = self.header)
        career_soup = BeautifulSoup(profession_page.content, "lxml")
        # Get all url_products
        for parse_category in career_soup.find_all("h2"):
            if (parse_category.text == "Browse all categories") | (parse_category.text[:10] == "Categories"):
                continue

            # Open json script
            array_jrcts = json_read_catalog.json_read_cat(position_text, parse_category.text)
            for array_jrct in array_jrcts:
                self.url_products.append(array_jrct)


if __name__ == "__main__":
    # Name positions for scrapy
    positions = ["IT Infrastructure"
        , "DevOps"
        , "Data Analytics and Management"
                 ]
    # init class
    Vendr = Vendr()
    Vendr.main_directory(positions)