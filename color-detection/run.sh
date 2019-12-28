#!/bin/bash

for i in {0..25}
do
   filename="samples/segmented$i.jpg"
   python show_colors.py -i $filename
done
