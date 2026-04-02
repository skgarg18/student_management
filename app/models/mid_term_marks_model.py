"""
This module defines the MidTermMarksModel, which represents marks of different students in different subjects.
"""

from sqlalchemy import Column, Integer, ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from app.utils.connection_manag import DatabaseManager
from app.models.base_model import DBBase


class MidTermMarksModel(DatabaseManager.Base, DBBase):

    __tablename__ = 'midterm_marks'

    # Composite Primary Key
    student_id = Column(Integer, primary_key=True)
    section_id = Column(Integer, primary_key=True)
    subject_id = Column(Integer, ForeignKey('subjects.subject_id'), primary_key=True)

    marks = Column(Integer)

    # Composite Foreign Key to students table
    __table_args__ = (
        ForeignKeyConstraint(
            ["student_id", "section_id"],
            ["students.id", "students.section_id"]
        ),
    )

    # Relationships
    subject = relationship("SubjectModel", back_populates="marks")

    section = relationship("SectionModel", back_populates="marks")

    student = relationship(
        "StudentModel",
        back_populates="marks",
        primaryjoin="and_(MidTermMarksModel.student_id==StudentModel.id, "
                    "MidTermMarksModel.section_id==StudentModel.section_id)"
    )