from pydantic import BaseModel


class MovieBase(BaseModel):
    title: str
    director: str
    year: int
    genre: str
    rating: float


class MovieCreate(MovieBase):
    pass


class MovieResponse(MovieBase):
    id: int

    class Config:
        from_attributes = True