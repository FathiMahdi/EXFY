from yara_handler import *
from exiftool_handler import *



def ExportALLToCsv(metadata,dic,csv='all.csv'):

    try:

        # metadata.extend(dic)
        for i, d in enumerate(metadata):
            d.update(dic[i])
        # for i, d in enumerate(metadata):
        #     d['rule'] = dic[i]

        data_frame = pd.DataFrame.from_dict(metadata)

        data_frame.to_csv(csv)

    except Exception as e:
        print(e)
        print('Error pleace check exfy -h or exfy --help')


def ExportALLToHTML(metadata, dic, html='all.html'):
    try:
        for i, d in enumerate(metadata):
            d.update(dic[i])

        # data_frame = pd.DataFrame.from_dict(metadata)

        # html_content = f'<h1>{header}</h1>\n' + data_frame.to_html(index=False)

        # data_frame.to_html(html, index=False)
            
        data_frame = pd.DataFrame.from_dict(metadata)

        header = "EXFY REPORT"
        # Add a header to the HTML file
        html_content = f'<h1>{header}</h1>\n' + data_frame.to_html(index=False)

        with open(html, 'w') as file:
            file.write(html_content)

    except Exception as e:
        print(e)
        print('Error please check exfy -h or exfy --help')