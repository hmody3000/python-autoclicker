import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import colorama

colorama.init()
class Fore():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UL = '\033[4m'
    RESET = '\033[0m'
    	


print(Fore.GREEN + """
██╗░░██╗███╗░░░███╗░█████╗░██████╗░██╗░░░██╗██████╗░░█████╗░░█████╗░░█████╗░
██║░░██║████╗░████║██╔══██╗██╔══██╗╚██╗░██╔╝╚════██╗██╔══██╗██╔══██╗██╔══██╗
███████║██╔████╔██║██║░░██║██║░░██║░╚████╔╝░░█████╔╝██║░░██║██║░░██║██║░░██║
██╔══██║██║╚██╔╝██║██║░░██║██║░░██║░░╚██╔╝░░░╚═══██╗██║░░██║██║░░██║██║░░██║
██║░░██║██║░╚═╝░██║╚█████╔╝██████╔╝░░░██║░░░██████╔╝╚█████╔╝╚█████╔╝╚█████╔╝
╚═╝░░╚═╝╚═╝░░░░░╚═╝░╚════╝░╚═════╝░░░░╚═╝░░░╚═════╝░░╚════╝░░╚════╝░░╚════╝░
 """)
print(Fore.YELLOW + """
█████████████████████████████████████████████████████████████████
██▀▄─██▄─██─▄█─▄─▄─█─▄▄─█─▄▄▄─█▄─▄███▄─▄█─▄▄▄─█▄─█─▄█▄─▄▄─█▄─▄▄▀█
██─▀─███─██─████─███─██─█─███▀██─██▀██─██─███▀██─▄▀███─▄█▀██─▄─▄█
▀▄▄▀▄▄▀▀▄▄▄▄▀▀▀▄▄▄▀▀▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀
""")
print(Fore.BLUE + "Press F to start")


delay = 0.05
button = Button.left
start_stop_key = KeyCode(char='f')



class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True
        print(Fore.YELLOW + 'start clicking')

    def stop_clicking(self):
        self.running = False
        print(Fore.BLUE+ 'stoped clicking' + Fore.RESET)

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)


mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
