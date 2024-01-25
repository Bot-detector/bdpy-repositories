from datetime import datetime
from sqlalchemy import  Column, Integer, BigInteger, Timestamp, Tinyint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# SQLAlchemy model
class StgReports(Base):
    __tablename__ = "stgReports"

    ID = Column(BigInteger, primary_key=True, index=True)
    created_at = Column(Timestamp, nullable=False, default=datetime.now())
    reportedID = Column(Integer, nullable=False)
    reportingID = Column(Integer, nullable=False)
    region_id = Column(Integer, nullable=False)
    x_coord = Column(Integer, nullable=False)
    y_coord = Column(Integer, nullable=False)
    z_coord = Column(Integer, nullable=False)
    timestamp = Column(Timestamp, nullable=False, default=datetime.now())
    manual_detect = Column(Tinyint, default=None)
    on_members_world = Column(Integer, default=None)
    on_pvp_world = Column(Tinyint, default=None)
    world_number = Column(Integer, default=None)
    equip_head_id = Column(Integer, default=None)
    equip_amulet_id = Column(Integer, default=None)
    equip_torso_id = Column(Integer, default=None)
    equip_legs_id = Column(Integer, default=None)
    equip_boots_id = Column(Integer, default=None)
    equip_cape_id = Column(Integer, default=None)
    equip_hands_id = Column(Integer, default=None)
    equip_weapon_id = Column(Integer, default=None)
    equip_shield_id = Column(Integer, default=None)
    equip_ge_value = Column(BigInteger, default=None)
