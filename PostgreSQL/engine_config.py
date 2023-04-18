from sqlalchemy import create_engine, MetaData

# Set DataBase engine, "echo=True" for console logging
engine = create_engine('postgresql://user_name:password@host:port/db_name', echo=True)
# Set MetaData object
metadata = MetaData()
# Set connection
connection = engine.connect()
# Set commit
commit = connection.commit()
