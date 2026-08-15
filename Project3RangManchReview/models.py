from sqlmodel import SQLModel, Field    #Field adds aditional information to the columns of the table
from typing import Optional
from datetime import datetime

class Review(SQLModel,table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    play_name: str = Field(index=True)
    reviewer_name: str
    comment: str
    rating:int = Field(ge=1, le=5, description="Rating must be between 1 and 5")
    created_at:datetime = Field(default_factory=datetime.now)




class ReviewCreate(SQLModel):
    play_name: str
    reviewer_name: str
    comment: str
    rating:int = Field(ge=1, le=5, description="Rating must be between 1 and 5")


class ReviewRead(SQLModel):
    id: int
    play_name: str
    reviewer_name: str
    comment: str
    rating:int
    created_at:datetime

class ReviewUpdate(SQLModel):
    comment: Optional[str] = None
    rating: Optional[int] = Field(default=None, ge=1, le=5)        