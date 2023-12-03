from fastapi import Request, HTTPException, Depends, status, APIRouter
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse

from sqlalchemy.orm import Session
from app import models, schemas, oauth2, utils
from app.database import get_db
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.post("/", status_code=status.HTTP_200_OK,response_model=schemas.Token, response_class=JSONResponse)
def root(user: schemas.Userlogin = Depends(schemas.Userlogin.as_form), db: Session = Depends(get_db)):
    user_enter = db.query(models.Users).filter(models.Users.username == user.username).first()
    print(user_enter.username)
    if not user_enter:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=
                            f"invalid creds of email mix")
    if not utils.verify_password(user.password, user_enter.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=
                            f"invalid creds")
    access_token = oauth2.create_access_token(data={"user_id": user_enter.id})
    print(access_token)
    return {"access_token": access_token, "token_type": "bearer"}
    