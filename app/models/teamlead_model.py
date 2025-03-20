from sqlalchemy import Column, Integer, String
from app.connection.database import Base

class DaftarTL(Base):
    __tablename__ = "team_lead"

    data_id = Column(Integer, primary_key=True, index=True)
    phone = Column(String)
    email = Column(String, unique=True)