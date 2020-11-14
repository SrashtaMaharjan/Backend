# import csv
# f = open('file.csv', 'r')
# csv_reader = csv.reader(f)
# for row in csv_reader:
#     print(row)


import csv
class Entry():
    first_name = ''
    last_name = ''
    email = ''
    def __init__(self, **kwargs):
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name') 
        self.email = kwargs.get('email')
    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.email}'

f = open('file.csv', 'r')
csv_reader = csv.reader(f)
entries = []
line_count = -1
for row in csv_reader:

    if any(row) and row[2]:
        if line_count == -1:
            line_count += 1
            continue
        if row[2]:
            entries.append(Entry(first_name = row[0], last_name = row[1], email = row[2].replace('\n', '')))
        else:
            entries[-1].email+= ' ' + row[2]
        line_count += 1
        print(line_count, row)
f.close() 
outputFile = open('VassarMutualAidEntries.txt', 'w')
for entry in entries:
    print(entry, file = outputFile)
outputFile.close()