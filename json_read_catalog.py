import requests

def json_read_cat(position,name_category):
    re_name_category = name_category.replace("(", "").replace(")", "").replace("/", "").replace(" ", "-").lower()
    data_for_search = []

    # !!!! dangerously. If None in page, I stop function (eazy find bot)
    i = 0
    while True:
        i = i + 1; page_data_for_search = []
        url = f"https://www.vendr.com/categories/{position}/{re_name_category}?page={i}&_data=routes%2F_marketplace.categories.%24categorySlug.%24subCategorySlug._index"
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

        response = requests.get( url, headers=headers, params=params)
        json_work_space = response.json()

        for js_companies in json_work_space["companies"]:
            slug = "".join(["https://www.vendr.com/marketplace/",js_companies["slug"]])

            data_for_search.append(slug)
            page_data_for_search.append(slug)

        # """data-disabled="true"""
        if len(page_data_for_search) == 0:
            break

    return data_for_search