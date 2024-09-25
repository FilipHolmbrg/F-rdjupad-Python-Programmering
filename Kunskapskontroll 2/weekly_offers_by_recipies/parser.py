#Imports
import logging
import re

def parser(description_list: list, offer_dict: dict) -> dict:
    """Function to parse list and populates empty entries in dict"""
    logger = logging.getLogger(__name__)
    # key:pattern dict is needed to extract data from description list. 
    parse_dict = {
                'unit': r"Per förp|Per kg|Per st",
                'save': r"SPARA \d{1,2}:\d{2}",
                'brand': r"\b([A-ZÅÄÖÉa-zåäöé\-]{2,})\b •" 
                }

    for string in description_list:
        # dict with parse strings
        for key, pattern in parse_dict.items():
            try:
                dict_string = re.search(pattern, string).group()
            except AttributeError:
                offer_dict[key].append(None)
                logger.debug('String set to None: %s', string)
            else:
                offer_dict[key].append(dict_string)
    return offer_dict