from datetime import datetime
from pydantic import BaseModel

# Pydantic model
class ReportsBase(BaseModel):
    created_at: datetime
    reportedID: int
    reportingID: int
    region_id: int
    x_coord: int
    y_coord: int
    z_coord: int
    timestamp: datetime
    manual_detect: bool = None
    on_members_world: int = None
    on_pvp_world: bool = None
    world_number: int = None
    equip_head_id: int = None
    equip_amulet_id: int = None
    equip_torso_id: int = None
    equip_legs_id: int = None
    equip_boots_id: int = None
    equip_cape_id: int = None
    equip_hands_id: int = None
    equip_weapon_id: int = None
    equip_shield_id: int = None
    equip_ge_value: int = None

class ReportsCreate(ReportsBase):
    pass