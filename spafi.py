# importing library

import datetime as dt
from winsound import Beep
from pyfiglet import figlet_format as ff
from faker import Faker
from time import sleep
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from getpass import getuser
import os
from termcolor import colored

# starting class program

class Spai:

    timezoning = dt.datetime.now()

    data_of_time, data_of_calendar = timezoning.strftime('%X'), timezoning.strftime('%x')

    faker = Faker('en_US')

    r, r2 = 'Response', '.'

    user_computer = getuser()

    path_of_fake_information = 'C:\\Users\\{}\\Desktop\\oo\\savefakeinformation.txt'.format(user_computer)

    path_of_password = 'C:\\Users\\{}\\Desktop\\oo\\savepasswordfile.txt'.format(user_computer)

    def starting(self):

        print(colored(ff('STRONG', font = 'banner3-D'), 'blue'))

        while 1:

            print("Hello, welcome to my program!!!\n1.giving strong password\n2.giving fake information\n3.search on history passwords\n4.create fake credit card\n0.Exit\n\n")
	
            question = input("Enter the your choice: 1 or 2 (enter 0 for exit) ;")

            if question == '1':

                self.Create_fake_password()

            elif question == '2':

                self.Create_fake_information()

            elif question == '3':

                self.historyofpassword()    

            elif question == '4':

                self.fakecard()    

            elif question == '0':

                print(colored('Thanks for use my program, see you latter', 'yellow'))

                break

            else:

                text = colored('Not found!!! Please try again', 'red')

                print(f'{text}\n{Spai.r2 * 40}')

                Beep(2000, 2000)

                sleep(0.5)

                continue

    def Create_fake_password(self):

        question2 = input('Please enter the name your password:')

        question3 = int(input('Please enter the some numbers:(recomended enter 20); '))

        fake_password = Spai.faker.password(question3)

        self.sending = self.password_lab(fake_password)

        title = "\nyour password for {} , {} , {} -- {} are saved\n{}".format(question2, self.sending, Spai.data_of_calendar, Spai.data_of_time, Spai.r2 * 40)	

        title2 = colored('your password is saved succsefull', 'cyan')

        print(f'{Spai.r:.^40}\n\n\n{title2}\n\n\n{Spai.r2 * 40}')

        Beep(1000, 100)

        self.save_file = open(Spai.path_of_password, 'a')

        self.save_file.write(title)

        self.save_file.close()

    def password_lab(self, fakepassword):
        
        lower_count = upper_count = num_count = special_count = 0

        for char in fakepassword:

           lower_count += char in ascii_lowercase
           upper_count += char in ascii_uppercase
           num_count += char in digits
           special_count += char in punctuation

        self.strength = sum([
            lower_count >= 2,
            upper_count >= 2,
            num_count >= 2,
            special_count >= 2
            ]) / 4 * 100

        if self.strength >= 70.0:

            return fakepassword   

    def Create_fake_information(self):  

        fullname = Spai.faker.name()

        username = Spai.faker.user_name()

        password = Spai.faker.password()

        country = Spai.faker.country()

        job = Spai.faker.job()

        home_address = Spai.faker.address()

        email = Spai.faker.email()

        favorite_color = Spai.faker.color_name()

        website = Spai.faker.domain_name()

        title = "\nyour fake information saved\n\n main name : {}\n\n username : {}\n\n password : {}\n\n country : {}\n\n job : {}\n\n Home address : {}\n\n email : {}\n\n favorite color : {}\n\n website : {}".format(fullname, username, password, country, job, home_address, email, favorite_color, website)

        print(f'{Spai.r:.^40}\n\n {title}\n\n{Spai.r2 * 40}')

        Beep(1000, 100)

        save_file2 = open(Spai.path_of_fake_information, 'a')

        save_file2.write(title)

        save_file2.close()

    def historyofpassword(self):

        gotopathofpasswordtxt = 'C:\\Users\\sajjad\\Desktop\\oo\\savepasswordfile.txt'
        
        if os.path.exists(gotopathofpasswordtxt):

            print(os.system(gotopathofpasswordtxt))

        else:

            print('This directory not found')  

    def fakecard(self):

        fake_number_card = colored(Spai.faker.credit_card_number(card_type = None), 'green')

        print(f'{Spai.r:.^40}\n\n\n{fake_number_card}\n\n\n{Spai.r2 * 40}') 

        Beep(1000, 100)         

obj = Spai()
obj.starting()
