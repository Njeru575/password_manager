from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#
DATABASE_URL = 'sqlite:///password_manager.db'


engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    passwords = relationship('Password', back_populates='account')

    def __repr__(self):
        return f"<Account(name={self.name})>"

class Password(Base):
    __tablename__ = 'passwords'
    id = Column(Integer, primary_key=True)
    account_name = Column(String, ForeignKey('accounts.name'), nullable=False)
    password = Column(String, nullable=False)  
    
    account = relationship('Account', back_populates='passwords')

    def __repr__(self):
        return f"<Password(account_name={self.account_name})>"

# Create tables in the database
Base.metadata.create_all(engine)
