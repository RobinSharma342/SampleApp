import requests

ADDRESSES = {
    "AL": {
        "street_name": "Main St",
        "city_name": "Montgomery",
        "zip_code": "36104"
    },
    "AK": {
        "street_name": "Birch Rd",
        "city_name": "Anchorage",
        "zip_code": "99501"
    },
    "AZ": {
        "street_name": "Sunrise Ave",
        "city_name": "Phoenix",
        "zip_code": "85001"
    },
    "AR": {
        "street_name": "Maple St",
        "city_name": "Little Rock",
        "zip_code": "72201"
    },
    "CA": {
        "street_name": "Oak Dr",
        "city_name": "Los Angeles",
        "zip_code": "90001"
    },
    "CO": {
        "street_name": "Pine Ln",
        "city_name": "Denver",
        "zip_code": "80202"
    },
    "CT": {
        "street_name": "Elm St",
        "city_name": "Hartford",
        "zip_code": "06103"
    },
    "DE": {
        "street_name": "Cedar Blvd",
        "city_name": "Wilmington",
        "zip_code": "19801"
    },
    "FL": {
        "street_name": "Sunset Blvd",
        "city_name": "Miami",
        "zip_code": "33101"
    },
    "GA": {
        "street_name": "Peach Tree Dr",
        "city_name": "Atlanta",
        "zip_code": "30301"
    },
    "HI": {
        "street_name": "Coral St",
        "city_name": "Honolulu",
        "zip_code": "96801"
    },
    "ID": {
        "street_name": "Mountain View Rd",
        "city_name": "Boise",
        "zip_code": "83702"
    },
    "IL": {
        "street_name": "Maple Ave",
        "city_name": "Chicago",
        "zip_code": "60601"
    },
    "IN": {
        "street_name": "Park Ln",
        "city_name": "Indianapolis",
        "zip_code": "46204"
    },
    "IA": {
        "street_name": "Cedar Rd",
        "city_name": "Des Moines",
        "zip_code": "50309"
    },
    "KS": {
        "street_name": "Prairie St",
        "city_name": "Topeka",
        "zip_code": "66101"
    },
    "KY": {
        "street_name": "Bluegrass Blvd",
        "city_name": "Louisville",
        "zip_code": "40202"
    },
    "LA": {
        "street_name": "Bayou Rd",
        "city_name": "New Orleans",
        "zip_code": "70112"
    },
    "ME": {
        "street_name": "Pinewood Dr",
        "city_name": "Portland",
        "zip_code": "04101"
    },
    "MD": {
        "street_name": "Chesapeake St",
        "city_name": "Baltimore",
        "zip_code": "21201"
    },
    "MA": {
        "street_name": "Beacon St",
        "city_name": "Boston",
        "zip_code": "02108"
    },
    "MI": {
        "street_name": "Maple Rd",
        "city_name": "Detroit",
        "zip_code": "48201"
    },
    "MN": {
        "street_name": "Birchwood Ave",
        "city_name": "Minneapolis",
        "zip_code": "55101"
    },
    "MS": {
        "street_name": "Magnolia Ln",
        "city_name": "Jackson",
        "zip_code": "39201"
    },
    "MO": {
        "street_name": "St. Louis Ave",
        "city_name": "St. Louis",
        "zip_code": "63101"
    },
    "MT": {
        "street_name": "Big Sky Rd",
        "city_name": "Billings",
        "zip_code": "59101"
    },
    "NE": {
        "street_name": "Cornfield Rd",
        "city_name": "Omaha",
        "zip_code": "68102"
    },
    "NV": {
        "street_name": "Desert Rd",
        "city_name": "Las Vegas",
        "zip_code": "89101"
    },
    "NH": {
        "street_name": "Maple Dr",
        "city_name": "Concord",
        "zip_code": "03301"
    },
    "NJ": {
        "street_name": "Garden St",
        "city_name": "Newark",
        "zip_code": "07102"
    },
    "NM": {
        "street_name": "Desert Blvd",
        "city_name": "Albuquerque",
        "zip_code": "87101"
    },
    "NY": {
        "street_name": "Broadway Ave",
        "city_name": "New York",
        "zip_code": "10001"
    },
    "NC": {
        "street_name": "Cherry Blossom Ln",
        "city_name": "Raleigh",
        "zip_code": "27601"
    },
    "ND": {
        "street_name": "Prairie Ave",
        "city_name": "Fargo",
        "zip_code": "58102"
    },
    "OH": {
        "street_name": "River Rd",
        "city_name": "Columbus",
        "zip_code": "43201"
    },
    "OK": {
        "street_name": "Pecan St",
        "city_name": "Oklahoma City",
        "zip_code": "73102"
    },
    "OR": {
        "street_name": "Fir Ln",
        "city_name": "Portland",
        "zip_code": "97201"
    },
    "PA": {
        "street_name": "Liberty Ave",
        "city_name": "Philadelphia",
        "zip_code": "19103"
    },
    "RI": {
        "street_name": "Ocean Blvd",
        "city_name": "Providence",
        "zip_code": "02901"
    },
    "SC": {
        "street_name": "Palmetto Ave",
        "city_name": "Charleston",
        "zip_code": "29401"
    },
    "SD": {
        "street_name": "Mount Rushmore Rd",
        "city_name": "Rapid City",
        "zip_code": "57701"
    },
    "TN": {
        "street_name": "Music Row",
        "city_name": "Nashville",
        "zip_code": "37203"
    },
    "TX": {
        "street_name": "Lone Star Blvd",
        "city_name": "Austin",
        "zip_code": "73301"
    },
    "UT": {
        "street_name": "Zion Ave",
        "city_name": "Salt Lake City",
        "zip_code": "84101"
    },
    "VT": {
        "street_name": "Green Mountain Rd",
        "city_name": "Burlington",
        "zip_code": "05401"
    },
    "VA": {
        "street_name": "Shenandoah Dr",
        "city_name": "Richmond",
        "zip_code": "23220"
    },
    "WA": {
        "street_name": "Evergreen Blvd",
        "city_name": "Seattle",
        "zip_code": "98101"
    },
    "WV": {
        "street_name": "Appalachian St",
        "city_name": "Charleston",
        "zip_code": "25301"
    },
    "WI": {
        "street_name": "Lakeview Rd",
        "city_name": "Milwaukee",
        "zip_code": "53201"
    },
    "WY": {
        "street_name": "Grand Teton Blvd",
        "city_name": "Cheyenne",
        "zip_code": "82001"
    }
}

def get_random_street_name(state):
    url = "https://randomuser.me/api/?nat=us"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        number = data['results'][0]['location']['street']['number']
        name = data['results'][0]['location']['street']['name']
        return f"{number} {name} {ADDRESSES[state]['city_name']} {state}, {ADDRESSES[state]['zip_code']}"
    else:
        return "Unknown Street"
    