#!/bin/bash

CORPUS_PATH=corpus/*.html

for file in $CORPUS_PATH
do
  python main.py $file
done
