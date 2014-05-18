#!/usr/bin/python

import sys
import operator
import re

file=open(sys.argv[1],"r+")
count={}
total_count = 0

for w in file.read().split():
    word = w.lower()
    word = re.sub("[\, \- \.]+", "", word.strip())
    if len(word) > 0:
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1
        total_count += 1

file.close();


sorted_count = sorted(count.iteritems(), key=operator.itemgetter(1))

count = 50

for key in reversed(sorted_count):
  print key[0], 100.0*key[1]/total_count
  count -= 1
  if count == 0:
    break

