from yara_handler import *
from exiftool_handler import *



def ExportALLToCsv(rule,file,csv='all.csv'):

    try:
        metadata = exifExtractAll(file)

        dic = yaraRunRuleFromFile(rule,file)

        for i, d in enumerate(metadata):
            d['rule'] = dic[i]


        data_frame = pd.DataFrame.from_dict(metadata)

        data_frame.to_csv(csv)

    except Exception as e:
        print(e)
        print('Error pleace check exfy -h or exfy --help')