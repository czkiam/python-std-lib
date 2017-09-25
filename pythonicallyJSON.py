#!/usr/bin/python

import json

data = {
    'sales' : [
        {'day':'Monday','revenue': 100},
        {'day':'Tuesday','revenue': 200},
        {'day':'Wednesday','holiday': True}
    ], 'expensese': 14.99, 'fires': None
}

objSales = json.dumps(data)
print objSales
print '------------------------------'

inputStr = '{"fires": null, "expenses": 14.99, "sales": [{"revenue": 100, "day": "Monday"}, {"revenue": 200, "day": "Tuesday"}, {"day": "Wednesday", "holiday": true}]}'
inputData = json.loads(inputStr)

print inputData

#error. KIV. solve later
#print sum([day for day in inputData['sales'] if 'revenue' in day.keys()])
