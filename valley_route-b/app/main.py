from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import Annotated
from app import schemas, crud, models, auth
from app.database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.include_router(auth.router)
models.Base.metadata.create_all(bind=engine)

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[schemas.User, Depends(auth.get_current_user)]


@app.get("/", tags=["User"], status_code=status.HTTP_200_OK, response_model=schemas.UserBase)
async def get_user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed")
    return user


