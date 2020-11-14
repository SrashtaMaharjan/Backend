# import csv
# f = open('file.csv', 'r')
# csv_reader = csv.reader(f)
# for row in csv_reader:
#     print(row)

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
    def __str__(self):
        return f'{self.name}, {self.email}, {self.donationPlatform}, {self.needLevel}, {self.notes}'

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
        print(line_count, row)
f.close()

outputFile = open('MutualAidEntries.txt', 'w')
for entry in entries:
    print(entry, file = outputFile)
outputFile.close()