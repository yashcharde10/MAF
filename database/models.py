from sqlalchemy import Integer, String, Text, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SupportTickets(Base):
    __tablename__ = 'support_tickets'
    id = Column(Integer, primary_key=True)
    user_email = Column(String(100))
    description = Column(Text)
    status = Column(String(20), default="Open")