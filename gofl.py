
#برنامه بک اند لاگین

import time
def start ():
    import pyfiglet
    result = pyfiglet.figlet_format("new program")
    print(result)
    time.sleep(2)
    mainmenu()
###################
def mainmenu ():
    print("welcome, thanks for choose them program")
    time.sleep(2)
    name_family()
    password()
###################
list_of_names = []
def name_family ():
    name = str(input('enter the your name and family:'))
    list_of_names.append(name)
###################
list_of_pass = []
def password ():
    print("your password most have 10 characters with number and strings")
    time.sleep(2)
    a = str(input("enter the password:"))
    if len(a) < 10:
        print("enter the 10 ch pass")
        print("1.again\n2.mainmenu")
        nn = input("choose the option:(1 or 2)")
        if nn == '1':
            password()
        else:
            mainmenu()   
    else:
        list_of_pass.append(a)
        print("your password and name are save good")
        search_login()
###################
def search_login ():
    from getpass4 import getpass
    print("-----------------------------------\nplease login")
    name = str(input("enter your name and family:"))
    password = getpass("enter your password:")
    if password == 'other':
        forgot_pass()
    elif name in list_of_names:
        if password in list_of_pass:
            print("you are login")
        else:
            print("your password is not True")
            print("1.again\n2.mainmenu")
            nn = input("choose the option:(1 or 2)")
            if nn == '1':
                search_login()
            else:
                mainmenu()   
    elif name not in list_of_names:
        if password in list_of_pass:
            print("your name is not found")
            print("1.again\n2.mainmenu")
            nn = input("choose the option:(1 or 2)")
            if nn == '1':
                search_login()
            else:
                mainmenu()   
        else:
            print("your password and name in not found")
            print("1.again\n2.mainmenu")
            nn = input("choose the option:(1 or 2)")
            if nn == '1':
                search_login()
            else:
                mainmenu()                             
###################
def forgot_pass (): # این بخش در مورد ارسال اس ام اس در صورت فراموشی رمز هست که api آن خاموش هست و ببرنامه این بخش کار نمیکند
    pass
###################
def forgot_pass2 ():
    pass
###################
start()

# فعلا برنامه تا این حد است و در ادامه بک اند یک برنامه احتمالا آموزشی طراحی میشود