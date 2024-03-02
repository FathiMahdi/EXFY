import sys
from main_parameter_handler import *
import argparse

def main():

    # show program banner
    banner('EXFY TOOL')

    # get the user flags
    parser = argparse.ArgumentParser(prog='EXFY', description='A tool that compine yara and exiftool',epilog='-h or --help to see all commands')
    parser.add_argument('--yara','-y',help='check rules ',action='store_true')
    parser.add_argument('--custom',type=str,help='run costum rules',metavar='yara rules file')
    parser.add_argument('--dir',type=str,help='directory path',metavar='dir apth')
    parser.add_argument('--file',type=str,help='file path',metavar='file path')
    parser.add_argument('--repo',help='yara scan with repository rules',action='store_true')
    parser.add_argument('--update','-u',help='update yara rules',action='store_true')
    parser.add_argument('--exiftool','-e',help='exif tool',metavar='file path or dir path',type=str)
    parser.add_argument('--csv','-c',type=str,help='export as csv',metavar='csv file name and path',required=False,default='exiftool_report.csv')
    parser.add_argument('--report','-r',type=str,help='export yara html report',metavar='report name file name and path')
    parser.add_argument('--all','-a',type=str,help='Yara and exiftool',metavar='')


    # construct argparser object
    args = parser.parse_args()

    #call parser handler
    parserHandler(args)


if __name__ == "__main__":
    main()