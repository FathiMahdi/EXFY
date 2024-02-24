import sys
from main_parameter_handler import parseMainParameter


# initialize system parameter list
system_parameters = []

# get system parameters
for arg in sys.argv:
    system_parameters.append(arg)


# parse system parameter        
parseMainParameter(system_parameters,len(system_parameters))