from sqlalchemy.orm import sessionmaker
from sqlalchemy import func, desc
from sqlalchemy import create_engine
from models import Student, Grade, Subject, Lecturer, Group

DATABASE_URL = "postgresql://username:password@localhost:5432/your_database"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def select_1():
    result = (
        session.query(Student.name, func.avg(Grade.grade).label("avg_grade"))
        .join(Grade)
        .group_by(Student.id)
        .order_by(desc("avg_grade"))
        .limit(5)
        .all()
    )
    return result

def select_2(subject_id):
    result = (
        session.query(Student.name, func.avg(Grade.grade).label("avg_grade"))
        .join(Grade)
        .filter(Grade.subject_id == subject_id)
        .group_by(Student.id)
        .order_by(desc("avg_grade"))
        .first()
    )
    return result

def select_3(subject_id):
    result = (
        session.query(Group.name, func.avg(Grade.grade).label("avg_grade"))
        .join(Student)
        .join(Grade)
        .filter(Grade.subject_id == subject_id)
        .group_by(Group.id)
        .all()
    )
    return result

def select_4(group_id):
    result = (
        session.query(Group.name, func.avg(Grade.grade).label("avg_grade"))
        .join(Student)
        .join(Grade)
        .filter(Student.group_id == group_id)
        .group_by(Group.id)
        .first()
    )
    return result

def select_5(lecturer_id):
    result = (
        session.query(Subject.name)
        .filter(Subject.lecturer_id == lecturer_id)
        .all()
    )
    return result

def select_6(group_id):
    result = session.query(Student.name).filter(Student.group_id == group_id).all()
    return result

def select_7(group_id, subject_id):
    result = (
        session.query(Student.name, Grade.grade)
        .join(Grade)
        .filter(Student.group_id == group_id, Grade.subject_id == subject_id)
        .all()
    )
    return result

def select_8(lecturer_id):
    result = (
        session.query(func.avg(Grade.grade).label("avg_grade"))
        .join(Subject)
        .filter(Subject.lecturer_id == lecturer_id)
        .scalar()
    )
    return result

def select_9(student_id):
    result = (
        session.query(Subject.name)
        .join(Grade)
        .filter(Grade.student_id == student_id, Grade.grade >= 3.0)  
        .all()
    )
    return result

def select_10(lecturer_id, student_id):
    result = (
        session.query(Subject.name)
        .join(Grade)
        .filter(Subject.lecturer_id == lecturer_id, Grade.student_id == student_id)
        .all()
    )
    return result
