# -*- coding: utf-8 -*-


#import modules
import requests
import json
import csv

# get data from API
response = requests.get("http://api.eia.gov/series/?api_key=29eab1ff543f39f9350752fc989a3365&series_id=PET.MCREXUS2.A")
response_pro = requests.get("http://api.eia.gov/series/?api_key=29eab1ff543f39f9350752fc989a3365&series_id=PET.MCRFPUS1.A")
# replace PET.MCRFPUS1.A to return a function

print(response.status_code)
print(response_pro.status_code)
script = response.json()
script_pro = response_pro.json()

#only get the 'data' list which contains [year, export] or [year, production]
data = script['series'][-1]['data']
data_pro = script_pro['series'][-1]['data']
print(data_pro)


year = []
export = []
production = []
#year 1990-2019
a = ['2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011', '2010', '2009', '2008', '2007', '2006', '2005', '2004', '2003', '2002', '2001', '2000', '1999', '1998', '1997', '1996', '1995', '1994', '1993', '1992', '1991', '1990']
year_selected = list(map(int,a))

print(type(year_selected[0]))

#append year and export number to above empty list
for i in data:
    #if its leap year, then export * 366, else export * 365
    if int(i[0]) in year_selected:
        year.append(int(i[0]))
        if int(i[0]) % 4 == 0:
            if int(i[0]) % 4 == 0:
                if int(i[0]) % 4 == 0:
                    export.append(i[1] * 366)
                else:
                    export.append(i[1] * 365)
            else:
                export.append(i[1] * 366)
        else: export.append(i[1] * 365)  

print(export)
print(year)

#append production # to the production list
for i in data_pro:
    if int(i[0]) in year_selected:
        production.append(i[1])
        
print(production)     

#get export and production amount from 1990 - 2019  
net_export = export[0:30]
production_final = production[0:30]

print(len(net_export))

with open('US_Crude_Oil_Data2.csv', 'w', newline='') as infile:
    pen = csv.writer(infile)
    pen.writerow(['US Crude Oil Production Data from 1990 to 2020'])
    pen.writerow(['Year'] + year)
    pen.writerow(['Net Export'] + net_export)
    pen.writerow(['Production'] + production_final)





















