from sqlalchemy import Column, String
from . import Base


class Author(Base):
    """ Author mapper class.

        Inherits from BaseModel:
            fields '__tablename__', 'id'
            method '__repr__'

        Backref fields:
            texts - from Text via authors_texts association
            quotes - from Quote via authors_quotes association
    """

    name = Column(String(50), nullable=False, unique=True, server_default='Unknown')  # NOQA

    def __str__(self):
        return str(self.name)
