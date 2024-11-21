from faker import Faker
from random import randint, choice, uniform
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base, Student, Group, Lecturer, Subject, Grade
from datetime import date, timedelta

DATABASE_URL = "postgresql://username:password@localhost:5432/your_database"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

groups = [Group(name=f"Group {i}") for i in range(1, 4)]
session.add_all(groups)
session.commit()

students = []
for _ in range(50):
    students
