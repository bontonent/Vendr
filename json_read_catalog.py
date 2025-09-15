# Json for get all company code names
import requests

def json_read_cat(position,name_category):
    # Element For create url
    re_name_category = name_category.replace("(", "").replace(")", "").replace("/", "").replace(" ", "-").replace(",","").lower()
    data_for_search = []

    # In this site we can open page 3 from 2.
    # If we open 3 without products.
    # We don't get products and stop work with this url position
    i = 0
    while True:
        i = i + 1; page_data_for_search = []
        # Connect to json with all necessary data
        url = f"https://www.vendr.com/categories/{position}/{re_name_category}?page={i}&_data=routes%2F_marketplace.categories.%24categorySlug.%24subCategorySlug._index"
        print(url)
        params = {
            "facets": [],
            "sortParam": "RELEVANCE",
            "nonOnBoardedDealer": False,
            "enableQueryCorrection": True
        }
        headers = {
            "content-type": "application/json; charset=utf-8",
            "accept": "*/*",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
        }

        # if error try see response
        response = requests.get( url, headers=headers, params=params)
        json_work_space = response.json()

        # Get data from json
        for js_companies in json_work_space["companies"]:
            slug = "".join(["https://www.vendr.com/marketplace/",js_companies["slug"]])

            print(slug)

            data_for_search.append(slug)
            page_data_for_search.append(slug)

        if len(page_data_for_search) == 0:
            break
    # return all create url companies
    return data_for_search