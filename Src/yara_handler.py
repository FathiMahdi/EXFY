import yara
import os

# def yara_scanner:
def list_files_in_directory(directory_path):
    isDerectory = False
    file_names = []
    file_name = ''

    try:
        # Ensure the directory path exists
        if not os.path.exists(directory_path):
            print(f"The directory '{directory_path}' does not exist.")
            return
        
        # Get a list of all files in the directory
        files = os.listdir(directory_path)
        isDerectory = True
        # Loop through the list of files
        for file_name in files:
            file_names.append(file_name)
           

        return isDerectory, file_names
    
    except:
        return isDerectory, file_names




# run yara from file
def yaraRunRuleFromFile(rule_path,file):
    #dic = {} # file_name: match
    dic = []
    try:
        rules = yara.compile(filepath=rule_path)

        try: 

            isdir, name_list = list_files_in_directory(file)

            if isdir:
                for name in name_list:
                    
                    matches = rules.match(file+name)

                    #dic[name] =matches
                    dic.append(matches)

                    if len(matches)!=0:
                        print(matches)

                    else:
                        print('File does not match any rule')

        except:
            print('Yaya: file not found')

            
    except:
        print('Yara: rule not found')

    return dic

    

# run yara from direct rule
def yaraRunRule(rule,file):
    dic = {}
    try:
        rules = yara.compile(source=rule)
        
        try:
            matches = rules.match(file)
            if len(matches)!=0:
                print(matches)
            else:
                print('File does not match any rule')
        except:
            print('Yaya: file not found')
    except:
        print('Yara: rule not found')


