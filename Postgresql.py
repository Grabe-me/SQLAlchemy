from sqlalchemy import create_engine, Column, Integer,\
    String, Table, MetaData, ForeignKey, insert, select

# Set DataBase engine, "echo=True" for console logging
engine = create_engine('postgresql://postgres:freedomofthewar@localhost:5432/alchemy', echo=True)
# Set MetaData object
metadata = MetaData()

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
# Set connection (conn)
connection = engine.connect()


def get_author_id(name, surname):
    # Getting id from table'authors' by fullname
    data = select(authors).\
        where(
            (authors.c.name== name.title()) &
            (authors.c.surname == surname.title())
        )
    author_tuple = connection.execute(data).fetchone()
    id = author_tuple[0]
    return id


# Inserting VAR_1
# Generating SQL-request to insert data (data-gen)
insert_author_v1 = authors.insert().values(
    name='Michael',
    surname='Bulgakov'
)

# Inserting data with conn by data-gen (insert v_1)
author_ins = connection.execute(insert_author_v1)

# data-gen
insert_book_v1 = books.insert().values(
    title='Master and Margaret',
    author_id=author_ins.inserted_primary_key[0] # type: tuple[0]
)

# insert v_1
book_ins = connection.execute(insert_book_v1)

# Inserting VAR_2
insert_authors_v2 = insert(authors)
insert_book_v2 = insert(books)
insert_multy_authors = connection.execute(
    insert_authors_v2, [
        {
            "name": "Lev",
            "surname": "Tolstoy"
        },
        {
            "name": "Jack",
            "surname": "London"
        }
    ]
)

insert_multy_books = connection.execute(
    insert_book_v2, [
        {
            "title": "War and Peace",
            "author_id": get_author_id('Lev', 'Tolstoy')
        },
        {
            "title": "Fairy Tales",
            "author_id": get_author_id('Lev', 'Tolstoy')
        }
    ]
)

# Saving changes in DataBase
connection.commit()

# Generating SQL-request to get data from 'authors' table (select)
s = authors.select()
# Getting data with conn by select
data = connection.execute(s)
# Extracting data and then printing it
print(data.fetchall())
