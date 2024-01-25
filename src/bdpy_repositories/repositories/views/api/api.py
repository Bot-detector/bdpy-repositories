from datetime import datetime
from typing import Optional
from pydantic import BaseModel

# Pydantic models
class ApiUsageBase(BaseModel):
    user_id: int
    timestamp: datetime
    route: Optional[str]

class ApiUsageCreate(ApiUsageBase):
    pass

class ApiUserBase(BaseModel):
    username: str
    token: str
    created_at: datetime = datetime.now()
    last_used: Optional[datetime]
    ratelimit: int = 100
    is_active: bool = True

class ApiUserCreate(ApiUserBase):
    pass

class ApiUserPermsBase(BaseModel):
    user_id: int
    permission_id: int

class ApiUserPermsCreate(ApiUserPermsBase):
    pass

class ApiPermissionsBase(BaseModel):
    permission: str

class ApiPermissionsCreate(ApiPermissionsBase):
    pass