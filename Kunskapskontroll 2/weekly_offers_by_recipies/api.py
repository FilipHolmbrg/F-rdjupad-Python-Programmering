#Imports
import logging
import requests
from time import sleep

def fetch_offers(object: object) -> tuple:
    """Function to get weely offers based of object attributes"""
    logger = logging.getLogger(__name__)
    # General url
    url = "https://ereklamblad.se/api/squid/v4/rpc/get_offers"  
    # Create dict used for population of data and creation of datafram
    offer_dict = {
            'validity': [],
            'name': [],
            'price': [],
            'unit': [],
            'save': [],
            'brand': [],
            }
    # Description of items to parse later
    description_list = []
    page_size = 24
    # Prepare request body
    data = {
            "where": {
                "publication_ids": [object.store_id]  # The publication ID you want to filter by
                    },
            "page": {
                "page_size": page_size  # Max number of items per page
                    }
            }
    
    for i in range(3): # Each iteration gives different results, so we need to pickup data many times to be sure to get all.
        sleep(.1)
        after_cursor = None  # Start without any cursor (first page)
        has_next_page = True
        
        while has_next_page:
            sleep(.1) # Pause between pages.
            # Add after_cursor if it's available (for next pages)
            
            if after_cursor:
                data["page"]["after_cursor"] = after_cursor
            else:
                data["page"].pop("after_cursor", None)  # Remove after_cursor if starting from the first page

            response = requests.post(url, json=data, headers=object.headers)
            logger.info('Response code = %d on iteration %d', response.status_code, i)
            
            # Check the response status code
            if response.status_code == 200:
                response_data = response.json()
                
                # Extract and print offers
                offers = response_data.get("offers", [])
                logger.info('numbers of offers at current page: %d', len(offers))

                for offer in offers:
                    offer_dict['validity'].append(offer['validity']['to'])
                    offer_dict['name'].append(offer['name']) 
                    offer_dict['price'].append(offer['price'])
                    description_list.append(offer['description'])
                
                logger.info('Cumulative offer list is at: %d', len(description_list))

                # Handle pagination
                page_info = response_data.get("page_info", {})
                after_cursor = page_info.get("last_cursor", None)  # Get the cursor for the next page
                has_next_page = page_info.get("has_next_page", False)  # Check if there is another page
                
            else:
                logger.warning('Response unsuccessfull: %d on iteration %d', response.status_code, i)
                break
            
    return (description_list, offer_dict)