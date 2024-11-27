import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from src import database, models, schemas, crud, auth

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.post("/org/create", response_model=schemas.OrgResponse)
def create_organization(org: schemas.OrgCreate, db: Session = Depends(database.get_db)):
    existing_org = crud.get_organization_by_name(db, org.organization_name)
    if existing_org:
        raise HTTPException(status_code=400, detail="Organization already exists")
    return crud.create_organization(db, org)

@app.get("/org/get", response_model=schemas.OrgResponse)
def get_organization(organization_name: str, db: Session = Depends(database.get_db)):
    org = crud.get_organization_by_name(db, organization_name)
    if not org:
        raise HTTPException(status_code=404, detail="Organization not found")
    return org

@app.post("/admin/login")
def admin_login(admin_login: schemas.AdminLogin, db: Session = Depends(database.get_db)):
    admin = crud.authenticate_admin(db, admin_login.admin, admin_login.password)
    if not admin:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = auth.create_access_token(data={"sub": admin.admin_email})
    return {"access_token": token, "token_type": "bearer"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
