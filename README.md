# Vendr Data Scraper

This project is a web scraper designed to extract job listings from the Vendr website, specifically targeting various positions in the tech industry. The scraper retrieves data in JSON format and stores it in a PostgreSQL database.

## Features

- Fetches job listings for specified positions.
- Constructs URLs to access JSON data.
- Extracts relevant information such as company name, salary details, and job descriptions.
- Stores the extracted data in a PostgreSQL database.
- Utilizes multi-threading for efficient data retrieval.

## Requirements

- Python 3.x
- Libraries:
  - requests
  - BeautifulSoup4
  - psycopg2
  - tqdm

## Installation

## SQL DB

```sql
CREATE DATABASE vendr
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name_company VARCHAR(255),
    min_salary FLOAT,
    median_salary FLOAT,
    max_salary FLOAT,
    describe TEXT
);
```

## Need create .env file
```angular2html
export db_password=<your_db_password>
export db_port=<your_db_port>
export db_host=<your_db_host>
```
## Install libraries
```
pip install -r requirements.txt
```


# Data Parsing Overview

This document outlines the process for extracting data from the Vendr website, specifically focusing on the "Application Development" category.

## Website Overview

The target website is structured to provide various job listings and company information. Below are screenshots illustrating the site layout:

![Website Layout](photo_md/img.png)

### Target Category: Application Development

We aim to extract all relevant data from the "Application Development" section. The following screenshot highlights this category:

![Application Development Category](photo_md/img_1.png)

## URL Construction for JSON Data Retrieval

To fetch the necessary data, we need to construct a URL using the following parameters:

- **position**: This will be set to "DevOps".
- **i**: This represents the page number to parse.

The URL format is as follows:

https://www.vendr.com/categories/{position}/{re_name_category}?page={i}&_data=routes%2F_marketplace.categories.%24categorySlug.%24subCategorySlug._index

### Work example
https://www.vendr.com/categories/data-analytics-and-management/big-data?page=2&_data=routes%2F_marketplace.categories.%24categorySlug.%24subCategorySlug._index

```json
{
   "currentUrl":"https://www.vendr.com/categories/data-analytics-and-management/big-data?page=2",
   "companies":[
      {
         "id":"82b34605-9ae4-41a4-9c97-4ee36fd3e898",
         "slug":"kyligence",
         "name":"Kyligence",
         "legalName":"Kyligence, Inc.",
         "icon":"//backoffice.vendr.com/public-assets/logos/1724519092301/httpssiteprodcdn.kyligence.iowpcontentthemeskyligencethemeimagesheaderfooterlogo.png",
         "description":"Kyligence Zen's AI-powered self-service analytics gives you an AI copilot for your data and metrics. Discover new insights and improve decision-making.",
         "isVendrVerified":false,
         "stats":{
           
         ...
```
- Name company: Kyligence  
- For create url: kyligence

## Create Url
https://www.vendr.com/marketplace/{name_company}

### Work example
https://www.vendr.com/marketplace/kyligence
