from sqlalchemy import create_engine, MetaData
from sqlalchemy.exc import SQLAlchemyError

class DatabaseUtility:
    def __init__(self, db_url: str):
        """
        Initialize the DatabaseUtility with the given database URL
        Args:
            db_url (str): The SQLite database URL.
        """
        self.db_url = db_url
        self.engine = None
        self.metadata = MetaData()

    def create_database(self):
        """
        Creates an SQLite database based on the provided URL.
        """
        try:
            # Create the engine
            self.engine = create_engine(self.db_url, echo=True, connect_args={"check_same_thread": False})

            # Initialize the metadata (useful for defining tables later)
            self.metadata.create_all(self.engine)

            print(f"Database successfully created {self.db_url}")
        except SQLAlchemyError as e:
            print(f"Error occurred while creating the database: {e}")
            raise

    def get_engine(self):
        if self.engine is None:
            raise ValueError("Database has not been created yet. Call 'create_database()' first.")
        return self.engine
