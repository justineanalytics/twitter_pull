print "hello world"
import csv
import os

mydir = '/Users/jbraun/Desktop/pythontesting'

print(os.listdir(mydir))
print("postdata.csv")

with open("postdata.csv", "rb") as csv_file:
	data = csv.reader(csv_file)
	for row in data:
		if row["Paid impressions"] == "0":

with open ('postdata.csv', 'rb') as csvfile:
		data = csv.DictReader(csvfile, delimiter=',',lineterminator='\n')
		for row in data:
			if row['Paid impressions']='0'



openfile = open("postdata.csv", "r")
csvwriter = csv.writer(openfile, delimiter=',',lineterminator='\n')
data = csv.DictReader(openfile, delimiter=',',lineterminator='\n')







