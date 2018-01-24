from peewee import *
import datetime

db = PostgresqlDatabase(
    'post',
    user='postgres', 
    password='root', 
    host='localhost')

class BaseModel(Model):
    class Meta: 
        database = db

class Post(BaseModel):
    author = CharField()
    title = CharField()
    body = TextField()
    date = DateTimeField(default=datetime.datetime.now)

class User(BaseModel):
    username = CharField()
    password = CharField()
    name = CharField()
    
def initialize_db():
    db.connect()
    db.create_tables([Post, User], safe=True)

def close_db():
    db.close()
