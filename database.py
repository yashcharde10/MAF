from sqlalchemy import Integer, Column, String, create_engine, Text, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# 1. DATABASE FILE --> Setting up database file 
DATABASE_URL = "sqlite:///./chat_history.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread":False})
Session_Local = sessionmaker(autoflush=False, bind=engine)
Base = declarative_base()

# Create Chat Table 
class ChatHistory(Base):
    __tablename__ = "chats"

    id = Column(Integer, primary_key=True, index=True)
    user_query = Column(Text)
    ai_response = Column(Text)
    timestamp = Column(DateTime, default=func.now())
    # we are saving thread_id for memory 
    thread_id = Column(Text)

def init_db():
    Base.metadata.create_all(bind=engine)