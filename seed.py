from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Group, Lecturer, Subject, Grade
import random
import datetime

fake = Faker()

engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)
session = Session()

for _ in range(30, 51):
    student = Student(student_name=fake.name())
    session.add(student)

groups_names = ['Group A', 'Group B', 'Group C']
for name in groups_names:
    group = Group(group_name=name)
    session.add(group)

for _ in range(3, 6):
    lecturer = Lecturer(lecturer_name=fake.name())
    session.add(lecturer)

subjects_names = ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'History', 'Geography', 'Literature']
for name in subjects_names:
    lecturer_id = random.randint(3, 6)
    subject = Subject(subject_name=name, lecturer_id=lecturer_id)
    session.add(subject)

students = session.query(Student).all()
subjects = session.query(Subject).all()

for student in students:
    for subject in subjects:
        if random.random() < 0.4:
            grade = round(random.uniform(2, 5), 2)
            grade_date = fake.date_between(start_date='-1y', end_date='today')
            new_grade = Grade(student_id=student.student_id, subject_id=subject.subject_id, grade=grade, grade_date=grade_date)
            session.add(new_grade)

session.commit()
