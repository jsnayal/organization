from pydantic import BaseModel

class OrgCreate(BaseModel):
    organization_name: str
    email: str
    password: str

class OrgResponse(BaseModel):
    id: int
    name: str
    admin_email: str
    dynamic_db_url: str

    class Config:
        orm_mode = True

class AdminLogin(BaseModel):
    admin: str
    password: str
