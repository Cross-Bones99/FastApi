from sqlmodel import SQLModel, Session, create_engine

DATABASE_URL ="postgresql+psycopg://postgres:Aahan%402003@localhost:5432/rangmanchdb"
engine =create_engine(DATABASE_URL, echo=True)

def create_tables():
    """ Create all the tables defined by SQLModel class"""

    SQLModel.metadata.create_all(engine)

def get_session():
    """Get a new session for interacting with the database for each request."""
    with Session(engine) as session:
        yield session    