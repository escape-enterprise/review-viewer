# Google API Backend for Review Viewer
# by Caleb "fivesixfive" North

# Imports
import email
from requests import get, post
from google.oauth2 import service_account
import google.auth.transport.requests


# IDs
EE_ENTERPRISE_ID = "ChIJ6SbUjmFvkogRQSBaQSB7QsM"
EE_BUSINESS_ID = "06876989116557201318"

# API URLS
LOCATION_ALL_REVIEWS = "https://mybusiness.googleapis.com/v4/accounts/%s/locations/%s/reviews"

# Scopes
SCOPES = ["https://www.googleapis.com/auth/business.manage", "https://www.googleapis.com/auth/plus.business.manage"]
SERVICE_ACCOUNT_FILE = "/Users/calebnorth/Downloads/ee-review-counter-4cbc6304753b.json"

credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
credentials.refresh(google.auth.transport.requests.Request())

req = get(LOCATION_ALL_REVIEWS.format(EE_BUSINESS_ID, EE_ENTERPRISE_ID) + f"?access_token={credentials.token}")
print(req.text)