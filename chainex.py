from os import system, name 
from time import sleep 
import datetime
import random
opers = name
#This is for debugging:
debug = 0
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
        #Variable Setting
        crypt = ""
        date = datetime.datetime.now().day+datetime.datetime.now().month+datetime.datetime.now().year
        #genmerate a key  
        key = ''
 
        for _ in range(4):
            #only alphabetical chars A-z
            rint = random.randint(97, 97 + 26 - 1)
            flip_bit = random.randint(0, 1)
            rint = rint - 32 if flip_bit == 1 else rint
            key += (chr(rint))
        #so now key is our key
        # later we will reverse it again.
        #well right now...
        randtooperate = ""
        for l in key:
            randtooperate += str(ord(l))

        # Start encrypting string
        for i in en:
            num = ord(i)
            #if is odd, place /, if is even, place ;
            # this is only for confusing :D
            if (num%2):
                char = "/"
            else: 
                char = ";"
                # letter by letter is added into crypt (phrase)
            pre = num+date+int(randtooperate)
            crypt += str(pre)+str(char)
        #final print
        if (debug == 1):
            print("Credentials:")
            print("Rand string", key)
            print("Rand number", randtooperate)
            print("Date" , date)
        print("Your message has been succesfully crypted:", "["+key+"]",crypt)
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
            print("Value not valid. Is not a string")
            quit()
        # Var settings
        crypt = ""
        date = datetime.datetime.now().day+datetime.datetime.now().month+datetime.datetime.now().year
        #try to detect key
        try:
            prerand = en.split()
            rand = prerand[0].strip("[").strip("]")
            #print("Rand found", rand)
        except: 
            print("Code not valid.. [Key not found]")
            quit()
        # decryption of key (RAND)
        # Example : [RLGX] 82769313;82769342/82769349;82769349;82769352/
        frand = ""
        for i in rand: 
            frand += str(ord(i))
        # start to decrypt
        if (debug == 1):
            print("Rand found (text): ", rand)
            print("Rand found (Numerical): ", frand)
        final = ""
        x = 0
        #remove key from string to decode 
        try: 
            for i in en[len(rand)+3:].split("/"):
                # 1 of 2 splittings done
                for a in i.split(";"):
                    # if letter is null skip
                    if (a == ""): break
                    # get the chr value by calc the diff
                    x = int(a)-int(date)-int(frand)
                    # add to final output
                    final += str(chr(int(x)))
        except:
            print("Code not valid.. Something failed while decrypting")
            quit()
        print("--------------------")
        print("Result:", final)
        print("--------------------")
        system("pause")
    if(act=="3"):
        quit()