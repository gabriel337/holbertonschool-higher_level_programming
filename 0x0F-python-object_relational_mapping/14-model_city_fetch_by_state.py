#!/usr/bin/python3
"""
 prints all City objects from the database hbtn_0e_14_usa
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    cities = (session
              .query(State.name, City.id, City.name)
              .filter(City.state_id == State.id)
              .order_by(City.id))

    for city in cities:
        print("{}: ({}) {}".format(*city))
    session.close()
