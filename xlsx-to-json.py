import pandas as pd
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta
import os


def capitalize_review(review):
    if pd.isnull(review) or review == '':
        return "No Review"
    else:
        if not review[0].isupper():
            review = review[0].upper() + review[1:]
        return review


def parse_time(time):
    if time == '':
        return None

    if time.endswith(' ago'):
        duration, unit = time.split(' ')[0], time.split(' ')[1]

        if unit == 'years':
            return datetime.now() - relativedelta(years=int(duration))
        elif unit == 'year':
            return datetime.now() - relativedelta(years=1)
        elif unit == 'months':
            return datetime.now() - relativedelta(months=int(duration))
        # Add more conditions for other units if needed

    try:
        return datetime.strptime(str(time), "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return None


def format_to_mysql_date(time):
    if time:
        return time.strftime("%Y-%m-%d %H:%M:%S")
    return None


def xlsx_to_json():
    while True:
        file_name = input(
            "Enter the name of the xlsx file (or 'quit' to exit): ")

        if file_name.lower() == 'quit':
            print("Exiting the program.")
            break

        try:
            if not file_name.endswith('.xlsx'):
                file_name += '.xlsx'

            if not os.path.exists(file_name):
                print("File not found. Please enter a valid file name.")
                continue

            output_file = file_name.replace('.xlsx', '_review_data.json')

            dining_location = input("Enter the dining hall location: ")

            data = pd.read_excel(file_name)

            data_mapped = []
            for index, row in data.iterrows():
                capitalized_name = ' '.join(word.capitalize()
                                            for word in row['name'].split())
                review_text = capitalize_review(row['review-text'])
                time_created = parse_time(row['time-created'])
                created_formatted = format_to_mysql_date(time_created)

                data_mapped.append({
                    'title': capitalized_name,
                    'stars': row['stars'],
                    'review': review_text,
                    'created': created_formatted,
                    'diningLocation': dining_location
                })

            with open(output_file, 'w') as json_file:
                json.dump(data_mapped, json_file, indent=4)

            print(f"Conversion successful. JSON file '{output_file}' created.")

        except Exception as e:
            print(f"An error occurred: {e}")


xlsx_to_json()
