from sqlalchemy import Column, Integer, \
    String, Table, ForeignKey, select
from engine_config import engine, metadata


# Getting SQL-request to create Table 'authors'
authors = Table('authors', metadata,
             Column('id', Integer(), primary_key=True),
             Column('name', String(150), nullable=False),
             Column('surname', String(150), nullable=False)
)

# Getting SQL-request to create Table 'books'
books = Table('books', metadata,
             Column('id', Integer(), primary_key=True),
             Column('title', String(250), nullable=False),
             Column('author_id', ForeignKey(authors.c.id))
)

# Creating Tables
metadata.create_all(engine)
