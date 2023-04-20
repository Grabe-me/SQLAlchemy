from sqlalchemy import select
from engine_config import connection
from Tables import authors, books


# Generating SQL-request to get data from 'authors' table (select)
a = authors.select()
b = select(books).order_by(books.c.author_id)
# Getting data with conn by select
data_a = connection.execute(a)
data_b = connection.execute(b)
# Extracting data
fetch_a = data_a.fetchall()
fetch_b = data_b.fetchall()
# Printing data
while fetch_a and fetch_b:
    fetch_a_pop = fetch_a.pop()
    fetch_b_pop = fetch_b.pop()
    print(
        fetch_a_pop.name,
        fetch_a_pop.surname,
        '-->',
        fetch_b_pop.title
    )

# Selecting filtered data
# Generating SQL request with 'where' condition and 'like' fiter
select_gogol = select(authors).where(authors.c.surname.like("Gog%"))
# Executing filtered data
gogol = connection.execute(select_gogol).fetchone()
# Generating SQL request with 'where' condition
gogol_book = select(books).where(books.c.author_id == int(gogol.id))
# Executing data
dead_souls = connection.execute(gogol_book).fetchone()
# Console output: The book "Dead souls" was written by Nikolay Gogol.
print(f'The book "{dead_souls.title}" was written by {gogol.name} {gogol.surname}.')


select_lev = select(authors.c.name, ).where(authors.c.surname == 'Tolstoy')
lev = connection.execute(select_lev).fetchone()
print(lev[0])