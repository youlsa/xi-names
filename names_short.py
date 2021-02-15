# -*- coding: utf-8 -*-

import csv
my_file = open('xi-short-names1.csv', 'w')

for i in range(ord('가'), ord('힣')):
    result = u"개포자이%s\n"%(chr(i))
    my_file.write(result)

for i in range(ord('A'), ord('Z')):
    result = u"개포자이%s\n"%(chr(i))
    my_file.write(result)

my_file.close()





my_file = open('xi-short-names2.csv', 'w')

for i in range(ord('가'), ord('힣')):
    result = u"개포%s자이\n"%(chr(i))
    my_file.write(result)

for i in range(ord('A'), ord('Z')):
    result = u"개포%s자이\n"%(chr(i))
    my_file.write(result)

my_file.close()
