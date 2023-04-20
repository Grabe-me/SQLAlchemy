from sqlalchemy import select
from Tables import authors, books
from engine_config import connection

# Context manager
# Raises Rollback if there is any Error
# Commits all otherwise
with connection.begin() as transaction:
    # Generating SQL query to get authors data using 'like' filter
    authors_select = connection.execute(
        select(authors).where(
            authors.c.surname.like("%ol%")
        )
    )
    # Setting list of authors data (tuples)
    authors_list = list(authors_select.fetchall())
    # Loop through authors_list
    for i in authors_list:
        # Generating SQL query to get books data using fiter by authors data
        books_select = connection.execute(
            select(books.c.title).where(books.c.author_id == i[0])
        )
        # Setting book title from books data
        title = books_select.fetchone()[0]
        # Generating console output log
        print(f'The book "{title}" is written by {i[1]} {i[2]}')

    # Console output:

    # The book "War and Peace" is written by Lev Tolstoy
    # The book "Dead souls" is written by Nikolay Gogol

    # Generating SQL subquery
    subquery = select(authors.c.id).where(authors.c.surname.like("Bul%"))
    # Generating SQL query using scalar_subquery() method
    data = connection.execute(
        select(books).where(
            books.c.author_id == subquery.scalar_subquery()))
    # Generating console output log
    print(f'My favorite book is "{data.fetchone().title}"')

    # Console output:

    # My favorite book is "Master and Margaret"

# Try-Except manager
# Commits all if 'try' block runs correctly
# 'Except' block raises Rollback

# Setting new transaction
trans = connection.begin()
# Generating SQL query to insert new author data
new_author = authors.insert().values(
    name='Anton',
    surname='Chehov'
)
# Trying insert new data
try:
    connection.execute(new_author)
    # Commiting transacton
    trans.commit()
    # Outputting 'success' console log
    print('Data added successfully')
except Exception('Error while inserting data'):
    # Rolling back transaction and logging out
    trans.rollback()
