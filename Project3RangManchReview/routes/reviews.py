from fastapi import APIRouter,Depends, HTTPException,Query
from models import Review, ReviewCreate, ReviewRead, ReviewUpdate
from database import get_session
from sqlmodel import Session, select,func

router = APIRouter(prefix="/reviews", tags=["Reviews"])

@router.post("/", response_model=ReviewRead)
def create_review(review: ReviewCreate, session: Session = Depends(get_session)):
    db_review=Review(**review.model_dump()) # ** unpacks the dictionary returned by model_dump() and passes it as keyword arguments to the Review constructor
    session.add(db_review)# stages for insertion into the database
    session.commit() #Stores row in the database
    session.refresh(db_review)
    return db_review


@router.get("/", response_model=list[ReviewRead])
def list_reviews(
    play_name:str | None = Query(None, description="Filter reviews by play name"),
    skip: int = Query(0, ge=0, description="Number of reviews to skip"),
    limit: int = Query(10, ge=1, le=50, description="Maximum number of reviews to return"),
    session: Session = Depends(get_session)
) :
    query=select(Review)

    if play_name:
        query=query.where(func.lower(Review.play_name)==play_name.lower())


    query=query.offset(skip).limit(limit)
    reviews=session.exec(query).all() # all -> returns all matching records as a list
    return reviews    



@router.get("/average/{play_name}")
def average_rating(play_name:str,session:Session=Depends(get_session)):

    result=session.exec(select(func.average(Review.rating),func.count(Review.id)).where(func.lower(Review.play_name)==play_name.lower())).first()

    average_rating,total_reviews=result

    if total_reviews==0:
        raise HTTPException(status_code=404, detail=f"No reviews found for the {play_name} play.")

    return {
        "play_name": play_name,
        "average_rating": average_rating,
        "total_reviews": total_reviews
    }


@router.patch("/{review_id}", response_model=ReviewRead)
def update_review(review_id: int, update: ReviewUpdate, session: Session = Depends(get_session) ):
    review = session.get(Review, review_id)
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")

    update_data = update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(review, key, value)

    session.add(review)
    session.commit()
    session.refresh(review)
    return review


@router.delete("/{review_id}")
def delete_review(review_id: int, session: Session = Depends(get_session) ):
    review = session.get(Review, review_id)
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")

    session.delete(review)
    session.commit()

    return {"message": "Review deleted"}


