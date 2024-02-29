import sys
from main_parameter_handler import *
import argparse






def main():

    # show program banner
    banner('EXFY TOOL')

    parser = argparse.ArgumentParser(description='EXFY')
    parser.add_argument('--yara','-y',type=str,help='check rules ',metavar='file path or dir path')
    parser.add_argument('--custom',type=str,help='run costum rules',metavar='yara rules file')
    parser.add_argument('--scan','-s',type=str,help='yara scan with repository rules',metavar='file path or dir path')
    parser.add_argument('--update','-u',type=str,help='update yara rules',metavar='')
    parser.add_argument('--exiftool','-e',type=str,help='exif tool',metavar='file path or dir path')
    parser.add_argument('--csv','-c',type=str,help='export as csv',metavar='csv file name and path')
    parser.add_argument('--report','-r',type=str,help='export yara html report',metavar='report name file name and path')
    parser.add_argument('--all','-a',type=str,help='Yara and exiftool',metavar='')

    args = parser.parse_args()




    # initialize system parameter list
    system_parameters = []

    # get system parameters
    for arg in sys.argv:
        system_parameters.append(arg)

    # check if all the flags are ok
    detect, flag_error_index = FlagChecker(system_parameters)

    # if all ok
    if detect:
        # parse system parameter        
        parseMainParameter(system_parameters,len(system_parameters))

    # else
    else:
        if len(system_parameters)==1:
            print('add -h or --help to to see all commands')

        elif len(system_parameters)>=2:
            print('Error flag {} not found'.format(system_parameters[flag_error_index]))



if __name__ == "__main__":
    main()