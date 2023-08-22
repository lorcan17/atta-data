import sqlite3

# Update column auto_generated to 1 for this row
connection = sqlite3.connect('data/atta.sqlite')
cursor = connection.cursor()
update_query = '''
UPDATE CITY_DIM
SET image_filepath = 'images\_Generic.jpg'
WHERE auto_generated = 0
'''
cursor.execute(update_query)
connection.commit()
connection.close()
        