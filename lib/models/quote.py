from sqlalchemy import Column, Text, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from . import Base
from .associations import authors_quotes
from .writing import Writing, Author
from datetime import date


class Quote(Base):
    """ Text mapper class.

        Inherits from BaseModel:
            fields '__tablename__', 'id'
            method '__repr__'
    """

    quote = Column(Text, nullable=False)
    _authors = relationship("Author", secondary=authors_quotes,
                            backref="quotes", lazy="joined")
    _source_id = Column(Integer, ForeignKey('writing.id'))
    _source = relationship("Writing", backref="quotes", lazy="joined")
    add_date = Column(Date, default=date.today, nullable=False)

    def __str__(self):
        return str(self.quote)

    def __iter__(self):
        for k, v in self.__dict__.items():
            if k in ['_authors', '_source']:
                yield (k[1:], v)
            elif not k.startswith('_'):
                yield (k, v)

    @property
    def authors(self):
        return self._authors

    @authors.setter
    def authors(self, author_list):
        # require that all quote authors be authors on the source (if any)
        if self.source and author_list and \
                not all(map(self.source.authors.__contains__, author_list)):
            raise Exception("Quote authors must be authors on source text.")
        self._authors = author_list

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, writing):
        # require that all quote authors be authors on the source (if any)
        if self.authors and writing and \
                not all(map(writing.authors.__contains__, self.authors)):
            raise Exception("Quote authors must be authors on source text.")
        self._source = writing
