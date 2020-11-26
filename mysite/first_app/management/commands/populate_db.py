from django.core.management.base import BaseCommand
from first_app.models import mutual_table


import csv

class Entry():
        name = ''
        email = ''
        donationPlatform = ''
        needLevel = ''
        notes = ''
        def __init__(self, **kwargs):
            self.name = kwargs.get('name')
            self.email = kwargs.get('email')
            self.donationPlatform = kwargs.get('donationPlatform')
            self.needLevel = kwargs.get('needLevel')
            self.notes = kwargs.get('notes') 

class Command(BaseCommand):
    

    def handle(self, *args, **options):
        f = open('mutual.csv', 'r')
        csv_reader = csv.reader(f)      
        entries = []

        line_count = -1
        for row in csv_reader:
            if any(row) and row[2]:
                if line_count == -1:
                    line_count += 1
                    continue
                if row[3]:
                    entries.append(Entry(name = row[0], email = row[1], donationPlatform = row[2], needLevel = row[3], notes = row[4].replace('\n', '')))
                else:
                    entries[-1].donationPlatform += ' ' + row[2]
                line_count += 1
        f.close()

        for entry in entries:
            e = mutual_table()
            e.name = entry.name
            e.email = entry.email
            e.donationPlatform = entry.donationPlatform
            e.needLevel = entry.needLevel
            e.notes = entry.notes
            e.save()
            





