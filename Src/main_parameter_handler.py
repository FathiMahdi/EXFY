import sys
from exiftool_handler import *
from yara_handler import *
from all_handler import *
import yara_updater
import yara_scanner
import report_generator
import common_functions



def parserHandler(args):

    # parser yara rules update
    if(args.update):
        print("- Updating yara rules ...")
        yara_updater.update()
       
    # parse exif tool
    if(args.exiftool):

        if(args.csv):

            try:
                exifConvertToCsv(args.exiftool,args.csv)
            except:
                print('Please check the file/s path')

        else:
            try:
                exifExtractAll(args.exiftool)
            except:
                print('Please check the file/s path')


    # parse yara
    if(args.yara):
        
        # run yara with custom rule
        if(args.custom):

            try:
                if(args.file):
                    
                    yaraRunRule(args.custom,args.file)
                    

                elif(args.dir):

                    yaraRunRuleFromFile(args.custom,args.dir)
            except:
                print('Erorr running yara on custom rules')

        
        # run yara with repository rules
        elif(args.repo):

            try:
                if(args.file):
                    match_result = yara_scanner.scan_file(args.file)

                elif(args.dir):
                    match_result = yara_scanner.scan_directory(args.dir, 1)


                if match_result is None:
                    raise Exception()
            except:
                sys.exit(0)

        if(args.report):
            report = report_generator.generate_report(match_result)
            common_functions.write_to_file(args.report, report)
            print('[+] Report saved to "{}"'.format(args.report))





    # parse all
           
 #   exfy --yara --file/dir file/dir --custom dd --repo --report