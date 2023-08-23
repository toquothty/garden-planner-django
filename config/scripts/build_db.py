from garden.models import Garden_DB
import csv

def run():
    with open("garden_data.csv", encoding="utf-8", newline="") as csv_file:
    # Read in csv, establish session to Database, loop through rows in csv
        csvreader = csv.DictReader(csv_file)

        
        for row in csvreader:
            vegetable = row["vegetable"]
            sow_type = row["sow_type"]
            harvest_days = row["harvest_days"]
            plant_spacing = row["plant_spacing"]
            seed_depth = row["seed_depth"]
            sow_window_start = row["sow_window_start"]
            sow_window_end = row["sow_window_end"]
            transplant_window_start = row["transplant_window_start"]
            transplant_window_end = row["transplant_window_end"]
            harvest_window_start = row["harvest_window_start"]
            harvest_window_end = row["harvest_window_end"]
            vegetable_picture_url = row["vegetable_picture_url"]

            # While in loop, stage column/row data
            create_vegetable = Garden_DB(
                vegetable=vegetable,
                sow_type=sow_type,
                harvest_days=harvest_days,
                plant_spacing=plant_spacing,
                seed_depth=seed_depth,
                sow_window_start=sow_window_start,
                sow_window_end=sow_window_end,
                transplant_window_start=transplant_window_start,
                transplant_window_end=transplant_window_end,
                harvest_window_start=harvest_window_start,
                harvest_window_end=harvest_window_end,
                vegetable_picture_url=vegetable_picture_url,
            )
            # Stage and commit per vegetable in loop
            create_vegetable.save()