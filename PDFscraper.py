#!/usr/bin/env python

'''
    File name: PDFScraper.py
    Author: mdugan
    Date created: 8/05/2018
    Date last modified: 8/05/2018
    Python Version: 3.7
'''
from tabula import *
convert_into("b_skate_overall2016.pdf", "test.csv", output_format="csv", pages="all")