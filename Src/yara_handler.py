import yara


# run yara from file
def yaraRunRuleFromFile(rule_path,file):
    dic = {}
    try:
        rules = yara.compile(filepath=rule_path)

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


def yaraConvertToCsv(rule_path,csv_path='metadata.csv'):
    yaraRunRule(rule_path)