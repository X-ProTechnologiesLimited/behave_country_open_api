# file:features/steps/country_api.py
# -----------------------------------------------------------------------------
# DOMAIN-MODEL:
# -----------------------------------------------------------------------------
import requests
class Country(object):

    def __init__(self):
        self.country  = None
        self.url = None
        self.response_json_map = None
        self.environment = None

    @classmethod
    def select_country(context, country):
        return country

    def add_country(self, country):
        self.country = country

    def send_api(self):
        country = self.select_country(self.country)
        self.url = 'https://restcountries.eu/rest/v2/name/'+country+'?fullText=true'
        responseCountry = requests.get(self.url, verify=True)
        dataCountry = responseCountry.json()
        self.response_json_map = {}
        self.response_json_map['http_response_code'] = responseCountry.status_code
        self.response_json_map['capital'] =  dataCountry[0]['capital']
        self.response_json_map['region'] =  dataCountry[0]['region']
        self.response_json_map['url'] =  self.url
