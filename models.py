from sqlalchemy import MetaData, Table, String, Column, Text, DateTime, Boolean, Integer, Date
from datetime import datetime

metadata = MetaData()

blog = Table('auth', metadata,
             Column('id', Integer(), primary_key=True, autoincrement=True),
             Column('username', String(200), nullable=False),
             Column('password', String(200), nullable=False),
             Column('secret_key', String(300), nullable=False)
             )
newsArchive = Table('archive', metadata,
                    Column('id', Integer(), primary_key=True, autoincrement=True),
                    Column('title', String(500), nullable=False),
                    Column('content', String(1024), nullable=True),
                    Column('publication_date', Date(), nullable=False)
                    )


def create_db(engine):
    metadata.create_all(engine)
