#Imports
import logging
import requests
from fetch_key import FetchKey

class StoreObject(FetchKey):
    """SubClass to Fetchkey: Get store attributes. Store id which is updated each week."""
    
    def __init__(self, store: str) -> None:
        self.logger = logging.getLogger(__name__)
        super().__init__()  # execute __init__ method in FetchKey
        self.store_name = store
        self.headers = {
                        'Content-Type': 'application/json',  # Non required argument
                        'X-Api-Key': FetchKey().get_items()  # Using X-Api-Key header as required
                        }
        self.url = "https://ereklamblad.se/api/squid/v2/dealerfront?r_lat=57.694554&r_lng=12.206504&r_radius=2500&limit=12&order_by=name&types=paged%2Cincito"
        self.store_id = self.fetch_id()
        
    def fetch_id(self) -> str:
        """Fetch id for store which updates every week"""
        # Make a request to the API
        response = requests.get(self.url, headers=self.headers)
        # Ensure the request was successful
        if response.status_code == 200:
            self.logger.info('Successful response: code = 200')
            # Parse the JSON response
            data = response.json()
            
            # Loop through the data and extract the desired fields
            for item in data:
                catalogs = item.get("catalogs", [])
                for catalog in catalogs:
                    # print(catalog)
                    if catalog['label'] == self.store_name:
                        catalog_id = catalog.get("id")
                        return catalog_id
                    
        else:
            self.logger.warning('Response unsuccessfull: %d', response.status_code)
            raise Exception("Store id not found due to unsuccessful response")
            