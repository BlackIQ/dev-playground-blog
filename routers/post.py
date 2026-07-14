# Datetime
from datetime import datetime, timezone

# FastAPI & SQLAlchemy
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

# Dependencies
from dependencies import get_db
# Model
from models import CategoryModel
# Schemas
from schemas import Category, CategoryRead

# FastAPI Router
router = APIRouter(
    prefix="/categories",
    tags=["Category"]
)


@router.get("", response_model=list[CategoryRead])
async def all_categories(db: Session = Depends(get_db)):
    db_categorys = db.query(CategoryModel).all()

    return db_categorys


@router.get("/{category_id}", response_model=CategoryRead)
async def get_category(category_id: int, db: Session = Depends(get_db)):
    db_category = db.get(CategoryModel, category_id)

    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")

    return db_category


@router.post("", response_model=CategoryRead, status_code=status.HTTP_201_CREATED)
async def create_category(category: Category, db: Session = Depends(get_db)):
    db_category = CategoryModel(**category.model_dump())

    db.add(db_category)

    db.commit()
    db.refresh(db_category)

    return db_category


@router.put("/{category_id}", response_model=CategoryRead)
async def update_category(category_id: int, category: Category, db: Session = Depends(get_db)):
    db_category = db.get(CategoryModel, category_id)

    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")

    for key, value in category.model_dump().items():
        setattr(db_category, key, value)

    db.commit()
    db.refresh(db_category)

    return db_category


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(category_id: int, db: Session = Depends(get_db)):
    db_category = db.get(CategoryModel, category_id)

    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")

    db_category.deleted_at = datetime.now(timezone.utc)

    db.commit()
    db.refresh(db_category)

    return None


@router.post("/{category_id}/restore", status_code=status.HTTP_204_NO_CONTENT)
async def restore_category(category_id: int, db: Session = Depends(get_db)):
    db_category = db.get(CategoryModel, category_id)

    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")

    db_category.deleted_at = None

    db.commit()
    db.refresh(db_category)

    return None


@router.get("/{category_id}/posts")
async def category_posts(category_id: int, db: Session = Depends(get_db)):
    pass
