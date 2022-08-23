import datetime

from peewee import *

db = SqliteDatabase("test.db")


class Region(Model):
    id = PrimaryKeyField(unique=True)
    name = CharField()

    class Meta:
        database = db


class District(Model):
    id = PrimaryKeyField(unique=True)
    region_id = ForeignKeyField(Region, backref="region")
    district_name = CharField()

    class Meta:
        database = db


class User(Model):
    id = PrimaryKeyField(unique=True)
    uid = IntegerField(unique=True)
    username = CharField()
    phone_num = IntegerField(null=True)
    first_name = CharField(null=True)
    last_name = CharField(null=True)
    until_premium = DateField(null=True)
    reg_date = DateField(default=datetime.date.today(), null=True)
    is_active = BooleanField(default=True)

    class Meta:
        database = db

class Item(Model):
    id = PrimaryKeyField(unique=True)
    item_name = CharField()
    price_from = IntegerField(null=True)
    price_to = IntegerField(null=True)
    district_id = ForeignKeyField(District, backref="district", null=True)
    region_id = ForeignKeyField(Region, backref="region", null=True)
    until_active = DateField(null=True)
    user_id = ForeignKeyField(User, backref="user")

    class Meta:
        database = db


class Tag(Model):
    id = PrimaryKeyField(unique=True)
    tag_name = CharField()

    class Meta:
        database = db


class Associations(Model):
    id = PrimaryKeyField(unique=True)
    tag_id = ForeignKeyField(Tag, backref="tag")
    item_id = ForeignKeyField(Item, backref="item")

    class Meta:
        database = db


class Feedback(Model):
    id = PrimaryKeyField(unique=False)
    user_id = ForeignKeyField(User, backref="user")
    message_id = IntegerField()


    class Meta:
        database = db


def create_table():
    db.connect()
    db.create_tables([User, Region, District, Item, Tag, Associations, Feedback])


if __name__ == '__main__':
    create_table()
