# models.py
from peewee import *

db = SqliteDatabase('database/postCurse.sqlite')

class BaseModel(Model):
    class Meta:
        database = db

class Client(BaseModel):
    id = AutoField(column_name='id')
    fio = CharField(max_length=50)
    address = CharField(max_length=50)

class TypePublication(BaseModel):
    id = AutoField(column_name='id')
    tip = CharField(max_length=30, unique=True)

class Publication(BaseModel):
    id = AutoField(column_name='id')
    id_type = ForeignKeyField(TypePublication, column_name='id_type',backref='publications', to_field='id')
    name = CharField(max_length=50, unique=True)
    price = IntegerField()

class Courier(BaseModel):
    id = AutoField(column_name='id')
    fio = CharField(max_length=100)

class Delivery(BaseModel):
    id = AutoField(column_name='id')
    id_courier = ForeignKeyField(Courier,column_name='id_courier', backref='deliveries',  to_field='id')
    name = CharField(max_length=100)

class Purchase(BaseModel):
    id = AutoField(column_name='id')
    id_publication = ForeignKeyField(Publication, column_name='id_publication', backref='purchases',  to_field='id')
    id_client = ForeignKeyField(Client, column_name='id_client', backref='purchases',  to_field='id')
    id_delivery = ForeignKeyField(Delivery,column_name='id_delivery', backref='purchases', to_field='id')

class Review(BaseModel):
    id = AutoField(column_name='id')
    id_client = ForeignKeyField(Client,column_name='id_client', backref='reviews',  to_field='id')
    id_delivery = ForeignKeyField(Delivery, column_name='id_delivery',backref='reviews', to_field='id')
    grade = IntegerField(column_name='grade')
    text = CharField(max_length=255, null=True, column_name='text')
