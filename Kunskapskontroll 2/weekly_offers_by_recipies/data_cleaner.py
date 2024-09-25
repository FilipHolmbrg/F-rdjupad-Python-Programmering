#Imports
import logging
import pandas as pd

def clean_data(offer_dict: dict) -> dict:
    "Function to transform and clean data."
    logger = logging.getLogger(__name__)

    df = pd.DataFrame(offer_dict)
    
    #Cleaning and transformation of data
    df['unit'] = df.unit.str.replace('Per ', '').astype(str)
    df['save'] = df.save.str.replace('SPARA ', '').astype(str).apply(lambda x: float(''.join(x.split(':')))/100 if ':' in x else x)
    df['brand'] = df.brand.str.replace(' •', '').astype(str)
    df['price'] = df.price.astype(float)

    df['validity'] = pd.to_datetime(df['validity'])
    df['validity_week'] = df['validity'].apply(lambda x: x.isocalendar()[1])
    df['validity_year'] = df['validity'].apply(lambda x: x.isocalendar()[0])
    df = df.drop('validity', axis=1)
    #Options feature to add: rows with None values in 'save' column should be removed. These are not discount products!
    
    logger.info('Number of rows before removing duplicates: %d', len(df))
    
    #Remove duplicates
    df = df.drop_duplicates()
    logger.info('Number of rows after removing duplicates: %d', len(df))
    
    #Devoid dataleakage by transformation from dataframe into dict (not necessary when this small dataset)
    temp_dict = df.to_dict('split')
    
    data_dict = {c: [] for c in temp_dict['columns']}

    for row in temp_dict['data']:
        for td, col in zip(row, data_dict.values()):
                col.append(td)
    
    return data_dict
    
        

        