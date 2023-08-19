import sqlite3

connection = sqlite3.connect('data/ATTA.sqlite')
cursor = connection.cursor()

# Drop the existing table if it exists

drop_staging_table_query = '''
    DROP TABLE IF EXISTS city_dim
'''
cursor.execute(drop_staging_table_query)

# Create the staging table if it doesn't exist
create_table = '''
    CREATE TABLE city_dim (
        city TEXT,
        country TEXT,
        image_filepath TEXT
    )
'''
cursor.execute(create_table)

# Commit changes and close the connection
connection.commit()
connection.close()

print("Tables created.")
