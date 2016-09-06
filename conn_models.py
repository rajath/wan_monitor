from peewee import *

db = SqliteDatabase('connections.db')

class BaseModel(Model):
    class Meta:
        database = db

class wanStatus(BaseModel):
	wanName= CharField()
    	wanUpCount = IntegerField()
    	wanDownCount = IntegerField()
    	wanState = BooleanField()

class wanSettings(BaseModel):
	name= CharField()
	interfaceName = CharField()
     	priority = IntegerField()
      	pingIP  = CharField()
    	