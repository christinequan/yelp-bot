import sys
from sys import argv
import csv
import rauth
import config
import pprint
import re

# Psuedocode
# 1. read the arguments - location (geocoder)
# 2. build api query
# 3. return the json of restaurants
# 4. build story string
# 5. return sentence (coming up: and google map links)

API_BASE = "http://api.yelp.com/v2/search"

# given the location, return the search parameters as a dictionary
def search_params(location):

    params = dict()
    params["term"] = "restaurant"
    params["location"] = location
    params["radius_filter"] = "10000"
    params["deals_filter"] = True
    params["actionlinks"] = True

    return params

def queryAPI(params):

    session = rauth.OAuth1Session(
        consumer_key = config.key,
        consumer_secret = config.secret,
        access_token = config.token,
        access_token_secret = config.secret_token
    )

    request = session.get(API_BASE, params = params)
    data = request.json()
    session.close()

    return data

def write_headline(location, data):

    businesses = data['businesses'] # list of businesses with deals

    template_base = "In {location}, there are currently {x} deals."
    template_base.format(location = location, x = len(businesses))

    deal_list = list()
    template_deal = """
    {restaurant} is a {star} star {category} restaurant.
    They are offering a {title} deal!
    {deal_description}.
    """
    heads_up = "Heads up! {heads_up}"
    counter = 1

    for entry in businesses:

        # get general restaurant information
        restaurant = entry['name']
        stars = entry['rating']
        category = get_categories(entry['categories'])

        deal = entry['deals'][0]
        description = deal['what_you_get']
        prog = re.compile(r".*(?=.)")
        description_clean = prog.match(description).group()
        deal_line = template_deal.format(restaurant = restaurant,
                             star = stars,
                             title = deal['title'],
                             deal_description = description_clean,
                             category = category)

        # Heads Up
        if "important_restrictions" in deal.keys():
            restrictions = deal['important_restrictions']
            rstr_str = heads_up.format(heads_up = restrictions)
            deal_str = str(counter) + ". " + deal_line + rstr_str
        else:
            deal_str = str(counter) + ". " + deal_line

        deal_list.append(deal_str)
        print(deal_str)
        counter = counter + 1

    return deal_list

def get_categories(categories):
    cat_str = str()
    counter = 1
    for cat in categories:

        if len(categories) == 2:
            cat_str = cat_str + str(cat[0])
        elif counter == len(categories):
            cat_str = cat_str +  str(cat[0])
            return cat_str
        else:
            cat_str = cat_str + str(cat[0]) + ", "
            counter = counter + 1

if __name__ == '__main__':

    if len(argv) < 2:
        print("Need to pass in a name of a location as an argument")

    else:
        location = argv[1]
        params = search_params(location)
        data = queryAPI(params)
        write_headline(location, data)

     # keys: region, total, businesses
     # region gives the geography
     # total gives the number of businesses with deals
     # businesses returns a list of busiessses - each as a dictionary entry
