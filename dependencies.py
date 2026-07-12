# Import session
from db import session


# Get DB function
def get_db():
    db = session()

    try:
        yield db
    finally:
        db.close()
