import csv
import sqlite3

database = r"C:\sqlite\db\pythonsqlite-marine-copepod.db"
output = "hsujiawei.csv"


from glob import glob; from os.path import expanduser
conn = sqlite3.connect(database)
cursor = conn.cursor()
cursor.execute("select * from proteins;")
#with open("out.csv", "w", newline='') as csv_file:  # Python 3 version    
with open(output, "wb") as csv_file:              # Python 2 version
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([i[0] for i in cursor.description]) # write headers
    csv_writer.writerows(cursor)