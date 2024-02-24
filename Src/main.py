import sys
from main_parameter_handler import *


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
    print('Error flag {} not found'.format(system_parameters[flag_error_index]))