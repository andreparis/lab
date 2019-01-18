import datetime
from ..util import Util

class ScheduleModel:
	def __init__(self, id, id_room, title, datetime_ini, datetime_final):
		self.id = id
		self.id_room = id_room
		self.title = title
		self.datetime_ini = datetime_ini
		self.datetime_final = datetime_final

	@property
	def datetime_ini(self):
		return self._datetime_ini
	
	@datetime_ini.setter
	def datetime_ini(self, date):
		if Util.isDatetimeValidFormat(date):
			self._datetime_ini = date

	@property
	def datetime_final(self):
		return self._datetime_final
	
	@datetime_final.setter
	def datetime_final(self, date):
		date_init = Util.strToDatetime(self.datetime_ini)
		date_final = Util.strToDatetime(date)
		if date_init >= date_final:
			raise Exception("Final date must be greater than initial date")
		self._datetime_final = date
		

