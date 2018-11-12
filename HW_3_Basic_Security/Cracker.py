# -*- coding: utf-8 -*-
"""
MSDS 7349-404 Data and Network Security
Homework_3    Basic Security  
Exercise 1.1
Jeffrey Lancon  
Date: 4 Nov 2018
"""

def testPass(cryptPass):
    salt = cryptPass[0:2]
    with open('HW3dictionary_2_2_2_2_2_2.txt','r') as f:
        for line in f:
            for word in line.split():
                dicPassword = word.strip('\n')
                cryptWord = fcrypt.crypt(dicPassword,salt)
                #print (salt)
                if (cryptWord == cryptPass):
                    print "[+] Found Password: "+dicPassword+"\n"
                    return
        print "[-] Password Not Found.\n"
        return

def main():
    passFile = open('HW3passwords_2_2_2_2_2_2.txt')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print "[*] Cracking Password For: "+user,"\n    Hash: "+cryptPass
            testPass(cryptPass)

if __name__ == "__main__":
    import fcrypt
    main()
