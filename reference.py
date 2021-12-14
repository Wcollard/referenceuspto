import os
import xml.etree.ElementTree as ET 
import sqlite3

#create a db
con=sqlite3.connect('reference.db') #creates a db named example.db
cur= con.cursor()

#CREATING A TABLE IN THE DB WITH COLUMNS
cur.execute('''CREATE TABLE IF NOT EXISTS references
				(reference_no. number PRIMARY KEY, ccode text, kcode text, datepub date, name text, notes text)''')

#import fill file

file_name="***.xml"
full_file=os.path.abspath(os.path.join('data', file_name))

#parse the dom

dom=ET.parse(full_file)


namespace={
	xmlns:uscom="urn:us:gov:doc:uspto:common"
}
	





if...
#Patent Numbers or Publication Numbers
for x in references:
	number=
	kindcode=
	date=
	name=
	notes=

if...
#foreign references
for x in references:
	number=
	countrycode=
	kindcode=
	date=
	name=
	notes=

if...
#Non patent Literature
for x in references
	data=


#store in database
cur.executemany("INSERT OR IGNORE INTO references VALUES (?, ?, ?)", reference_list)
con.commit()
