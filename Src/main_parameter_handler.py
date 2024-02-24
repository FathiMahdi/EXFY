import sys
from exiftool_handler import *
from yara_handler import *
from all_handler import *

# -h --help help and banner
# -a -all exiftool + yara + all csv
# -e --exiftool exiftool only
# -y --yara  yara only
# if only application name make -h


# PEY -e 3439yeqhr.png --csv kabgfkjbaf.csv
# PEY -y  rule  path 

avaiable_flags=[
    '-e',
    '--exiftool',
    '-y',
    '--yara',
    '-h',
    '--help',
    '--csv',
    '-c',
    '--source',
    '-s',
    '--all',
    '-a'
]


def FlagChecker(system_parameters):

    detect = False
    flag_error_index = 0

    for i in range(len(system_parameters)):

        if system_parameters[i][0] == '-':

            detect = False
            for j in range(len(avaiable_flags)):

                if system_parameters[i]==avaiable_flags[j]:
                    detect = True

            if detect== False:
                flag_error_index = i
                break   

    return detect , flag_error_index


def parseMainParameter(parameter,arg_counter):

    if arg_counter > 1:

        # for help
        if parameter[1] == '--help' or parameter[1] == '-h':

            print('Help')
            return True
        
        # chek if exiftool is required
        elif parameter[1] == '--exiftool' or parameter[1]== '-e':
            
            # check if csv extraction required
            if (arg_counter>=4) and ((parameter[3] == '--csv') or (parameter[3] == '-c')):

                exifConvertToCsv(parameter[2],parameter[4])

            # others just extract the metadata ond show them in terminal
            elif (arg_counter<=3):
                exifExtractAll(parameter[2])

        # chek if yara is required
        elif parameter[1] == '--yara' or parameter[1]== '-y': 
            
            # check if csv extraction required
            # if (arg_counter>=4) and ((parameter[3] == '--csv') or (parameter[3] == '-c')):

            #    yaraConvertToCsv(parameter[2],parameter[4])

            # PEY -y  -s rule  path 
            if (arg_counter==5) and ((parameter[2] == '--source') or (parameter[2] == '-s')):
                yaraRunRule(parameter[3],parameter[4])
     
            # others just extract the metadata ond show them in terminal
            elif (arg_counter==4) and ((parameter[2] != '--source') or (parameter[2] != '-s')):
         
                yaraRunRuleFromFile(parameter[2],parameter[3])    

        # chek if all is required
        elif parameter[1] == '--all' or parameter[1]== '-a':

            # check if csv extraction required
            if (arg_counter>=4) :

                if arg_counter==5:
                    ExportALLToCsv(parameter[2],parameter[3],parameter[4])
                    
                elif arg_counter==4:
                    ExportALLToCsv(parameter[2],parameter[3])


        # no command found
        else:
        
            return False
        
    else :

        # TODO: print help
        return True
    