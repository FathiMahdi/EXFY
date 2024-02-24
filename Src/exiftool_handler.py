import exiftool
import pandas as pd


def exifExtractAll(img_path):

    metadata={}

    with exiftool.ExifToolHelper() as et:

        try:
            metadata = et.get_metadata(img_path) 

        except:
            print("Error file not found!!")
            return 0

    print(metadata)
    return metadata


def exifConvertToCsv(img_path,csv_path='metadata.csv'):
    metadata  = exifExtraclAll(img_path)
    data_frame = pd.DataFrame.from_dict(metadata)
    data_frame.to_csv(csv_path)


