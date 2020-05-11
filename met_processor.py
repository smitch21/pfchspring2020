import csv
import re


with open('MetObjects.csv', 'r') as input:
    data = csv.reader(input)
    with open('met_processed.csv', mode='w', newline='') as output:
        met_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for work in data:
            accession_date = work[6]
            print(accession_date)
            if accession_date.isnumeric() and int(accession_date[0:4]) >= 2001:
                creation_date = str(work[26])
                p = re.compile('\d{4}')
                m = p.search(creation_date)
                if not m is None and m.group(0).isnumeric():
                    creation_date = m.group(0)
                    met_writer.writerow([work[4], accession_date, creation_date, work[9], work[5], work[43]])
