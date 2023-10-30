# Invoice-Project (TV0.02)
![image](https://github.com/weiz0123/Invoice-Project/assets/76544381/bff389cf-366d-430a-bcdc-0528faa53678)
...
============================================================================================
============================================================================================
# Current Stage
1. Auto Extraction is compeleted
2. be able to init current companies with their invoice
3. be able to add / delete / update information from company / new company

   
# Goal of this version
1. Be Able to Systematically process and store information
2. Better GUI Display
3. Display location of the extraction with proper label
4. Establish a database for storing all the information (can be cloud database??)
   a. firebase - Google
   b. MongleDB
   c. sqlite

   d. mysql or sql server (not recommanded)

   *needs to choose one from the above list
# Challenging Issue:
1. we need to find a way to set up a modle that can be used to read and extract informaiton
   from a dynamic structure (i.e. tables)

## gather as much online source / source code as possible
...
============================================================================================
============================================================================================
# Python 3.9.*
# None Standard Library Used:
1. tesseract-ocr (needs to add to environment variable mannully)
2. opencv / cv2
3. threading (this maybe already in the standard library ?)
4. watchdog
5. pyplot
6. matplot
7. ... (maybe a couple of more ? refering to the source code)

# GUI FrameWork:
1. Qt.
2. Qt Creator 10.0.2 (Community) Version is used for GUI Design
3. PyQt6 and PyQt5 libraries are used for python developmenet of the interfase

# Test Source:
1. the folder structure of the test source is set fixed.
2. DO NOT Manipulate the folder strcuture of the test folder
3. when testing on local machine. paste the path fo the company_test folder to the variable "test_path"
   under the folder "GUI_Management" and under the file "User_Interface_Main.py" on line 19

# NOTICE:
1. Copy the project path to "sys.path.append (#here is the project path)" for each file...
2. this way of importing needs to be fixed
============================================================================================
============================================================================================
# TO START ....
1. After installing the folder, go to the path Invoice-Project/GUI_Management/User_Interface_Main.py
2. Make Sure all the libraries are installed
3. .ui (GUI) File is under GUI_Management
   
