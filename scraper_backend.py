"""
I love stackoverflow even though I only partially understand this code!

https://stackoverflow.com/questions/56417474/unable-to-retrieve-data-from-macro-trends-using-selenium-and-read-html-to-create

"""
import requests
from bs4 import BeautifulSoup as bs
import re
import json
import csv
import os

def get_financial_data(company_code, company_name,frequency):
    url = f'https://www.macrotrends.net/stocks/charts/{company_code}/{company_name}/financial-ratios?freq={frequency}'
    r = requests.get(url)
    p = re.compile(r' var originalData = (.*?);\r\n\r\n\r',re.DOTALL)

    data = json.loads(p.findall(r.text)[0])

    headers = list(data[0].keys())
    headers.remove('popup_icon')
        
    results = []

    results.append(headers)

    for row in data:
        soup = bs(row['field_name'])
        field_name = soup.select_one('a, span').text
        fields = list(row.values())[2:]
        fields.insert(0, field_name)
        results.append(fields)

    frequency = frequency

    if frequency == 'A':
        file = f"{company_code}_{company_name}_Annual.csv"
    else:
        file = f"{company_code}_{company_name}_Quarterly.csv"

    with open(file, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)

        indices = [0,13,14,15,16,17,18,19,20]

        for i in indices:
            csvwriter.writerow(results[i])
        
    csvfile.close()

def generate_company_data(company_codes,company_names,Type):

    dir = os.path.join('/Users/rahul/Desktop/Personal Development/Additional_Projects/Financial_Data/',f'{Type}')
    if not os.path.exists(dir):
        os.mkdir(dir)
    
    companies_combinations = []
    
    for i in range(len(company_codes)):
        companies_combinations.append([company_codes[i],company_names[i],'A'])
        companies_combinations.append([company_codes[i],company_names[i],'Q'])
    
    for i in range(len(companies_combinations)):
        get_financial_data(companies_combinations[i][0],companies_combinations[i][1],companies_combinations[i][2])

    print(f'Data for {Type} firms has been saved')





