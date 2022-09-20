from sqlalchemy import Column, String, Float
from db.models.base import Base


class Input(Base):
    id = Column(String, primary_key=True, index=True)
    sepal_length = Column(Float, nullable=False)
    sepal_width = Column(Float, nullable=False)
    petal_length = Column(Float, nullable=False)
    petal_width = Column(Float, nullable=False)
