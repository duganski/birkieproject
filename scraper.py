import requests
import bs4
import csv

outputFile = open('RaceResults.csv', 'w')
outputWriter = csv.writer(outputFile)

skate = 'http://birkie.pttiming.com/results/2018/?page=1150&r_page=division&divID=1'
classic = 'http://birkie.pttiming.com/results/2018/?page=1150&r_page=division&divID=2'

# Download a webpage with requests.get
res = requests.get(skate)
res.raise_for_status()
# Create a BeautifulSoup Object from HTML
birkieSoup = bs4.BeautifulSoup(res.text, features='html.parser')

headers = birkieSoup.select('.subheaderRow')
rows = birkieSoup.select('.dataRow')

# Scrape table and write to CSV
for row in rows:
    # print(row.get_text(strip=True))
    outputWriter.writerow([row.get_text("|", strip=True)])
outputFile.close()
