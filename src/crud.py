from sqlalchemy.orm import Session
from src import models
from src.utils import hash_password
from src.constants import databases_path
import os



def create_organization(db: Session, org_data):
    dynamic_db_path = os.path.join(databases_path, org_data.organization_name) + '_db.db'
    dynamic_db_url = f"sqlite:///{dynamic_db_path}"
    organization = None
    try:
        from db_utils import DatabaseUtility
        DatabaseUtility(dynamic_db_url).create_database()
        organization = models.Organization(
            name=org_data.organization_name,
            admin_email=org_data.email,
            admin_password=hash_password(org_data.password),
            dynamic_db_url=dynamic_db_url,
        )
        db.add(organization)
        db.commit()
        db.refresh(organization)
    except Exception as ex:
        print(f"Database not created: ", ex)
    return organization

def get_organization_by_name(db: Session, name: str):
    return db.query(models.Organization).filter(models.Organization.name == name).first()

def authenticate_admin(db: Session, email: str, password: str):
    org = db.query(models.Organization).filter(models.Organization.admin_email == email).first()
    if org and org.admin_password == hash_password(password):
        return org
    return None
