from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, BigInteger, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship

# Define the SQLAlchemy session
Base = declarative_base()

# SQLAlchemy models
class ApiUsage(Base):
    __tablename__ = "apiUsage"

    id = Column(BigInteger, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("apiUser.id"), index=True, nullable=False)
    timestamp = Column(DateTime, nullable=False, default=datetime.now())
    route = Column(Text)

    # user = relationship("ApiUser", back_populates="api_usages")

class ApiUser(Base):
    __tablename__ = "apiUser"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, nullable=False)
    token = Column(String, index=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    last_used = Column(DateTime)
    ratelimit = Column(Integer, default=100, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)

    # api_usages = relationship("ApiUsage", back_populates="user")
    # user_perms = relationship("ApiUserPerms", back_populates="user")

class ApiUserPerms(Base):
    __tablename__ = "apiUserPerms"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("apiUser.id"), index=True, nullable=False)
    permission_id = Column(Integer, ForeignKey("apiPermissions.id"), index=True, nullable=False)

    # user = relationship("ApiUser", back_populates="user_perms")
    # permission = relationship("ApiPermissions", back_populates="user_perms")

class ApiPermissions(Base):
    __tablename__ = "apiPermissions"

    id = Column(Integer, primary_key=True, index=True)
    permission = Column(Text, nullable=False)

    # user_perms = relationship("ApiUserPerms", back_populates="permission")
