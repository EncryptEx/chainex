# visual 
import eel
eel.init('web')

# 
# to compile:
# python -m eel chainex.py web --onefile --noconsole --exclude win32com --exclude numpy --exclude cryptography --icon=favicon.ico
# 

# IMPORTANT: MAIN WORK ON corechainex.py
import corechainex

# transaltor js - py on visualization
@eel.expose
def pyencrypt(en, mode, ti, exp):
    return(corechainex.encrypt(en, mode, ti, exp))
eel.start('index.html', mode='default')