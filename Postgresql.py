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
