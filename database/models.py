from sqlalchemy import Boolean, Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base


class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, default=None)
    users = relationship("User", back_populates="team")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, index=True)
    status = Column(Boolean, default=True)

    team_id = Column(Integer, ForeignKey("teams.id"))

    team = relationship("Team", back_populates="users")

class Integration(Base):
    __tablename__ = "integrations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, default=None)
    type = Column(String, index=True, default=None)
    token = Column(String, index=True, default=None)
    status = Column(Boolean, default=True)