from sqlalchemy import select, insert
from Tables import authors, books
from engine_config import connection


def get_author_id(name, surname):
    # Getting id from table 'authors' by fullname
    data = select(authors).\
        where(
            (authors.c.name == name.title()) &       # 'c' means 'column'
            (authors.c.surname == surname.title())
        )
    author_data = connection.execute(data).fetchone()
    id = author_data.id         # author_data[0]
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
            "name": "Nikolay",
            "surname": "Gogol"
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
            "title": "Dead souls",
            "author_id": get_author_id('Nikolay', 'Gogol')
        }
    ]
)

# Saving changes in DataBase
connection.commit()