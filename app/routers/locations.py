from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..schemas import PackageLocationCreate, PackageLocationResponse
from ..crud import read_package, create_package_location, list_location_history

router = APIRouter(prefix="/packages", tags=["Location"])

@router.post("/{package_id}/location", response_model=PackageLocationResponse)
async def add_package_location(package_id: int, location: PackageLocationCreate, db: Session = Depends(get_db)):
    """
    Add a location to a package.
    """
    package = read_package(db, package_id)
    if not package:
        raise HTTPException(status_code=404, detail="Package not found")
    return create_package_location(db, package_id, location)

@router.get("/{package_id}/location_history", response_model=List[PackageLocationResponse])
async def list_package_location_history(package_id: int, db: Session = Depends(get_db)):
    """
    List the location history of a package.
    """
    # Check if package exists
    package = read_package(db, package_id)
    if not package:
        raise HTTPException(status_code=404, detail="Package not found")
    
    # Search for history (may return empty list if no locations)
    history = list_location_history(db, package_id)
    return history if history else []
