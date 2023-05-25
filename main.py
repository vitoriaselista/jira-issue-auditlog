# This script is created by Ana Vitória Selista for Jira administrative use

import json
import requests
from config import *
from datetime import datetime
import csv

auth = (user_email, api_key)

headers = {
        "Content-Type": "application/json"
    }

def get(url, params={}):
    return requests.get(url, params=params, auth=auth, headers=headers)

# Make a GET request to retrieve the changelog of an issue
search = get(base_url + f'/rest/api/2/issue/{issue_key}/changelog').json()

# List to store the data rows
rows = []

# Field names for the CSV file
field_names = ['Author', 'Author Account Id', 'Change Date', 'Field ID', 'Field Type', 'From String', 'To String']

for value in search['values']:
    author = value['author']['displayName']
    author_account_id = value['author']['accountId']
    change_date = value['created']

    # Formatting the status_change_date
    formatted_date = datetime.strptime(change_date, "%Y-%m-%dT%H:%M:%S.%f%z")
    formatted_date = formatted_date.strftime("%d/%m/%Y %H:%M")

    for item in value['items']:
        field_id = item['fieldId']
        field_type = item['fieldtype']
        from_string = item.get('fromString')
        to_string = item.get('toString')
        print(from_string)

        # Row with the extracted data
        row = [author, author_account_id, formatted_date, field_id, field_type, from_string, to_string]

        # Add the row to the list of rows
        rows.append(row)

# Filename for the CSV file
filename = f'auditlog_{issue_key}.csv'

# Write the data to the CSV file
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(field_names)
    writer.writerows(rows)

print(f"CSV file '{filename}' has been created successfully.")




