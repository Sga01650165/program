#------import---------

import datetime
import winsound
import pyfiglet
from faker import Faker

#------printing---------

print(pyfiglet.figlet_format('Strong', font = 'banner3-D'))

#--------moudles--------

timezoning = datetime.datetime.now()

faker = Faker('en_US')

#-----------------------

class StrongPasswordandinformation:

	date_of_time = timezoning.strftime("%X")

	date_of_calendar = timezoning.strftime("%x")

	def saving(self):

		question = int(input("Please specify the number of digits in your password:"))

		randomaly = faker.password(question)

		name = input("choose the name your password:")

		title = "\nyour password for {} , {} , {} -- {} are saved".format(name, randomaly, StrongPasswordandinformation.date_of_calendar, StrongPasswordandinformation.date_of_time)	
		
		print("\n============response============\n\n", title,'\n\n\n================================')
		
		winsound.Beep(1000, 100)
		
		file = open('C:\\Users\\ok\\Desktop\\oo\\savepassfile.txt', 'a')
		
		file.write(title)	

	def create_faker_information(self):
		
		fullname = faker.name()

		phone = faker.phone_number()

		job = faker.job()

		username = faker.user_name()

		password = faker.password()

		email = faker.email()

		address = faker.address()

		favorite_color = faker.color_name()

		website = faker.domain_name()

		title = "\nyour fake information saved\n\n name : {}\n\n Phone Number : {}\n\n job : {}\n\n username : {}\n\n password : {}\n\n email : {}\n\n address : {}\n\n favorite_color : {}\n\n website : {}".format(fullname, phone, job, username, password, email, address, favorite_color, website)

		print("\n============response============\n\n", title,'\n\n\n================================')
		
		winsound.Beep(1000, 100)
		
		file2 = open('C:\\Users\\ok\\Desktop\\oo\\saveinfofile.txt', 'w')

		file2.write(title)		

abj = StrongPasswordandinformation()		

def inputing():
	
	while True:
		
		print("Hello, welcome to my program!!!\n1.giving strong password\n2.giving fake information\n0.Exit\n\n")
	
		q2 = input('enter the your choose:1 or 2 or 0 ; ')
	
		if q2 == '1' :

			abj.saving()

		elif q2 == '2' :
	
			abj.create_faker_information()

		elif q2 == '0' :

			print('Thanks for use my program, see you latter')
		
			break		

		else:
			
			raise Exception("Not found!!! try again")	

inputing()