#!/usr/bin/python3
"""
"""

from model_state import Base, State
from sqlalchemy import create_engine, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
