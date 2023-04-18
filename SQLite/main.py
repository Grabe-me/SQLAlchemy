from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm.session import sessionmaker


engine = create_engine('sqlite:///test_alchemy.db', echo=True)
base = declarative_base()


class User(base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    def __repr__(self):
        return '<User(name="{}", fulname="{}")>'.format(self.name, self.fullname)


session = sessionmaker(bind=engine)

user_ivan = User(name='Ivan', fullname='Ivanov')

if __name__ == '__main__':
    engine.connect()
    print(engine)
    # print(user_ivan.id)
    # session.add()
    # print(user_ivan.id)
    # base.metadata.create_all(engine)
