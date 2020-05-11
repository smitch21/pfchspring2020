import csv
import json
import requests
import re

with open('harvard_processed.csv', mode='w', newline='') as output:
    harvard_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for year in range(2001, 2021):
        payload = {'q': 'accessionyear:' + str(year), 'size': 100, 'apikey': 'ebd40990-8a75-11ea-a066-95faa1e6fe57'}
        r = requests.get('https://api.harvardartmuseums.org/object', params=payload)
        input = json.loads(r.text)
        pages = int(input['info']['pages'])
        for page in range(1, pages+1):
            print(page)
            payload = {'q': 'accessionyear:' + str(year), 'size': 100, 'apikey': 'ebd40990-8a75-11ea-a066-95faa1e6fe57', 'page': page}
            r = requests.get('https://api.harvardartmuseums.org/object', params=payload)
            input = json.loads(r.text)
            for work in input['records']:
                creation_date = str(work['dated'])
                p = re.compile('\d{4}')
                m = p.search(creation_date)
                if not m is None and m.group(0).isnumeric():
                    creation_date = m.group(0)
                    harvard_writer.writerow([work['objectid'], work['accessionyear'], creation_date, work['culture'], work['division'], work['classification']])
