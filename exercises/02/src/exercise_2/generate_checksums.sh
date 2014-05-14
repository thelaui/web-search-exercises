#!/bin/bash

FILE=$1

echo "sum of bytes:"
python bytesum.py $FILE

echo "cksum:"
cksum $FILE

echo "sha1sum:"
sha1sum $FILE
