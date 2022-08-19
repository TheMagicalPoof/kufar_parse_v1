import datetime

from peewee import *

db = SqliteDatabase("test.db")


class Region(Model):
    id = PrimaryKeyField(unique=False)
    name = TextField()

    class Meta:
        database = db


class District(Model):
    id = PrimaryKeyField(unique=False)
    name = TextField()
    region_id = ForeignKeyField(Region, backref="region")

    class Meta:
        database = db


class User(Model):
    id = PrimaryKeyField(unique=False)
    uid = IntegerField(unique=False)
    username = TextField()
    first_name = TextField(null=False)
    last_name = TextField(null=False)
    phone_num = IntegerField(null=False)
    until_premium = DateField(null=False)
    reg_date = DateField(default=datetime.date.today())

    class Meta:
        database = db

class Search(Model):
    id = PrimaryKeyField(unique=False)
    name = TextField()

    class Meta:
        database = db


class Associations(Model):
    id = PrimaryKeyField(unique=False)
    name = TextField()
    search_id = ForeignKeyField(Search, backref="search")

    class Meta:
        database = db



def create_table():
    db.connect()
    db.create_tables([User, Region, District])


if __name__ == '__main__':
    create_table()
