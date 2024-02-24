import sys
from main_parameter_handler import *


# initialize system parameter list
system_parameters = []

# get system parameters
for arg in sys.argv:
    system_parameters.append(arg)

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

if detect:
    # parse system parameter        
    parseMainParameter(system_parameters,len(system_parameters))

else:
    print('Error flag {} not found'.format(system_parameters[flag_error_index]))