﻿# HW for Matrix TL position.
Open project at Pycharm or all over IDE the can run Python 3.11
open termenal and set project dir as working dir,
for example c:\MatrixHW_selenium

Run next command to get all prerequisites for run tests:
**pip install -r requirements.txt**

In case some prerequisites not installed properlly,
Execute it menually in one of 2 options:
1. pip intall **<Package-name>**
2. In IDE go to the file with error , right click on import and will pop up install package option.

To run all tests execute next command:
**python -m pytest**

The report created automaticlly in working directory with name :
**AutomatonPytestReport.html**
You can open it in by double clicing on him in directory or
Right click in IDE and then open with browser option.

Update prerequisites in requirements.txt
** pip freeze > requirements.txt**
