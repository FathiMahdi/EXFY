import sys
from main_parameter_handler import *

# show program banner
banner('EXFY TOOL')

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