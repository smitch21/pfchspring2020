import csv
import json
import re

with open('cma_data.json', 'r') as input:
    data = json.load(input)
    with open('cma_processed.csv', mode='w', newline='') as output:
        cma_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for work in data:
            accession_date = work['accession_number'][0:4]
            if accession_date.isnumeric() and int(accession_date) >= 2001:
                creation_date = str(work['creation_date'])
                p = re.compile('\d{4}')
                m = p.search(creation_date)
                if not m is None and m.group(0).isnumeric():
                    creation_date = m.group(0)
                    cma_writer.writerow([work['id'], work['accession_number'], creation_date, work['culture'][0], work['department'], work['type']])