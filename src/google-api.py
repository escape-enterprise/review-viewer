# Google API Backend for Review Viewer
# by Caleb "fivesixfive" North

# Imports
from requests import get, post

# IDs
EE_ENTERPRISE_ID = "ChIJ6SbUjmFvkogRQSBaQSB7QsM"
EE_BUSINESS_ID = "06876989116557201318"

# API URLS
LOCATION_ALL_REVIEWS = f"https://mybusiness.googleapis.com/v4/accounts/%s/locations/%s/reviews"

# Temp req
print(get(LOCATION_ALL_REVIEWS % (EE_BUSINESS_ID, EE_ENTERPRISE_ID)).text)