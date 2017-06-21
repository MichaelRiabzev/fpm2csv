import xml.etree.ElementTree as ET
import csv

fpmFields = ['title','user','url','password','notes','category','launcher']

tree = ET.parse("fpm.xml")
root = tree.getroot().findall('PasswordList')[0]

# open a file for writing

dstFile = open('fpm.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(dstFile)
csvwriter.writerow(fpmFields)

for passEntry in root.findall('PasswordItem'):
	csvRow = []

	for field in fpmFields: csvRow.append(passEntry.find(field).text)
	csvwriter.writerow(csvRow)

dstFile.close()
