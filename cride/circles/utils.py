import csv

from .models.circles import Circle


def import_data(file): 
    """
    Import data from a csv file.
    """
    
    with open(str(file)) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_counter = 0
        for row in csv_reader:
            if line_counter != 0:
                c = Circle(
                    name=row[0],
                    slug_name=row[1],
                    rides_offered=int(row[2]),
                    rides_taken=int(row[3]),
                    is_limited=(False if int(row[4]) == 0 else True),
                    members_limit=int(row[4])
                )
                c.save()
                line_counter += 1
