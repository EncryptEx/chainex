from os import system, name 
from sys import exit
from time import sleep 
import datetime
import random
import base64

# dev purpouses only.
debug = 0

# auxiliar functions
def getTime(ti):
    if (ti == 0):
        # minute
        date = datetime.datetime.now().minute+datetime.datetime.now().hour+datetime.datetime.now().day+datetime.datetime.now().month+datetime.datetime.now().year
    elif (ti == 1):
        # hour 
        date = datetime.datetime.now().hour+datetime.datetime.now().day+datetime.datetime.now().month+datetime.datetime.now().year
    elif (ti == 2):
        # day
        date = datetime.datetime.now().day+datetime.datetime.now().month+datetime.datetime.now().year
    elif (ti == 3):
        # month
        date = datetime.datetime.now().month+datetime.datetime.now().year
    elif (ti == 4):
        #year
        date = datetime.datetime.now().year
    else: 
        print("\033[33mError while trying to get time expiration value. #3=", ti)
        exit()
    return date
# core functions.
def encrypt(en, mode, ti, export):
    if (int(mode) == 1):
        if (debug == 1):
            print("==========ENCRYPT METHOD STARTING============")
        try: 
            if (en is None):
                en = " ._. "
            if (en == ""):
                en = " ._. "
            en = str(en)
        except: 
            print("Value not valid. STRING TO ENCRYPT")
            exit()
        #Variable Setting
        try:
            ti = int(ti)
        except:
            print("Value not valid. TIME VAR")
            exit()
        # var declaration
        crypt = ""
 
        date = getTime(ti)

        #genmerate a key  
        key = ''
        for _ in range(5):
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
            if (debug == 1):
                print(pre, " means ", num, "+", date, "+", int(randtooperate))
            crypt += str(pre)+str(char)
            if (debug == 1):
                if (i is not None):
                    if (num is not None):
                        print("letter["+i+"] means ("+str(num)+")")

        if (debug == 1):
            print("Rand found (text):", key)
            print("Rand found (Numerical):", randtooperate)
            print("Time mode found:", ti)
            print("Whoole string encoded:("+str(ti)+") ["+key+"] "+ crypt)
        #final print
        if (debug == 1):
            print("Export:",export)
        if (export is not None and export != ""):
            # no want to export
            exportkey = str("("+str(ti)+") ["+key+"] ")
            encodedBytes = base64.b64encode(exportkey.encode("utf-8"))
            encodedkey = str(encodedBytes, "utf-8")

            crypt = str(crypt)
            aencodedBytes = base64.b64encode(crypt.encode("utf-8"))
            finalencodedcrypt = str(aencodedBytes, "utf-8")
            if (debug == 1):
                print("MODE 1")
                print("Full export key",exportkey)
                print("Full export key e1",encodedBytes)
                print("Full export key e2",encodedkey)
                print("Crypt:", crypt)
                print("Full export crypt e1",aencodedBytes)
                print("Full export crypt e2",finalencodedcrypt)
                print([finalencodedcrypt, encodedkey])
                print("--------------------FINISH ENCODE WITH EXPORT--------------------")
            return [finalencodedcrypt, encodedkey]
            
        else:
            toprint = "("+str(ti)+") ["+key+"] "+ crypt
            encodedBytes = base64.b64encode(toprint.encode("utf-8"))
            encodedStr = str(encodedBytes, "utf-8")
            if (debug == 1):
                print("MODE 2")
                print([encodedStr])
                print("--------------------FINISH ENCODE WITH NO EXPORT--------------------")
            return [encodedStr]
    if (int(mode) == 2):
        # decryption mode
        if (debug == 1):
            print("==========DECRYPT METHOD STARTING============")
            print("mode", mode, "export", export, "time", ti, "string", en)
        
        try: 
            en = str(en).lstrip()
        except:
            print("\033[33mDECODE: Is not a string or can't be converted into it.")
            exit()

        try:
            decodedBytes = base64.b64decode(en)
            en = str(decodedBytes, "utf-8")
            # check if is a string
        except: 
            print("\033[33mSomething went wrong when decoding base64")
            # quit if no
        # Var settings
        crypt = ""
        if (export is not None and export != ""):
            if (debug == 1):
                    print("EXPORT IS ON")
            # KEY IS IMPORTED
            try: 
                export = str(export)
                decodedBytes = base64.b64decode(export)
                export = str(decodedBytes, "utf-8")
            except: 
                print("\033[33mSomething went wrong when decoding base64 of export")
                exit()

            preti = export.split()
            try: 
                if (debug == 1):
                    print("PRETI", preti)
                ti = preti[0].strip("(").strip(")")
                ti = int(ti)
                rand = preti[1].strip("[").strip("]")
            except: 
                print("\033[33mValue not valid. Is not a string while getting #preti-export-yes")
                exit()

            date = getTime(ti)
            length = 0
        else:
            # KEY IS NOT IMPORTED SEPARATELY
            if (debug == 1):
                    print("EXPORT IS OFF")
            try: 
                preti = en.split()
                if (debug == 1):
                    print("preti", preti)    
                ti = preti[0].strip("(").strip(")")
                ti = int(ti)
            except: 
                print("\033[33mError while trying to get time expiration value. #preti-no-export")
                exit()

            # get time depending of ti value
            date = getTime(ti)


            # get day+month+year
            # old code
            # date = datetime.datetime.now().day+datetime.datetime.now().month+datetime.datetime.now().year
            # try to detect key
            try:

                prerand = en.split()
                rand = prerand[1].strip("[").strip("]")
                #print("Rand found", rand)
            except: 
                print("\033[33mCode not valid.. [Key not found]")
                exit()
            length = len(rand)+7
        # decryption of key (RAND)
        # Example : [RLGX] 82769313;82769342/82769349;82769349;82769352/
        frand = ""
        for i in rand: 
            frand += str(ord(i))
        # start to decrypt
        if (debug == 1):
            print("Rand found (text):", rand)
            print("Rand found (Numerical):", frand)
            print("Time mode found:", ti)
            print("Time value found:", date)
            print("Whoole string encoded:", en)
        final = ""
        x = 0
        #remove key from string to decode 
        try: 
            if (debug == 1):
                print("to decode:", en[length:])
            for i in en[length:].split("/"):
                # 1 of 2 splittings done
                for encodedletter in i.split(";"):
                    # if letter is null skip
                    if (debug == 1):
                        print("CHARS",encodedletter)
                    if (encodedletter == "" or encodedletter is None): break
                    # get the chr value by calc the diff
                    x = int(encodedletter)-int(date)-int(frand)
                    letter = str(chr(int(x)))

                    if (debug == 1):
                        print("letter[",letter,"] means (",str(x),")")
                    # add to final output
                    final += letter

        except:
            return "An error ocurred while decoding it."
            exit()
        return[final]