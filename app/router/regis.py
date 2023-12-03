from fastapi import Request, HTTPException, Depends, status, APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
from app import models, schemas, oauth2, utils
from app.database import get_db
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi.templating import Jinja2Templates


router = APIRouter()


templates = Jinja2Templates(directory="app/templates")

@router.get("/registration/", response_class=HTMLResponse)
def registration(request: Request):
    return templates.TemplateResponse("registration.html", {"request": request})

@router.post("/registration/", status_code=status.HTTP_201_CREATED,response_model=schemas.UserRegis, response_class=JSONResponse)
def registration(request: Request, user: schemas.UserCreate = Depends(schemas.UserCreate.as_form), db: Session = Depends(get_db)):
    #username: str = Form(...), password: str = Form(...)
    try:
        hashed_pass = utils.hash(user.password)
        user.password = hashed_pass
        new_user = models.Users(username=user.username, password=user.password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        print("User added successfully")
        #return new_user.username
        return schemas.UserRegis(username=new_user.username, id=new_user.id)
    except IntegrityError as e:
        print(f"Error in database operation: {e}")
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Username already exists. Please choose a different username.")
    except Exception as e:
        print(f"Error in database operation: {e}")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Internal server Error")