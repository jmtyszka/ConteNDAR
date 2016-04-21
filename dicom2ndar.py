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
import sys
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
    except:
        print("Problem getting directory listing for %s" % dicomdir)
        sys.exit(1)

    test_dicom = os.path.join(dicomdir, dir_list[0])

    # Open DICOM object
    dcm = dicom.read_file(test_dicom)

    '''
    subjectkey	                GUID		Required	The NDAR Global Unique Identifier (GUID) for research subject
    src_subject_id	            String	20	Required	Subject ID how it's defined in lab/project
    interview_date	            Date		Required	Date on which the interview/genetic test/sampling/imaging was completed. MM/DD/YYYY
    interview_age	            Integer		Required	Age in months at the time of the interview/test/sampling/imaging.
    gender	                    String	20	Required	Gender (M/F/T)
    image_file	                File		Required	Data file (3D Image, 4D Image)
    image_description	        String	512	Required	Image description (BOLD-EPI, MP-RAGE, Multiecho GRE)
    scan_type	                String	50	Required	Type of Scan (fMRI, MR structural (T1), MR structural (T2), MR structural (B0 map)
    scan_object	                String	50	Required	The Object of the Scan (Live)
    image_file_format	        String	50	Required	Image file format (NIFTI)
    image_modality	            String	20	Required	Image modality (MRI)
    transformation_performed	String	4	Required	Performed transformation (Yes, No)
    '''

    # Get Patient ID from DICOM object
    print("Patient Name : %s" % dcm.PatientName)
    print("Sex          : %s" % dcm.PatientSex)
    print("")
    print("Scan Date    : %s" % dcm.AcquisitionDate)

if __name__ == '__main__':

    main()