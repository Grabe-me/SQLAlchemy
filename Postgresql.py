from sqlalchemy import create_engine, Column, Integer,\
    String, Table, MetaData, ForeignKey, insert


engine = create_engine('postgresql://postgres:freedomofthewar@localhost:5432/alchemy', echo=True)
metadata = MetaData()

author = Table('authors', metadata,
             Column('id', Integer(), primary_key=True),
             Column('name', String(150), nullable=False),
             Column('surname', String(150), nullable=False)
)

book = Table('books', metadata,
             Column('id', Integer(), primary_key=True),
             Column('title', String(250), nullable=False),
             Column('author_id', ForeignKey(author.c.id))
)

# Creating Tables
metadata.create_all(engine)
# Set connection (conn)
connection = engine.connect()
# Inserting VAR_1
# Generating SQL-request to insert data (data-gen)
insert_author = author.insert().values(
    name='Michael',
    surname='Bulgakov'
)

# Inserting data with conn by data-gen (insert v_1)
author_ins = connection.execute(insert_author)
# Saving changes in DataBase (commit)
connection.commit()

# data-gen
insert_book = book.insert().values(
    title='Master and Margaret',
    author_id=author_ins.inserted_primary_key[0] # type: tuple[0]
)

# insert v_1
book_ins = connection.execute(insert_book)
# commint
connection.commit()


# Generating SQL-request to get data from 'authors' table (select)
s = author.select()
# Getting data with conn by select
data = connection.execute(s)
# Extracting data and then printing it
print(data.fetchall())
