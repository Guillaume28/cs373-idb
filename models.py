from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

"""
init SQLAlchemy
"""
engine = create_engine('postgresql://postgres:password@104.239.139.162/olympics', echo=False)
Base = declarative_base(engine)

def loadSession():
    metadata = Base.metadata
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

"""
models
"""

class Athlete(Base):
    """
      id
      first_name
      last_name
      gender 
      medal_id: relation to medal model
    """
    __tablename__ = 'athletes'
    __table_args__ = {'autoload':True}

class Event(Base):
    """
      id
      name
      sport_id: relation to sport model
    """
    __tablename__ = 'events'
    __table_args__ = {'autoload':True}
    
class Sport(Base):
    """
      id
      name
    """
    __tablename__ = 'sports'
    __table_args__ = {'autoload':True}
    
class City(Base):
    """
      id
      name
      country_id: relation to countries table
    """
    __tablename__ = 'cities'
    __table_args__ = {'autoload':True}

class Country(Base):
    """
      id
      name
      noc: Name of countries National Olympic Committee
    """
    __tablename__ = 'countries'
    __table_args__ = {'autoload':True}

class Olympics(Base):
    """
      id
      year
      season
      city_id: Relation to the cities table where the games were hosted
    """
    __tablename__ = 'olympics'
    __table_args__ = {'autoload':True}

class Medal(Base):
    """
      id
      athlete_id: Relation to athlete model who won the medal
      country_id: Relation to the country model which was being represented by the athlete
      event_id: Relation to the event model which the medal was one in
      olympic_id: Relation to the olympic model containing the year and season the medal was won in
    """
    __tablename__ = 'medals'
    __table_args__ = {'autoload':True}
