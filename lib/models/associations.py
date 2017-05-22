from sqlalchemy import Column, ForeignKey, Integer, Table
from . import Base


authors_texts = Table('association', Base.metadata,
                      Column('writing_id', Integer, ForeignKey('writing.id')),
                      Column('author_id', Integer, ForeignKey('author.id')))

authors_quotes = Table('authors_quotes', Base.metadata,
                       Column('quote_id', Integer, ForeignKey('quote.id')),
                       Column('author_id', Integer, ForeignKey('author.id')))

text_collections = Table(
    'collections', Base.metadata,
    Column('collection', Integer, ForeignKey('writing.id'), primary_key=True),
    Column('member', Integer, ForeignKey('writing.id'), primary_key=True))
