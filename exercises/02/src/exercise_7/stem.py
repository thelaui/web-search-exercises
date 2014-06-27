#!/usr/bin/python

import sys
#import Stemmer
from sets import Set
import re

def stem(algo):
    file=open(sys.argv[1],"r+")
    stems=Set()
    #stemmer = Stemmer.Stemmer(algo)
    total_count = 0

    for w in file.read().split():
        word = w.lower()
        word = re.sub("[\, \- \. \" \; \! \* \? \( \) \:]+", "", word.strip())
        if len(word) > 0:
            #stem = stemmer.stemWord(word)

            print word

            stems.add(word)
            total_count += 1

    file.close();

    #for stem in stems:
    #    print stem

    print algo, len(stems), total_count


#stem('english')
stem('porter')
