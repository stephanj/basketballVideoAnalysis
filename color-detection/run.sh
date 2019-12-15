#!/bin/bash

for i in {0..25}
do
   filename="samples/segmented$i.jpg"
   python color.py $filename
done
