#!/usr/bin/env python2
'''
Extract DICOM header fields required by NDARs Common Data Element format and generate CSV file

AUTHOR
----
Mike Tyszka, Ph.D.

DATES
----
2016-03-31 JMT From scratch

REQUIRES
----
Python 2.7 and PyDICOM package
'''

import os
import dicom
import argparse

def main():

    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Exctract DICOM header fields for NDAR CDE')
    parser.add_argument('-d','--dicomdir', required=True, help='DICOM series directory')
    parser.add_argument('-g','--guid', required=True, help='Subject NDAR GUID')
    parser.add_argument('-n','--ndarfile', required=True, help='Output NDAR CSV file')

    args = parser.parse_args()

    dicomdir = args.dicomdir
    guid = args.guid
    ndarfile = args.ndarfile

    # Find first file in DICOM directory
    try:
        dir_list = os.listdir(dicomdir)
    catch:


    first_dicom = dir_list[0]

    # Load header from first file



if __name__ == '__main__':

    main()