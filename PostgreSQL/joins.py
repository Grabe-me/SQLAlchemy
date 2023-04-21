from sqlalchemy import select
from Tables import authors, books
from engine_config import connection

# Generating 'JOIN' SQL request
join = authors.join(books)
# Executing data with inserted 'JOIN' request into 'SELECT' request
data = connection.execute(select(join)).fetchall()
# Setting 'for' loop to get console logs using executed data
for value in data:
    print('The book %s was written by %s %s' % (value.title, value.name, value.surname))

# Console output:
# The book Master and Margaret was written by Michael Bulgakov
# The book War and Peace was written by Lev Tolstoy
# The book Dead souls was written by Nikolay Gogol


# Generating SQL request using 'JOIN', 'WHERE', 'LIKE' constructions
request = select(
    authors.c.name,
    authors.c.surname).select_from(
    authors.join(books)).where(books.c.title.like('%oul%'))
# Executing data with SQL request
data = connection.execute(request).fetchall()
# Setting 'for' loop to get console logs using executed data
for author in data:
    print(f'name: {author.name};\tsurname: {author.surname}')

# Console output:
# name: Nikolay;	surname: Gogol


# Generating SQL request with subrequest included in
subrequest = select(books.c.title).where(
    books.c.author_id.in_(  # start of subquery
        select(authors.c.id).select_from(  # selecting column from 'JOIN' construction
            authors.join(books)).where(
            authors.c.surname.like('%ol%')  # filtering authors' surnames with 'LIKE' operator
        )
    )
)
# Executing data
data = connection.execute(subrequest).fetchall()
# Getting console logs using executed data
print("Book's titles with syllable 'ol' included in:")
for title in data:
    print(f'\t{title.title}')

# Console output:
# Book's titles with syllable 'ol' included in:
# 	War and Peace
# 	Dead souls
