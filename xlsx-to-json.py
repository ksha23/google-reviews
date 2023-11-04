import pandas as pd
import json
import os


def capitalize_review(review):
    if pd.isnull(review) or review == '':
        return "No Review"
    else:
        if not review[0].isupper():
            review = review[0].upper() + review[1:]
        return review


def xlsx_to_json():
    while True:
        file_name = input(
            "Please place the xlsx file in the same directory as this script and enter the name of the xlsx file (or 'quit' to exit): ")

        if file_name.lower() in ['quit']:
            print("Exiting the program.")
            break

        try:
            if not file_name.endswith('.xlsx'):
                file_name += '.xlsx'

            if os.path.exists(file_name):
                output_file = file_name.replace('.xlsx', '_review_data.json')

                # Read the Excel file
                data = pd.read_excel(file_name)

                # Map the columns to the desired format
                data_mapped = []
                for index, row in data.iterrows():
                    # Capitalize each word in the 'name' column
                    capitalized_name = ' '.join(
                        word.capitalize() for word in row['name'].split())

                    # Handle the 'review-text' column
                    review_text = capitalize_review(row['review-text'])

                    # Convert 'time-created' to string
                    time_created = str(row['time-created'])

                    data_mapped.append({
                        'title': capitalized_name,
                        'stars': row['stars'],
                        'review': review_text,
                        'time': time_created
                    })

                # Write the mapped data to a JSON file
                with open(output_file, 'w') as json_file:
                    json.dump(data_mapped, json_file, indent=4)

                print(
                    f"Conversion successful. JSON file '{output_file}' created.")

            else:
                print("File not found. Please enter a valid file name.")

        except Exception as e:
            print(f"An error occurred: {e}")


xlsx_to_json()
