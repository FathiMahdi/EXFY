# EXFY (EXIFTOOL & YARA)

A tool that combine yara and exiftool 

## Discription

The EXFY is a simple command line tool that mix beteween exiftool and yara, This tool used as a file/s malware detector as well to extract all the file/s meta data

## Content

- [EXFY (EXIFTOOL \& YARA)](#exfy-exiftool--yara)
  - [Discription](#discription)
  - [Content](#content)
  - [Features](#features)
  - [Installation](#installation)
  - [Flags](#flags)
  - [Examples](#examples)
  - [Reference](#reference)
  


## Features

- Suport yara scanner file/dir based on repository rules for more info <a href=https://github.com/iomoath/yara-scanner>Yara scanner by Moath Maharmeh </a>.
- Suport csv and html report extraction.

## Installation

- `pip install -r requirements.txt` or `pip3 install -r requirements.txt`
  
## Flags

The following table shows all the node AT commads where ***x*** is variable :

| **Flag**               | **Description**                                   |
| :----------------------| :-------------------------------------------------|
|  `-e` , `--exiftool`   |  use exiftool only                                |
|  `-y` , `--yara`       |  use yara only                                    |
|  `-a` , `--all`        |  exiftool and yara                                |
|  `-c` , `--csv`        |  export csv file                                  |
|  `-s` , `--source`     |  add rule source                                  |
|  `-h` , `--help`       |  help                                             |
*Table: Progam flags*

You can run exfy -h to see all the avialble command

```shell
python3 exfy.py -h
    _______  __ ________  __   __________  ____  __ 
   / ____/ |/ // ____/\ \/ /  /_  __/ __ \/ __ \/ / 
  / __/  |   // /_     \  /    / / / / / / / / / /  
 / /___ /   |/ __/     / /    / / / /_/ / /_/ / /___
/_____//_/|_/_/       /_/    /_/  \____/\____/_____/
                                                    

usage: EXFY [-h] [--yara] [--custom yara rules file] [--dir dir apth] [--file file path]
            [--repo] [--update] [--exiftool file path or dir path]
            [--csv csv file name and path] [--report report name file name and path] [--all]

A tool that compine yara and exiftool

options:
  -h, --help            show this help message and exit
  --yara, -y            check rules
  --custom yara rules file
                        run costum rules
  --dir dir apth        directory path
  --file file path      file path
  --repo                yara scan with repository rules
  --update, -u          update yara rules
  --exiftool file path or dir path, -e file path or dir path
                        exif tool
  --csv csv file name and path, -c csv file name and path
                        export as csv
  --report report name file name and path, -r report name file name and path
                        export yara html report
  --all, -a             Yara and exiftool

```

## Examples

To run exiftool on dir or file

- `python3 exfy.py --exiftool  Images/` {dir/file}
  
To run exiftool on dir or file and export .csv report

- `python3 exfy.py --exiftool  Images/ --csv report.csv` {dir/file}

To run yara{custom rules}

- `python3 exfy.py --yara  --custom yarafile --file Images/file.jpg` {file}
- `python3 exfy.py --yara  --custom yarafile --file Images/` {dir}

To run both yara{yara scanner repository rules} .html report

- `python3 exfy.py --yara --repo --dir Images/ --report report.html` {dir}
- `python3 exfy.py --yara --repo --dir Images/ --report report.html` {file}
  
To run both yara{yara scanner repository rules} and exify and export .csv and .html report

- `python3 exfy.py --all --repo --dir Images/ --report report` {directory}
- `python3 exfy.py --all --repo --file Images/test.jpg --report report` {file}

To run both yara{custom rules} and exify and export .csv and .html report

- `python3 exfy.py --all --custom custom_rules/r1.yar --dir Images/ --report report`
  
## Reference

- <https://github.com/VirusTotal/yara>
- <https://github.com/smarnach/pyexiftool>
- <https://github.com/iomoath/yara-scanner>
