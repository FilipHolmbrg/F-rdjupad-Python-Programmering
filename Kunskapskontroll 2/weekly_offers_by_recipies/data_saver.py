#Imports
import logging
import sqlite3
import pandas as pd

def save_data(data: dict, object: object) -> None: 
    """Function to save data into database table"""
    logger = logging.getLogger(__name__)
    
    database = 'veckans_erbjudande.db'
    current_data = pd.DataFrame.from_dict(data)
    
    try:
        # Create engine and append data
        con = sqlite3.connect(database)
        current_data.to_sql(object.store_name, con, if_exists='append', index=False)
        
        ## Alt 1. Extract current table, remove duplicates and replace table using Pandas
        df_to_clean = pd.read_sql(f'SELECT * FROM "{object.store_name}"', con)
        logger.info('Number of rows before removing duplicates: %d', len(df_to_clean))
        df_cleaned = df_to_clean.drop_duplicates()
        logger.info('Number of rows after removing duplicates: %d', len(df_cleaned))
        df_cleaned.to_sql(f'{object.store_name}', con, if_exists='replace', index=False)
        
        # Commit
        con.commit()
        
        logger.info(f'Data from {object.store_name} stored in table at db: {database}')
        
    except sqlite3.OperationalError as e:
        logger.warning(e)
        print("OperationalError", e)
    
    finally:
        # Close connection
        con.close()
    
    ##############################
    ## Alt 2. Extract current table, remove duplicates and replace table using sqlite3
    # cur = con.cursor()
    # cur.execute(f'CREATE TABLE temp_table AS SELECT DISTINCT * FROM "{self.store}"')
    # con.commit()
    # cur.execute(f'DROP TABLE "{self.store}"')
    # con.commit()
    # cur.execute(f'ALTER TABLE temp_table RENAME TO "{self.store}"')
    # con.commit()
    ##Close connection
    # con.close()
    ##############################