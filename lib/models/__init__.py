from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import sessionmaker


class BaseModel(object):
    """
        Defines utility methods on all models; info on custom base classes at
        http://docs.sqlalchemy.org/en/latest/orm/extensions/declarative/mixins.html  # NOQA
    """

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        items = [(k, map(str, v) if isinstance(v, list) else v)
                 for k, v in dict(self).items()]
        return "{}({})".format(self.__class__.__name__,
                               ", ".join(["{}={}".format(*t) for t in items]))

    def __iter__(self):
        for k, v in self.__dict__.items():
            if not k.startswith('_'):
                yield (k, v)


Base = declarative_base(cls=BaseModel)
# add echo="debug" to for detailed messages, incl. generated SQL
engine = create_engine("mysql://user:password@localhost:3306/mysql_example")


def create_all(engine=engine):
    Base.metadata.create_all(engine)


def session(engine=engine):
    Base.metadata.bind = engine
    return sessionmaker(bind=engine)()
