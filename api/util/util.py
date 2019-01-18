from datetime import datetime
import time

class Util:

	@staticmethod
	def isDatetimeValidFormat(string):
		try:
			datetime.strptime(string, "%d/%m/%Y %H:%M")
			return True
		except ValueError:
			raise Exception("Date format invalid!")

	@staticmethod
	def strToDatetime(string):
		try:
			date = datetime.strptime(string, "%d/%m/%Y %H:%M")
			return date
		except ValueError:
			raise Exception("Please, check the time you are trying to schedule your room!")

# print(Util.strToDatetime("30 Nov 00  1:33PM"))
# print(Util.strToDatetime("30/13/2001 14:10"))
# print(Util.strToDatetime("30-11-2001 8:10"))
# print(Util.strToDatetime("30/11/2001 20:10"))
# print(Util.strToDatetime("30-11/2001 08:10"))