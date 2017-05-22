from sqlalchemy import Column, Text, Boolean, SmallInteger
from sqlalchemy.orm import relationship
from . import Base
from .associations import authors_texts, text_collections
from .author import Author  # necessary because of relationship or repr()


class Writing(Base):
    """ Text mapper class.

        Inherits from BaseModel:
            fields '__tablename__', 'id'
            method '__repr__'

        Backref:
            quotes - from Quote
            collections - from self
    """

    title = Column(Text, nullable=False)
    year = Column(SmallInteger)
    year_approximate = Column(Boolean, default=False, nullable=False)
    authors = relationship("Author", secondary=authors_texts, backref="texts")

    # self-referential many-many...a collection is a text that contains texts
    # so contents => this is a collection; collections => that this is in
    # http://docs.sqlalchemy.org/en/latest/orm/join_conditions.html
    contents = relationship(
        "Writing", secondary="collections",
        primaryjoin="Writing.id==collections.c.collection",
        secondaryjoin="Writing.id==collections.c.member",
        backref="collections")

    def __str__(self):
        return str(self.title)
