from peewee import *

db = SqliteDatabase('/root/wan_monitor_env/wan_monitor/connections.db',threadlocals=True)

class BaseModel(Model):
    class Meta:
        database = db

class wanStatus(BaseModel):
	interfaceName= CharField()
    	upCount = IntegerField()
    	downCount = IntegerField()
    	state = BooleanField()

class wanSettings(BaseModel):
	name= CharField()
	interfaceName = CharField()
     	priority = IntegerField()
      	pingIP  = CharField()
    	
