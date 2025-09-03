from pydantic import BaseModel
from typing import Optional

class PackageBase(BaseModel):
    shipping_date: str
    status: str
    destination: str
    weight: float

class PackageCreate(PackageBase):
    pass

class PackageUpdate(BaseModel):
    shipping_date: Optional[str] = None
    status: Optional[str] = None
    destination: Optional[str] = None
    weight: Optional[float] = None

class PackageResponse(PackageBase):
    id: int
    
    class Config:
        from_attributes = True

class LocationBase(BaseModel):
    location: str
    registration_date: str

class PackageLocationCreate(LocationBase):
    pass

class PackageLocationResponse(LocationBase):
    id: int
    package_id: int
    
    class Config:
        from_attributes = True
