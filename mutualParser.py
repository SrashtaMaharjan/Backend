import MySQLdb
db=MySQLdb.connect(passwd="7252109691", db="mutual_schema")

c=db.cursor()

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

import csv
f = open('code/mutual.csv', 'r')
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
        #print(line_count, row)
f.close()

#for row in csv_reader:
 #         entry = Entry()
  #        entry.name = row[0]
   #       entry.email = row[1]
    #      entry.donationPlatform = row[2]
     #     entry.needLevel = row[3]
      #    entry.notes = row[4] 
       #   print(f"""INSERT INTO mutual_table VALUES (NULL, "{entry.name}","{entry.email}", "{entry.donationPlatform}", {entry.needLevel}, "{entry.notes}");""") 
for entry in entries:
    c.execute(f"""INSERT INTO mutual_table VALUES (NULL, "{entry.name}","{entry.email}", "{entry.donationPlatform}", {entry.needLevel}, "{entry.notes}");""")

db.commit()