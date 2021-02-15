# -*- coding: utf-8 -*-

import csv
my_file = open('hahaha.csv', 'w')
with open('kr_korean.csv') as csvfile:
    spamreader = csv.reader(csvfile)

    for rows in spamreader:
        result = u'개포 %s 자이,개%s자\n'%(rows[0].decode('utf-8'),rows[0].decode('utf-8')[0],)
        print(unicode(result))
        my_file.write(unicode(result).encode('utf-8'))
        # my_file.write(u'개포 %s 자이,개%s자'%(rows[0].decode('utf-8').encode('utf-8'),rows[0].decode('utf-8').encode('utf-8')[0],))
        # print(u'개포 %s 자이'%(rows[0].decode('utf-8'),), u'개%s자'%(rows[0].decode('utf-8')[0],))
        # spamwriter.writerow([u'개포 %s 자이'%(rows[0].decode('utf-8'),), u'개%s자'%(rows[0].decode('utf-8')[0],)])
        # print(rows[0])
my_file.close()
