from peewee import *
import datetime

# db = SqliteDatabase('post.db')
db = PostgresqlDatabase(
    'd82mi4nidcdk7d',
    user='zvtcysihlmeoqn', 
    password='4e38515ce95ae971cca3910d1fbf010c285e2f1e168819cac3f820edb9f93847', 
    host='ec2-54-217-218-80.eu-west-1.compute.amazonaws.com')

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
