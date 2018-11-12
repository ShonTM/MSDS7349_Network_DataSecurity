# -*- coding: utf-8 -*-
"""
MSDS 7349-404 Data and Network Security
Homework_3    Basic Security  
Exercise 2.1
Jeffrey Lancon  
Date: 4 Nov 2018
"""
import zipfile
File_Zip = 'evil_2_2_2_2_2_2_2_2.zip'
zFile = zipfile.ZipFile(File_Zip)
zFile.extractall(pwd='secret')



"""
Exercise 2.2
Jeffrey Lancon  
Date: 4 Nov 2018
"""
import zipfile
File_Zip = 'evil_2_2_2_2_2_2_2_2.zip'
zFile = zipfile.ZipFile(File_Zip)

try:
    zFile.extractall(pwd="foobar")
except Exception, e:
    print 'File: ',File_Zip,'\nPassword: foobar','\nException Raised: ',e


"""
Exercise 2.3
Jeffrey Lancon  
Date: 4 Nov 2018
"""
import zipfile
DicFile = 'HW3Dictionary_2_2_2_2_2_2.txt'
File_Zip = 'evil_2_2_2_2_2_2_2_2.zip'
zFile = zipfile.ZipFile(File_Zip)
with open(DicFile,'r') as f:
    for line in f:
        for word in line.split():
            dicPassword = word.strip('\n')
            try:
                zFile.extractall(pwd=dicPassword)
                print 'File: ',File_Zip,'\n[+] Password: ',dicPassword,'\nCorrect Password Found\n'
#                exit(0)
            except Exception, e:
                print 'File: ',File_Zip,'\n[-] Password: ',dicPassword,'\nException Raised: ',e,'\n'