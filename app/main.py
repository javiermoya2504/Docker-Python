from fastapi import Depends, FastAPI, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Student

app = FastAPI(title="Students App")
templates = Jinja2Templates(directory="templates")


@app.get("/")
def index(request: Request, db: Session = Depends(get_db)):
    students = db.query(Student).order_by(Student.student_id).all()
    return templates.TemplateResponse(
        "index.html", {"request": request, "students": students}
    )


@app.get("/about")
def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})
