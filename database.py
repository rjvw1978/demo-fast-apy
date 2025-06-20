from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = "postgresql://demo_db_z5oy_user:23V0MyE5fUSq9bjeGQ85ohTgOiamaf0K@dpg-d1ak54je5dus73emfq5g-a.oregon-postgres.render.com/demo_db_z5oy"

engine=create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

