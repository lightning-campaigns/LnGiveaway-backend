import qrcode
import time
from dotenv import load_dotenv

load_dotenv()

class Helper():

    def generateQR(self, username, data):
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        img = qrcode.make(data)
        img.save('./images/'+username+current_time+'.png')