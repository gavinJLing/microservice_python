class Advert:
    def __init__(self, id: str, title: str, price: int, reg_year_month: str, body_type: str, miles: int, cc: float,
                 transmission: str, fuel: str, url: url):
        self.id = id
        self.title = title
        self.price = price
        self.reg_year_month = reg_year_month
        self.body_type = body_type
        self.miles = miles
        self.cc = cc
        self.transmission = transmission
        self.fuel = fuel
        self.url = url
        self.descriptionRaw = ""
        self.other1 = ""
        self.other2 = ""
        self.other3 = ""


import requests
from bs4 import BeautifulSoup

spec_list = []

## initialise
car_count = 0

page_count = 0
page = 1
site_domain = "https://www.autotrader.co.uk"

search_url = "/car-search"
detail_url = "/classified/advert/"
query_param = "?sort=price-asc&radius=200&postcode=tn278eh&onesearchad=Used&make=AUDI&model=R8&year-from=2007&year-to=2019&body-type=Coupe&transmission=Automatic"
# query_param = "?sort=price-asc&radius=200&postcode=tn278eh&onesearchad=Used&make=AUDI&model=Q5&transmission=Automatic"
has_more_pages = True
while has_more_pages:
    # request a page
    url = site + search_url + query_param + "&page=" + str(page)
    print(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # did we fi d any ad's

    car_count = int(soup.find('h1', class_="search-form__count").text.split(" ")[0])
    if len(spec_list) == car_count:
        print("PageCount: {}, SpecList: {}".format(page, len(spec_list)))
        # No ad's found - stop
        break

    page_count = int((car_count + 5) / 10)

    print("Processing Ad's from page {} of {}. For total of Car count: {}".format(page, page_count, car_count))
    adverts = soup.find_all('article', class_="search-listing")

    # Process Ad's on current page
    ad_number = 0
    for advert in adverts:
        ad_number += 1
        price = advert.find('div', class_="vehicle-price").text.replace("£", "").replace(",", "")

        info_div = advert.find('div', class_="information-container")
        title = info_div.find('h2', class_="listing-title").text
        ad_url = info_div.find('a', class_="listing-fpa-link")['href']
        ad_id = ad_url.split("/")[3].split("?")[0]

        ## Check fro dups
        is_dup = False
        for exist_ad in spec_list:
            # print("id- {} dup check {} ".format(ad_id, str(exist_ad) ) )
            if exist_ad.id == str(ad_id):
                is_dup = True
                break
        if is_dup:
            print("skipping duplicate add for ad_id " + ad_id)
            continue

        spec_tags = info_div.find('ul', class_="listing-key-specs").findChildren()

        ##print("Page: {}, ad: {}, parse spec structure: {}".format(page, ad_number, spec_tags))
        raw_year = spec_tags[0].text.split(" ")
        raw_bodyType = spec_tags[1].text.lower()
        raw_miles = spec_tags[2].text.replace(",", "").split(" ")
        raw_cc = spec_tags[3].text.replace("L", "")
        ## this is horrid
        ## 1 2 3 4 5 6
        ## 1 2 3 5 6       <- for some ad's the bhp was missing
        if (spec_tags[4].text[-3:] == "bhp"):
            raw_bhp = spec_tags[4].text.split(" ")
            raw_transmission = spec_tags[5].text.lower()
            raw_fuel = spec_tags[6].text.lower()
        else:
            raw_bhp = ""
            raw_transmission = spec_tags[4].text.lower()
            raw_fuel = spec_tags[5].text.lower()

        spec_list.append(Advert(ad_id, title, int(price), raw_year[0] + raw_year[1].replace("(", "/"), raw_bodyType,
                                int(raw_miles[0]), float(raw_cc), raw_transmission, raw_fuel,
                                site + detail_url + ad_id))

    if page == page_count:
        has_more_pages = False
    else:
        page += 1

    # end of page processing, next page?

# end of Site scrape
print("Found {} ad specs".format(len(spec_list)))

## get individual ads for car images and details
ad_number = 0
for advert in spec_list:
    ad_number += 1
    print("inspection of Advert {} of {} for more details".format(ad_number, len(spec_list)))
    print("url: " + advert.url)
    car_detail_response = requests.get(advert.url)
    soup_detail = BeautifulSoup(car_detail_response.text, 'html.parser')
    ##print(soup_detail)

    # <button type="button" class="gallery-thumbs__placeholder"><img src="https://m.atcdn.co.uk/a/media/w100h75/8a84642bf4a24ee1887b101ad68b4ede.jpg" alt=" "></button>

    meta_description = soup_detail.find('meta', attrs={'name': 'og:description'})
    advert.descriptionRaw = meta_description["content"]

    print("Meta detail: #", ad_number, " id:", advert.id, "  desc:", advert.descriptionRaw)


## Repackage and dump to a file for the processing.
json_data = {"source": "autotrader", "timestamp": "20191028"}
json_data['ads'] = []

for advert in spec_list:
    json_data['ads'].append({
        'id': advert.id,
        'title': advert.title.strip(),
        'price': advert.price,
        'reg': advert.reg_year_month,
        'body_type': advert.body_type,
        'miles': advert.miles,
        'cc': advert.cc,
        'tran': advert.transmission,
        'fuel': advert.fuel,
        'url': advert.url,
        'description_raw': advert.descriptionRaw,
        'other1': advert.other1,
        'other2': advert.other2,
        'other3': advert.other3

    })

import json

with open('car_science_autodtrader_20191028.json', 'w') as outfile:
    json.dump(json_data, outfile)






