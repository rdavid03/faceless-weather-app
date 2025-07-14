import csv
import sqlite3

con = sqlite3.Connection('data.sqlite')
cur = con.cursor()
cur.execute('CREATE TABLE "us_cities" ( gnis INTEGER, fips INTEGER, name TEXT, state_name TEXT, class_code TEXT, primary_lat_dec REAL, primary_long_dec REAL, primary_point TEXT);')

f = open('National_Incorporated_Places_and_Counties.csv')
csv_reader = csv.reader(f, delimiter=',')

cur.executemany('INSERT INTO us_cities VALUES (?, ?, ?, ?, ?, ?, ?, ?)', csv_reader)
cur.close()
con.commit()
con.close()
f.close()

