from sqlalchemy import Column, BigInteger, Integer, BINARY
from .db_session import SqlAlchemyBase


class MapTile(SqlAlchemyBase):
    __tablename__ = 'maptiles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    zoom = Column(Integer, nullable=False)
    x = Column(BigInteger, nullable=False)
    y = Column(BigInteger, nullable=False)
    img = Column(BINARY, nullable=False)
