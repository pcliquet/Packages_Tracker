from sqlalchemy.orm import Session
from .models import Package, PackageLocation
from .schemas import PackageCreate, PackageUpdate, PackageLocationCreate


def list_packages(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Package).offset(skip).limit(limit).all()


def create_package(db: Session, package: PackageCreate):
    new_package = Package(
        shipping_date=package.shipping_date,
        status=package.status,
        destination=package.destination,
        weight=package.weight
    )
    db.add(new_package)
    db.commit()
    db.refresh(new_package)
    return new_package


def read_package(db: Session, package_id: int):
    return db.query(Package).filter(Package.id == package_id).first()


def update_package(db: Session, package_id: int, package: PackageUpdate):
    db_package = db.query(Package).filter(Package.id == package_id).first()
    if not db_package:
        return None
    for key, value in package.dict(exclude_unset=True).items():
        setattr(db_package, key, value)
    db.commit()
    db.refresh(db_package)
    return db_package


def delete_package(db: Session, package_id: int):
    db_package = db.query(Package).filter(Package.id == package_id).first()
    if not db_package:
        return False
    db.delete(db_package)
    db.commit()
    return True


def create_package_location(db: Session, package_id: int, location: PackageLocationCreate):
    new_location = PackageLocation(
        package_id=package_id,
        location=location.location,
        registration_date=location.registration_date
    )
    db.add(new_location)
    db.commit()
    db.refresh(new_location)
    return new_location


def list_location_history(db: Session, package_id: int):
    return db.query(PackageLocation).filter(PackageLocation.package_id == package_id).all()
