from peewee import *
db = SqliteDatabase("test.db")


class Region(Model):
    id = PrimaryKeyField(unique=True)
    name = TextField()

    class Meta:
        database = db


class District(Model):
    id = PrimaryKeyField(unique=True)
    name = TextField()
    region_id = ForeignKeyField(Region,  backref="region")





