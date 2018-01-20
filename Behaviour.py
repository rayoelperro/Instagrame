from pynput.keyboard import Key, Controller
import time

class KeyBoard:
    def __init__(self):
        self.keyboard = Controller()
        self.ok = True
    def PressString(self,charray):
        self.ok = False
        for c in charray:
            self.Press(c)
        self.ok = True
    def PressDelete(self,times):
        for i in range(0,times):
            self.Press(Key.backspace)
    def Press(self,key):
        self.keyboard.press(key)
        self.keyboard.release(key)
        time.sleep(0.01)