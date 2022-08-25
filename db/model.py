import datetime
from create_bot import DB
from peewee import *





class Region(Model):
    id = PrimaryKeyField(unique=True)
    name = CharField()

    class Meta:
        database = DB


class District(Model):
    id = PrimaryKeyField(unique=True)
    region_id = ForeignKeyField(Region, backref="region")
    name = CharField()

    class Meta:
        database = DB


class User(Model):
    uid = PrimaryKeyField(unique=True)
    username = CharField()
    phone_num = IntegerField(null=True)
    first_name = CharField(null=True)
    last_name = CharField(null=True)
    until_premium = DateField(null=True)
    reg_date = DateField(default=datetime.date.today(), null=True)
    is_active = BooleanField(default=True)

    class Meta:
        database = DB


class Item(Model):
    id = PrimaryKeyField(unique=True)
    name = CharField()
    price_from = IntegerField(null=True)
    price_to = IntegerField(null=True)
    district_id = ForeignKeyField(District, backref="district", null=True)
    until_active = DateField(null=True)
    uid = ForeignKeyField(User, backref="user")

    class Meta:
        database = DB


class Tag(Model):
    id = PrimaryKeyField(unique=True)
    name = CharField()

    class Meta:
        database = DB


class Associations(Model):
    id = PrimaryKeyField(unique=True)
    tag_id = ForeignKeyField(Tag, backref="tag")
    item_id = ForeignKeyField(Item, backref="item")

    class Meta:
        database = DB


class Feedback(Model):
    id = PrimaryKeyField(unique=False)
    uid = ForeignKeyField(User, backref="user")
    message_id = IntegerField()

    class Meta:
        database = DB


def create_table():
    DB = SqliteDatabase("test.db")
    DB.create_tables([User, Region, District, Item, Tag, Associations, Feedback])


if __name__ == '__main__':
    create_table()
