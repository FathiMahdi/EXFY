# EXFY (EXIFTOOL & YARA)

## Content

- [EXFY (EXIFTOOL \& YARA)](#exfy-exiftool--yara)
  - [Content](#content)
  - [Discription](#discription)
  - [Features](#features)
  - [Installation](#installation)
  - [Flags](#flags)
  - [Examples](#examples)
  
## Discription

The exfy is a simple command line too l that mix beteween exiftool and yara

## Features

- Supporting AMS bootloader.
- Supporting Firmware Update Over Air.
- Supporting communication with AMS LoRa nodes.
- Supporting standard modbus command configuration.
- Supporting analog sensor mapping configuration.
- Supporting digital polling & digital interrupt counter.
- Supporting output trigger based on pre-defined rules.

## Installation

- Plug in the power plug or battries.
- Wait untill the `green LED` is on.
- Configure the device see ***[here](#configurations)***.
- Check the the data on senshost see ***[here](#references)***.

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

## Examples
