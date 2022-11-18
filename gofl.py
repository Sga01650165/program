
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
    password = getpass("enter your password (if forgot your password enter other):")
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
    import random
    name = str(input('enter the your name and family:'))
    index_of_name = list_of_names.index(name)
    index_of_pass = list_of_pass.index(index_of_name)
    list_of_pass.remove(index_of_pass)
    ###################
    list_of_number = ['0','1','2','3','4','5','6','7','8','9']
    make_random_number = random.sample(list_of_number,9)
    add_to_string = ''.join(make_random_number)
    list_of_pass.insert(index_of_pass,add_to_string) #ظاهرا در این خط یک باگ سینتکسی وجود دارد که مشکل از روند کدهای بالا هست به کل این قسمت را چشم پوشی کنید
    forgot_pass2(add_to_string)
###################
def forgot_pass2 (number):   # این قسمت برای مثال میباشد
    import ghasedakpack # این ای پی ای با توجه به کد بالا کار میکند که مشکل سینتکسی دارد و علاوه بر آن این ای پی ای برای بنده غیرفعال هست
    phone = int(input("enter the your phone number:"))
    message = number
    receptor = str(phone)                   
    linenumber = "10008566"
    sms = ghasedakpack.Ghasedak("")
    sms.send({'mesaage':message, 'receptor':receptor, 'linenumber':linenumber})
###################
start()

# فعلا برنامه تا این حد است و در ادامه بک اند یک برنامه احتمالا آموزشی طراحی میشود
