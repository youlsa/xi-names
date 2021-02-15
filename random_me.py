# -*- coding: utf-8 -*-

import csv
import random

results = []
with open('kr_korean.csv') as csvfile:
    spamreader = csv.reader(csvfile)

    for rows in spamreader:
        result = u'개포 %s 자이\t\t(개%s자)'%(rows[0].decode('utf-8'),rows[0].decode('utf-8')[0],)
        results.append(result)



while 1:
    print(random.choice(results)),
    raw_input('...')
    
