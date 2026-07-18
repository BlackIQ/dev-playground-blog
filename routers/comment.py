# Datetime
from datetime import datetime, timezone

# FastAPI & SQLAlchemy
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from dependencies import get_db  # Dependencies
from models import Comment  # Model
from schemas import CommentCreate, CommentUpdate, CommentRead  # Schemas

# FastAPI Router
router = APIRouter(prefix="/comments", tags=["Comment"])


@router.get("", response_model=list[CommentRead])
async def all_categories(db: Session = Depends(get_db)):
    db_categories = db.query(Comment).all()

    return db_categories


@router.get("/{comment_id}", response_model=CommentRead)
async def get_comment(comment_id: int, db: Session = Depends(get_db)):
    db_comment = db.get(Comment, comment_id)

    if not db_comment:
        raise HTTPException(status_code=404, detail="Comment not found")

    return db_comment


@router.post("", response_model=CommentRead, status_code=status.HTTP_201_CREATED)
async def create_comment(comment: CommentCreate, db: Session = Depends(get_db)):
    db_comment = Comment(**comment.model_dump())

    db.add(db_comment)

    db.commit()
    db.refresh(db_comment)

    return db_comment


@router.put("/{comment_id}", response_model=CommentRead)
async def update_comment(
    comment_id: int, comment: CommentUpdate, db: Session = Depends(get_db)
):
    db_comment = db.get(Comment, comment_id)

    if not db_comment:
        raise HTTPException(status_code=404, detail="Comment not found")

    for key, value in comment.model_dump().items():
        setattr(db_comment, key, value)

    db.commit()
    db.refresh(db_comment)

    return db_comment


@router.delete("/{comment_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    db_comment = db.get(Comment, comment_id)

    if not db_comment:
        raise HTTPException(status_code=404, detail="Comment not found")

    db_comment.deleted_at = datetime.now(timezone.utc)

    db.commit()
    db.refresh(db_comment)

    return None


@router.post("/{comment_id}/restore", status_code=status.HTTP_204_NO_CONTENT)
async def restore_comment(comment_id: int, db: Session = Depends(get_db)):
    db_comment = db.get(Comment, comment_id)

    if not db_comment:
        raise HTTPException(status_code=404, detail="Comment not found")

    db_comment.deleted_at = None

    db.commit()
    db.refresh(db_comment)

    return None
