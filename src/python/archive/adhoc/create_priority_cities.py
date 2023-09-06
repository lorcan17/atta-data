import sqlite3

connection = sqlite3.connect('data/ATTA.sqlite')
cursor = connection.cursor()

# Drop the existing table if it exists

drop_staging_table_query = '''
    DROP TABLE IF EXISTS aqicn_staging
'''
cursor.execute(drop_staging_table_query)

# Create the staging table if it doesn't exist
create_staging_table_query = '''
    CREATE TABLE priority_cities (
        city TEXT,
        country TEXT
    )
'''
cursor.execute(create_staging_table_query)

# Commit changes and close the connection
connection.commit()
connection.close()

print("Tables created.")
