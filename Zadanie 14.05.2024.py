from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    student_id = Column(Integer, primary_key=True)
    student_name = Column(String)

class Group(Base):
    __tablename__ = 'groups'

    group_id = Column(Integer, primary_key=True)
    group_name = Column(String)

class Lecturer(Base):
    __tablename__ = 'lecturers'

    lecturer_id = Column(Integer, primary_key=True)
    lecturer_name = Column(String)

class Subject(Base):
    __tablename__ = 'subjects'

    subject_id = Column(Integer, primary_key=True)
    subject_name = Column(String)
    lecturer_id = Column(Integer, ForeignKey('lecturers.lecturer_id'))
    lecturer = relationship("Lecturer", back_populates="subjects")

class Grade(Base):
    __tablename__ = 'grades'

    grade_id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.student_id'))
    subject_id = Column(Integer, ForeignKey('subjects.subject_id'))
    grade = Column(Float)
    grade_date = Column(Date)

    student = relationship("Student", back_populates="grades")
    subject = relationship("Subject", back_populates="grades")

grades = relationship("Grade", back_populates="student")

grades = relationship("Grade", back_populates="subject")

subjects = relationship("Subject", back_populates="lecturer")
