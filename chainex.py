from os import system, name 
from time import sleep 
import datetime
import random
import eel
debug = 0
eel.init('web')


def encrypt(en, mode):
    if (int(mode) == 1):
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
        return("["+key+"] "+ crypt)
    if (int(mode) == 2):
        try: 
            en = str(en)
        except: 
            print("\033[33mValue not valid. Is not a string")
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
            print("\033[33mCode not valid.. [Key not found]")
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
            print("\033[33mCode not valid.. Something failed while decrypting")
            quit()
        return final
@eel.expose
def pyencrypt(en, mode):
	return(encrypt(en, mode))
eel.start('index.html')