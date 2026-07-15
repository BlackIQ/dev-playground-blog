# Datetime
from datetime import datetime, timezone

# FastAPI & SQLAlchemy
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

# Dependencies
from dependencies import get_db
# Model
from models import Tag
# Schemas
from schemas import TagCreate, TagUpdate, TagRead

# FastAPI Router
router = APIRouter(
    prefix="/tags",
    tags=["Tag"]
)


@router.get("", response_model=list[TagRead])
async def all_tags(db: Session = Depends(get_db)):
    db_tags = db.query(Tag).all()

    return db_tags


@router.get("/{tag_id}", response_model=TagRead)
async def get_tag(tag_id: int, db: Session = Depends(get_db)):
    db_tag = db.get(Tag, tag_id)

    if not db_tag:
        raise HTTPException(status_code=404, detail="Tag not found")

    return db_tag


@router.post("", response_model=TagRead, status_code=status.HTTP_201_CREATED)
async def create_tag(tag: TagCreate, db: Session = Depends(get_db)):
    db_tag = Tag(**tag.model_dump())

    db.add(db_tag)

    db.commit()
    db.refresh(db_tag)

    return db_tag


@router.put("/{tag_id}", response_model=TagRead)
async def update_tag(tag_id: int, tag: TagUpdate, db: Session = Depends(get_db)):
    db_tag = db.get(Tag, tag_id)

    if not db_tag:
        raise HTTPException(status_code=404, detail="Tag not found")

    for key, value in tag.model_dump().items():
        setattr(db_tag, key, value)

    db.commit()
    db.refresh(db_tag)

    return db_tag


@router.delete("/{tag_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tag(tag_id: int, db: Session = Depends(get_db)):
    db_tag = db.get(Tag, tag_id)

    if not db_tag:
        raise HTTPException(status_code=404, detail="Tag not found")

    db_tag.deleted_at = datetime.now(timezone.utc)

    db.commit()
    db.refresh(db_tag)

    return None


@router.post("/{tag_id}/restore", status_code=status.HTTP_204_NO_CONTENT)
async def restore_tag(tag_id: int, db: Session = Depends(get_db)):
    db_tag = db.get(Tag, tag_id)

    if not db_tag:
        raise HTTPException(status_code=404, detail="Tag not found")

    db_tag.deleted_at = None

    db.commit()
    db.refresh(db_tag)

    return None
