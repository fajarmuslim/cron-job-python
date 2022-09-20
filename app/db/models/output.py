from sqlalchemy import Column, String, Integer
from db.models.base import Base


class Output(Base):
    uuid = Column(Integer, primary_key=True, index=True)
    id = Column(String, nullable=False)
    pred_class = Column(Integer, nullable=False)
