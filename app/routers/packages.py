from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..crud import list_packages, create_package as crud_create_package, read_package as crud_read_package, update_package as crud_update_package, delete_package as crud_delete_package
from ..schemas import PackageCreate, PackageUpdate, PackageResponse
from typing import List

router = APIRouter(prefix="/packages", tags=["Packages"])

@router.get("/", response_model=List[PackageResponse])
async def list_all_packages(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    List all packages with pagination.
    """
    return list_packages(db, skip, limit)

@router.post("/", response_model=PackageResponse)
async def create_package(package: PackageCreate, db: Session = Depends(get_db)):
    """
    Create a new package.
    """
    return crud_create_package(db, package)

@router.get("/{package_id}", response_model=PackageResponse)
async def read_package(package_id: int, db: Session = Depends(get_db)):
    """
    Return package details by ID.
    """
    package = crud_read_package(db, package_id)
    if not package:
        raise HTTPException(status_code=404, detail="Package not found")
    return package

@router.put("/{package_id}", response_model=PackageResponse)
async def update_package(package_id: int, package: PackageUpdate, db: Session = Depends(get_db)):
    """
    Update an existing package by ID.
    """
    updated_package = crud_update_package(db, package_id, package)
    if not updated_package:
        raise HTTPException(status_code=404, detail="Package not found")
    return updated_package

@router.delete("/{package_id}")
async def delete_package(package_id: int, db: Session = Depends(get_db)):
    """
    Delete a package by ID.
    """
    success = crud_delete_package(db, package_id)
    if not success:
        raise HTTPException(status_code=404, detail="Package not found")
    return {"msg": "Package deleted successfully!"}

