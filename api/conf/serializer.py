from flask_restplus import fields
from api.conf.restplus import api


room = api.model('Room information', {
	'id': fields.Integer(readOnly=True, description='The unique identifier of a room'),
	'name': fields.String(required=True, description='Room name')
	})

schedule_room = api.model('Scheduling information for a room', {
	'id': fields.Integer(readOnly=True, description='The unique identifier of a scheduling'),
	'id_room': fields.Integer(readOnly=True, description='The unique identifier of a room scheduled'),
	'name': fields.String(required=True, description='Room name'),
	'datetime_ini': fields.DateTime(required=True, description='Initial date and time scheduled for a room')
	'datetime_final': fields.DateTime(required=True, description='End date and time scheduled for a room')
	})

