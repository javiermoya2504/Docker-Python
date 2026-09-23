import logging

from fastapi import Depends, FastAPI, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Student

logger = logging.getLogger("uvicorn.error")

app = FastAPI(title="Students App")
templates = Jinja2Templates(directory="templates")


@app.get("/")
def index(request: Request, db: Session = Depends(get_db)):
    try:
        students = db.query(Student).order_by(Student.student_id).all()
    except SQLAlchemyError:
        logger.warning("No se pudo conectar a la base de datos, mostrando lista vacía.")
        students = []
    return templates.TemplateResponse(
        "index.html", {"request": request, "students": students}
    )


@app.get("/about")
def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})
