import os
import sys
from sqlalchemy import Column, ForeignKey, Integer,Float, String, DateTime, Enum,ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class myEnum(enum.Enum):
    refund = "refund"
    paid = "paid"
    cancelled = "cancelled"

class Product(Base):
    __tablename__='product'
    id = Column(Integer,primary_key=True)
    name = Column(String(250),nullable=False)
    pricing = Column(Float, nullable=False)
    weight = Column(Float, nullable=False)
    color = Column(String(250),nullable=False)
    shopping_cart = Column(Integer, ForeignKey("shopping_cart.id"))
    status = Column(Enum(myEnum))



    class Customer(Base):
        __tablename__='customer'
        id = Column(Integer,primary_key=True)
        first_name = Column(String(250), nullable=False)
        last_name = Column(String(250), nullable=False)
        email= Column(String(250), nullable=False, unique=True)
        address= Column(String(250), nullable=False)
        shopping_cart_id= Column(Integer,ForeignKey("shopping_cart.id"))

    class Shopping_Cart(Base):
        __tablename__='shopping_cart'
        id = Column(Integer,primary_key=True)
        quantity= Column(Integer)
        price= Column(Float)
        # bill_id= Column(Integer,ForeignKey("bill.id"), primary_key=True)


    class Bill(Base):
        __tablename__='bill'
        id = Column(Integer,primary_key=True)
        created_at = Column(DateTime)
        total_price = Column(Float)
        status = Column(String,Enum("paid", "pending", "refunded", "cancelled"))
        shopping_cart_id= Column(Integer,ForeignKey("shopping_cart.id"))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
