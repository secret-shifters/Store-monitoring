# myapp/scripts/populate_db

import csv
import os
from django.conf import settings
from home.models import Store, StoreTiming

# Define paths to the CSV files within the 'csv_data' folder in your app
data_csv_path = os.path.join(settings.BASE_DIR, 'home', 'csv', 'timeZones.csv')
menu_hours_csv_path = os.path.join(settings.BASE_DIR, 'home', 'csv', 'businessHours.csv')

def create_store_data():
    with open(data_csv_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            Store.objects.create(
                store_id=row['store_id'],
                timezone_str=row['timezone_str'],
            )

def populate_store_start_end_time():
    with open(menu_hours_csv_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            store = Store.objects.filter(store_id=row['store_id']).first()
            if store:
                StoreTiming.objects.create(
                    store=store,
                    day=int(row['day']),
                    start_time=row['start_time_local'],
                    end_time=row['end_time_local'],
                )

def main():
    create_store_data()
    populate_store_start_end_time()

if __name__ == "__main__":
    main()
