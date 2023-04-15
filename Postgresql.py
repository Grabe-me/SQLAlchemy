from sqlalchemy import create_engine, Column, Integer, String, Table, MetaData, ForeignKey


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


metadata.create_all(engine)
insert_author = author.insert().values(
    name='Michael',
    surname='Bulgakov'
)

connection = engine.connect()
author_ins = connection.execute(insert_author)
connection.commit()


insert_book = book.insert().values(
    title='Master and Margaret',
    author_id=author_ins.inserted_primary_key[0]
)

book_ins = connection.execute(insert_book)
connection.commit()

s = author.select()
data = connection.execute(s)
print(data.fetchall())
