import mysql.connector
import json


def insert_ratings_from_json(file_path):
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='pass',
            database='madEats'
        )

        if connection.is_connected():
            cursor = connection.cursor()

            with open(file_path, 'r') as json_file:
                data = json.load(json_file)

                for row in data:
                    title = row['title']
                    stars = row['stars']
                    review = row['review']
                    dining_location = row['diningLocation']
                    created = row['created']

                    # Prepare INSERT statement
                    insert_query = "INSERT INTO ratings (title, stars, review, diningLocation, created) VALUES (%s, %s, %s, %s, %s)"
                    record = (title, stars, review, dining_location, created)

                    # Execute the INSERT statement
                    cursor.execute(insert_query, record)

                # Commit the changes
                connection.commit()
                print("Data inserted successfully into the ratings table!")

    except Exception as e:
        print("An error occurred:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


# Replace 'path_to_your_json_file' with the actual path to the JSON file
insert_ratings_from_json('./Liz\'s_review_data.json')
