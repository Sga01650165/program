#=====================

from tkinter import Tk, Label, Entry, StringVar
import speedtest
import time

#=====================

class App(Tk):

	def __init__(self):

		Tk.__init__(self)

		self.text_for_download = StringVar()

		self.text_for_upload = StringVar()

		self.text_for_ping = StringVar()

		self.backend_internet_speed()

		self.Sitting_gefault_app()

		self.Create_label()

		self.Create_entry()

	def Sitting_gefault_app(self):

		self.title('Speed test internet')

		self.geometry('500x600')

		self.resizable(0, 0)

	def Create_label(self):

		Label(self, text = 'Your Internet Speed', font = ('Tahima', 20), foreground = 'red').pack()

		Label(self, text = time.ctime(), font = ('Tahima', 10, 'bold')).place(x = 170, y = 70)

		Label(self, text = 'Speed of download(Mbit/s)', font = ('Tahima', 15), foreground = 'green').place(x = 135, y = 100)

		Label(self, text = 'Speed of Upload(Mbit/s)', font = ('Tahima', 15), foreground = 'green').place(x = 145, y = 250)

		Label(self, text = 'Ping', font = ('Tahima', 15), foreground = 'green').place(x = 235, y = 380)

	def Create_entry(self):

		Entry(self, font = ('arial', 20, 'bold'), textvariable = self.text_for_download, bd = 2, background = 'powder blue', justify = 'center').place(x = 105, y = 170)

		Entry(self, font = ('arial', 20, 'bold'), textvariable = self.text_for_upload, bd = 2, background = 'powder blue', justify = 'center').place(x = 105, y = 320)

		Entry(self, font = ('arial', 20, 'bold'), textvariable = self.text_for_ping, bd = 2, background = 'powder blue', justify = 'center').place(x = 105, y = 445)

	def backend_internet_speed(self):

		self.obj = speedtest.Speedtest()

		self.downloadspeed = round(self.obj.download() / 1024 / 1024, 3)

		self.uploadspeed = round(self.obj.upload() / 1024 / 1024, 3)

		self.pingspeed = (self.obj.results.ping)

		print(time.time())

		self.text_for_download.set(self.downloadspeed)

		self.text_for_upload.set(self.uploadspeed)

		self.text_for_ping.set(self.pingspeed)	

if __name__ == '__main__':

	app = App()

	app.mainloop()


