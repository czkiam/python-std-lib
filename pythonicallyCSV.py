#!/usr/bin/python

import csv
from subprocess import call

header_row = ['title', 'firstname', 'lastname', 'authorid']
generated_row = ['Angular 2: Getting Started', 'Deborah', 'Kurata', 891]
generated_rows = [
    ['Angular 2 fundamentals', 'Jim', 'Cooper', 225],
    ['Building a Web App with ASP.NET Core, MVC 6, EF Core and Angular', 'Shawn', 'Wildermuth', 479]
]

ps_data = open('ps_data.csv', 'w')

wtr = csv.writer(ps_data)


wtr.writerow(generated_row)
wtr.writerows(generated_rows)

ps_data.close()

ps_headerdata = open('ps_headerdata.csv', 'w')
dw = csv.DictWriter(ps_headerdata, fieldnames = header_row)
dw.writeheader()

first = dict(zip(header_row, generated_row))
#print first

rows = [dict(zip(header_row, row)) for row in generated_rows ]

#print rows

dw.writerows(rows)

ps_headerdata.close()

ps_data = open('ps_data.csv', 'r')

rdr =  csv.reader(ps_data)

for row in rdr:
    print row

print '---------------------------'

ps_headerdata = open('ps_headerdata.csv', 'r')
dr = csv.DictReader(ps_headerdata)

for row in dr:
    print row

#call(["more", r"D:\GItRepos\python-std-lib\ps_data.csv"])
 