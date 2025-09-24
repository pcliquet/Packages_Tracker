from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class Package(Base):
    __tablename__ = 'packages'

    id = Column(Integer, primary_key=True, index=True)
    shipping_date = Column(String(255), index=True)  
    status = Column(String(255), index=True)      
    destination = Column(String(255), index=True)     
    weight = Column(Float)

    # Relationship with locations
    locations = relationship("PackageLocation", back_populates="package", cascade="all, delete-orphan")


class PackageLocation(Base):
    __tablename__ = 'package_locations'

    id = Column(Integer, primary_key=True, index=True)
    package_id = Column(Integer, ForeignKey('packages.id'), nullable=False)
    location = Column(String(255), nullable=False)
    registration_date = Column(String(255), nullable=False)

    # Relationship with packages
    package = relationship("Package", back_populates="locations")
    