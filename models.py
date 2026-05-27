from sqlalchemy import Column, Integer, String, Float
from database import Base


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, index=True)

    director = Column(String, nullable=False)

    year = Column(Integer)

    genre = Column(String)

    rating = Column(Float)