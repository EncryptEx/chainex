from os import system, name 
from time import sleep 
import datetime
import random
opers = name
def clear(): 
        # for windows 
    if opers == 'nt': 
        _ = system('cls') 
        # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
clear()
# Input file
chainex = """

  e88'Y88 888 888     e Y8b     888 Y88b Y88 888'Y88 Y8b Y8P 
 d888  'Y 888 888    d8b Y8b    888  Y88b Y8 888 ,'Y  Y8b Y  
C8888     8888888   d888b Y8b   888 b Y88b Y 888C8     Y8b   
 Y888  ,d 888 888  d888888888b  888 8b Y88b  888 ",d  e Y8b  
  "88,d88 888 888 d8888888b Y8b 888 88b Y88b 888,d88 d8b Y8b 
                                                             
"""
while True:
    clear()
    print(chainex)
    print("1) ChainEx Text Encrypt")
    print("2) ChainEx Text Decrypt")
    print("3) Quit")
    act = input("\nWhat do you want to do?")
    if (act==str(1)):
        clear()
        print(chainex)
        print(" ChainEx Text Encrypt")
        en = input("\nPlease enter below text to encode:")
        try: 
            en = str(en)
        except: 
            print("Value not valid.")
            quit()
        crypt = ""
        date = datetime.datetime.now().day
        rand = random.randint(3000,999999)
        for i in en:
            num = ord(i)
            if (num%2):
                char = "/"
            else: 
                char = ";"
            pre = num+date+rand
            crypt += str(pre)+str(char)

        print("Your message has been succesfully crypted:", "["+str(rand)+"]",crypt)
        print("\n\nRemember today's date!")
        system("pause")
    if(act==str(2)):
        clear()
        print(chainex)
        print(" ChainEx Text Decrypt")
        en = input("\nPlease enter below text to decode:")
        try: 
            en = str(en)
        except: 
            print("Value not valid.")
            quit()
        crypt = ""
        date = datetime.datetime.now().day
        try:
            chyper = en.split()
            rand = chyper[0].strip("[").strip("]")
            #print("Rand found", rand)
        except: 
            print("Code not valid..")
            quit()
        final = ""
        x = 0
        try: 
            for i in en[len(rand)+3:].split("/"):
                crypt = crypt
                for a in i.split(";"):
                    if (a == ""): break
                    # print("Analizing..", a)
                    x = int(a)-int(date)-int(rand)
                    # print("Solution", x)
                    final += str(chr(int(x)))
        except:
            print("Code not valid..")
            quit()
        print("--------------------")
        print("Result:", final)
        print("--------------------")
        system("pause")
    if(act=="3"):
        quit()