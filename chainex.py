from os import system, name 
from time import sleep 
import datetime
import random
import eel
import base64

# dev purpouses only.
debug = 0
eel.init('web')

# 
# to compile:
# python -m eel chainex.py web --onefile --noconsole --exclude win32com --exclude numpy --exclude cryptography
# 

def encrypt(en, mode, ti='3'):
    if (int(mode) == 1):
        try: 
            en = str(en)
        except: 
            print("Value not valid. STRING TO ENCRYPT")
            quit()
        #Variable Setting
        try:
            ti = int(ti)
        except:
            print("Value not valid. TIME VAR")
            quit()
        # var declaration
        crypt = ""
 
        if (ti == 0):
            # minute
            date = datetime.datetime.now().minute+datetime.datetime.now().hour+datetime.datetime.now().day+datetime.datetime.now().month+datetime.datetime.now().year
        else: 
            if (ti == 1):
                # hour 
                date = datetime.datetime.now().hour+datetime.datetime.now().day+datetime.datetime.now().month+datetime.datetime.now().year
            else: 
                if (ti == 2):
                    # day
                    date = datetime.datetime.now().day+datetime.datetime.now().month+datetime.datetime.now().year
                else:
                    if (ti == 3):
                        # month
                        date = datetime.datetime.now().month+datetime.datetime.now().year
                    else:
                        if (ti == 4):
                            #year
                            date = month+datetime.datetime.now().year
                        else: 
                            print("\033[33mError while trying to get time expiration value. #2=", ti)
                            quit()

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
        toprint = "("+str(ti)+") ["+key+"] "+ crypt
        encodedBytes = base64.b64encode(toprint.encode("utf-8"))
        encodedStr = str(encodedBytes, "utf-8")
        return encodedStr
    if (int(mode) == 2):
        # decryption mode
        try: 
            en = str(en.lstrip())
            decodedBytes = base64.b64decode(en)
            en = str(decodedBytes, "utf-8")
            # check if is a string
        except: 
            print("\033[33mValue not valid. Is not a string")
            quit()
            # quit if no
        # Var settings
        crypt = ""
        try: 
            preti = en.split()
            ti = preti[0].strip("(").strip(")")
            ti = int(ti)
        except: 
            print("\033[33mError while trying to get time expiration value.")
            quit()

        # get time depending of ti value
        if (ti == 0):
            # minute
            date = datetime.datetime.now().minute+datetime.datetime.now().hour+datetime.datetime.now().day+datetime.datetime.now().month+datetime.datetime.now().year
        else: 
            if (ti == 1):
                # hour 
                date = datetime.datetime.now().hour+datetime.datetime.now().day+datetime.datetime.now().month+datetime.datetime.now().year
            else: 
                if (ti == 2):
                    # day
                    date = datetime.datetime.now().day+datetime.datetime.now().month+datetime.datetime.now().year
                else:
                    if (ti == 3):
                        # month
                        date = datetime.datetime.now().month+datetime.datetime.now().year
                    else:
                        if (ti == 4):
                            #year
                            date = month+datetime.datetime.now().year
                        else: 
                            print("\033[33mError while trying to get time expiration value. #2=", ti)
                            quit()


        # get day+month+year
        # old code
        # date = datetime.datetime.now().day+datetime.datetime.now().month+datetime.datetime.now().year
        #try to detect key
        try:
            prerand = en.split()
            rand = prerand[1].strip("[").strip("]")
            #print("Rand found", rand)
        except: 
            print("\033[33mCode not valid.. [Key not found]")
            quit()
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
                print("to decode:", en[len(rand)+7:])
            for i in en[len(rand)+7:].split("/"):
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
            quit()
        return final
@eel.expose
def pyencrypt(en, mode, ti):
    return(encrypt(en, mode, ti))
eel.start('index.html')