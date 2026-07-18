# Datetime
from datetime import datetime, timezone

# FastAPI & SQLAlchemy
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from dependencies import get_db  # Dependencies
from models import Post, Tag  # Models
from schemas import PostCreate, PostUpdate, PostRead  # Schemas

# FastAPI Router
router = APIRouter(prefix="/posts", tags=["Post"])


@router.get("", response_model=list[PostRead])
async def all_posts(db: Session = Depends(get_db)):
    db_posts = db.query(Post).all()

    return db_posts


@router.get("/{post_id}", response_model=PostRead)
async def get_post(post_id: int, db: Session = Depends(get_db)):
    db_post = db.get(Post, post_id)

    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")

    return db_post


@router.post("", response_model=PostRead, status_code=status.HTTP_201_CREATED)
async def create_post(post: PostCreate, db: Session = Depends(get_db)):
    date = post.model_dump(exclude=("tag_ids"))

    db_post = Post(**date)

    db_tags = db.query(Tag).filter(Tag.id.in_(post.tag_ids)).all()

    db_post.tags = db_tags

    db.add(db_post)

    db.commit()
    db.refresh(db_post)

    return db_post


@router.put("/{post_id}", response_model=PostRead)
async def update_post(post_id: int, post: PostUpdate, db: Session = Depends(get_db)):
    db_post = db.get(Post, post_id)

    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")

    for key, value in post.model_dump().items():
        setattr(db_post, key, value)

    db.commit()
    db.refresh(db_post)

    return db_post


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post_id: int, db: Session = Depends(get_db)):
    db_post = db.get(Post, post_id)

    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")

    db_post.deleted_at = datetime.now(timezone.utc)

    db.commit()
    db.refresh(db_post)

    return None


@router.post("/{post_id}/restore", status_code=status.HTTP_204_NO_CONTENT)
async def restore_post(post_id: int, db: Session = Depends(get_db)):
    db_post = db.get(Post, post_id)

    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")

    db_post.deleted_at = None

    db.commit()
    db.refresh(db_post)

    return None
