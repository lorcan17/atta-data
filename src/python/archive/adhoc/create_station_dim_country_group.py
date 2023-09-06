import sqlite3

connection = sqlite3.connect('data/ATTA.sqlite')
cursor = connection.cursor()

# Drop the existing table if it exists

drop_staging_table_query = '''
    DROP TABLE IF EXISTS station_dim
'''
cursor.execute(drop_staging_table_query)

# Create the staging table if it doesn't exist
create_staging_table_query = '''
    CREATE TABLE station_dim (
        uid INTEGER PRIMARY KEY,
        lat REAL,
        lon REAL,
        country_code2 TEXT,
        station_name TEXT,
        city TEXT,
        country TEXT,
        etl_insert_ts DATETIME,
        etl_update_ts DATETIME

    )
'''
cursor.execute(create_staging_table_query)

# Drop the existing table if it exists

drop_staging_table_query = '''
    DROP TABLE IF EXISTS country_income_group
'''
cursor.execute(drop_staging_table_query)

# Create the final table if it doesn't exist
create_final_table_query = '''
    CREATE TABLE IF NOT EXISTS country_income_group (
        economy TEXT,
        region TEXT,
        country_code2 TEXT,
        country_code3 TEXT,
        income_group TEXT,
        lending_category TEXT,
        etl_insert_ts DATETIME,
        etl_update_ts DATETIME
    )
'''
cursor.execute(create_final_table_query)

# Commit changes and close the connection
connection.commit()
connection.close()

print("Tables created.")
